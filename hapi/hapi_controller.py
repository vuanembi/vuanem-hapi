from typing import Any

from hapi.hapi import services
from hapi.hapi_service import pipeline_service


def hapi_controller(body: dict[str, Any]):
    if body["table"] in services:
        return pipeline_service(services[body["table"]])(body)
