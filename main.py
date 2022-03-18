from hapi.hapi_controller import hapi_controller
from tasks.tasks_service import tasks_service


def main(request):
    data = request.get_json()

    print(data)

    if "resource" in data:
        response = hapi_controller(data)
    elif "tasks" in data:
        response = tasks_service(data)
    else:
        raise ValueError(data)

    print(response)

    return response
