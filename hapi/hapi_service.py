from typing import Optional, Any, Union

from compose import compose

from hapi.hapi import interface
from hapi import hapi_repo
from db import bigquery


def pipeline_service(resource: interface.Resource):
    def _svc(body: Optional[dict[str, Any]]) -> dict[str, Union[str, int]]:
        return compose(
            lambda x: {
                "resource": resource.name,
                "output_rows": x,
            },
            bigquery.load(
                resource.name,
                resource.schema,
                resource.id_key,
                resource.cursor_key,
            ),
            resource.transform,
            hapi_repo.get(resource.uri),
            resource.params_fn,
        )(body)

    return _svc
