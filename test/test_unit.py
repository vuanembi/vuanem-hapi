import pytest

from hapi.hapi import services
from hapi.hapi_service import pipeline_service
from hapi.hapi_controller import hapi_controller
from tasks.tasks_service import tasks_service


@pytest.fixture(  # type: ignore
    params=services.values(),
    ids=services.keys(),
)
def resource(request):
    return request.param


TIME_FRAME = [
    ("auto", (None, None)),
    ("manual", ("2022-01-01", "2022-02-01")),
]


@pytest.fixture(
    params=[i[1] for i in TIME_FRAME],
    ids=[i[0] for i in TIME_FRAME],
)
def timeframe(request):
    return request.param


class TestPipeline:
    def test_service(self, resource, timeframe):
        res = pipeline_service(resource)(
            {
                "start": timeframe[0],
                "end": timeframe[1],
            }
        )
        res

    def test_controller(self, resource, timeframe):
        res = hapi_controller(
            {
                "resource": resource.name,
                "start": timeframe[0],
                "end": timeframe[1],
            }
        )
        res


class TestTasks:
    def test_service(self, timeframe):
        res = tasks_service(
            {
                "start": timeframe[0],
                "end": timeframe[1],
            }
        )
        res
