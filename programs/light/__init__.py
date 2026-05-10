import asyncio
import json
import urllib.parse
import urllib.request
from collections import deque
from datetime import datetime, date, timedelta
from driver import driver, motion_driver
from tools import get_color
from InquirerPy import inquirer
from InquirerPy.utils import patched_print
from .config import LATITUDE, LONGITUDE, SUN_API_URL, FORCE_DAY, FORCE_NIGHT


class Light:
    def __init__(self):
        self.quit = asyncio.Event()
        self.color = get_color("W")
        self.lines = 0
        self.motion_history = deque([0] * 10, maxlen=10)
        self.pir_init_task = None
        self.sun_update_task = None
        self.sunrise = None
        self.sunset = None
        self.local_tz = datetime.now().astimezone().tzinfo

    @classmethod
    async def run(cls):
        light = cls()
        light.pir_init_task = asyncio.create_task(motion_driver.initialize())
        light.sun_update_task = asyncio.create_task(light.sun_update_loop())
        await asyncio.gather(light.loop(), light.stop(), light.sun_update_task)
        driver.clear()

    async def loop(self):
        while not self.quit.is_set():
            if motion_driver.initialized:
                self.frame()
            await asyncio.sleep(0.5)

    async def stop(self):
        await inquirer.text(message="Quitter:").execute_async()
        if self.pir_init_task:
            self.pir_init_task.cancel()
        self.quit.set()

    def frame(self):
        if self.is_daytime():
            self.clear_if_day()
            return

        motion = motion_driver.read()
        self.motion_history.append(1 if motion else 0)

        total = sum(self.motion_history)
        delta = 1 if total > 0 else -1
        lines = max(0, min(self.lines + delta, 5))
        if self.lines == lines:
            return
        self.lines = lines

        driver.clear(False)
        for y in range(6, 6 - self.lines, -1):
            for x in range(6):
                driver.set(x, y, self.color)
        driver.show()

    def clear_if_day(self):
        if self.lines != 0:
            self.lines = 0
            driver.clear()
            driver.show()

    async def sun_update_loop(self):
        while not self.quit.is_set():
            await self.fetch_sun_times()
            await self.wait_until_next_boundary()

    async def fetch_sun_times(self):
        if FORCE_NIGHT:
            patched_print("sun schedule: mode forcé nuit")
            return
        if FORCE_DAY:
            patched_print("sun schedule: mode forcé jour")
            return

        url = self.build_sun_api_url()
        try:
            data = await asyncio.to_thread(self.download_url, url)
            payload = json.loads(data)
        except Exception as exc:
            patched_print("sun schedule: échec de la requête", exc)
            return

        results = payload.get("results") if isinstance(payload, dict) else None
        if results is None:
            results = payload

        sunrise = results.get("sunrise")
        sunset = results.get("sunset")
        if sunrise is None or sunset is None:
            patched_print("sun schedule: réponse API sans sunrise/sunset")
            return

        try:
            self.sunrise = self.parse_sun_time(sunrise)
            self.sunset = self.parse_sun_time(sunset)
            patched_print("sun schedule: sunrise=", self.sunrise, "sunset=", self.sunset)
        except Exception as exc:
            patched_print("sun schedule: impossible de parser les heures", exc)

    def build_sun_api_url(self):
        query = {
            "lat": LATITUDE,
            "lng": LONGITUDE,
            "formatted": 0,
        }
        return f"{SUN_API_URL}?{urllib.parse.urlencode(query)}"

    def download_url(self, url):
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode("utf-8")

    def parse_sun_time(self, value):
        if isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value)
            except ValueError:
                dt = datetime.strptime(value, "%I:%M:%S %p")
                dt = datetime.combine(date.today(), dt.time())
                dt = dt.replace(tzinfo=self.local_tz)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=self.local_tz)
            return dt.astimezone(self.local_tz)
        raise ValueError("invalid sun time format")

    async def wait_until_next_boundary(self):
        if self.sunrise is None or self.sunset is None:
            await asyncio.wait([self.quit.wait()], timeout=3600)
            return

        now = datetime.now(self.local_tz)
        if now < self.sunrise:
            target = self.sunrise
        elif now < self.sunset:
            target = self.sunset
        else:
            tomorrow = now + timedelta(days=1)
            target = datetime(
                tomorrow.year,
                tomorrow.month,
                tomorrow.day,
                0,
                1,
                tzinfo=self.local_tz,
            )

        delay = max(0, (target - now).total_seconds())
        await asyncio.wait([self.quit.wait()], timeout=delay)

    def is_daytime(self):
        if FORCE_NIGHT:
            return False
        if FORCE_DAY:
            return True
        if self.sunrise is None or self.sunset is None:
            now = datetime.now(self.local_tz)
            return 6 <= now.hour < 22
        now = datetime.now(self.local_tz)
        return self.sunrise <= now <= self.sunset
