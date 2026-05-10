from . import config
import asyncio
from InquirerPy.utils import patched_print
import json
import os.path
import time
from datetime import datetime


class Sun:
    data_path = os.path.join(os.path.dirname(__file__), "data.json")
    data = {}
    last_update = datetime.fromtimestamp(0)

    def __init__(self):
        self.readJsonData()

    def readJsonData(self):
        mtime = os.path.getmtime(self.data_path)
        self.last_update = datetime.fromtimestamp(mtime)
        with open(self.data_path, "r") as f:
            self.data = json.loads(f.read())

    async def request(self):
        pass

    async def isNight(self):
        return True
