from . import config
from InquirerPy.utils import patched_print
import json
import os.path
from datetime import datetime
from tools import get_minutes


class Sun:
    data_path = os.path.join(os.path.dirname(__file__), "data.json")
    data = {}
    last_update = datetime.fromtimestamp(0)
    sunrise_minutes = 8 * 60
    sunset_minutes = 20 * 60

    def __init__(self):
        self.readJsonData()

    def parseData(self, results):
        sunrise_dt = datetime.fromisoformat(results["sunrise"])
        sunset_dt = datetime.fromisoformat(results["sunset"])
        self.sunrise_minutes = get_minutes(sunrise_dt)
        self.sunset_minutes = get_minutes(sunset_dt)

    def readJsonData(self):
        mtime = os.path.getmtime(self.data_path)
        self.last_update = datetime.fromtimestamp(mtime)
        with open(self.data_path, "r") as f:
            self.data = json.loads(f.read())
            self.parseData(self.data["results"])

    async def request(self):
        pass

    async def isNight(self):
        now_minutes = get_minutes(datetime.now())
        is_day = self.sunrise_minutes < now_minutes < self.sunset_minutes
        return not is_day
