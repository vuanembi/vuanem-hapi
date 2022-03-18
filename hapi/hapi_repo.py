from typing import Any
import os
from datetime import datetime

import requests

BASE_URL = "http://portal.hapi.solutions:8880/api/message"
TS_FORMAT = "%Y%m%d"


def parse_dt(timeframe: tuple[datetime, datetime]) -> dict[str, str]:
    start, end = timeframe
    return {
        "from_date": start.strftime(TS_FORMAT),
        "to_date": end.strftime(TS_FORMAT),
    }


def get(uri: str):
    def _get(params: dict[str, Any]) -> list[dict[str, Any]]:
        with requests.get(
            f"{BASE_URL}/{uri}",
            params={
                **params,
                "system": "VUANEM",
                "token": os.getenv("HAPI_TOKEN"),
            },
        ) as r:
            res = r.json()
        data = res["data"]
        return data if data else []

    return _get
