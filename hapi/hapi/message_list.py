from compose import compose

from db.bigquery import get_last_ts
from hapi.hapi.interface import Resource
from hapi.hapi.utils import parse_ts
from hapi.hapi_repo import parse_dt

message_list = Resource(
    "MessageList",
    "list",
    lambda rows: [
        {
            "create_date": parse_ts(row.get("create_date")),
            "create_uid": row.get("create_uid"),
            "data": row.get("data"),
            "error_message": row.get("error_message"),
            "id": row.get("id"),
            "message_content": row.get("message_content"),
            "message_type": row.get("message_type"),
            "receiver": row.get("receiver"),
            "sender": row.get("sender"),
            "service_code": row.get("service_code"),
            "status": row.get("status"),
            "subject": row.get("subject"),
            "sys_code": row.get("sys_code"),
            "system": row.get("system"),
            "system_code": row.get("system_code"),
            "template_code": row.get("template_code"),
            "template_content": row.get("template_content"),
            "write_date": parse_ts(row.get("write_date")),
            "write_uid": row.get("write_uid"),
        }
        for row in rows
    ],
    [
        {"name": "create_date", "type": "TIMESTAMP"},
        {"name": "create_uid", "type": "NUMERIC"},
        {"name": "data", "type": "STRING"},
        {"name": "error_message", "type": "STRING"},
        {"name": "id", "type": "NUMERIC"},
        {"name": "message_content", "type": "STRING"},
        {"name": "message_type", "type": "STRING"},
        {"name": "receiver", "type": "STRING"},
        {"name": "sender", "type": "STRING"},
        {"name": "service_code", "type": "STRING"},
        {"name": "status", "type": "STRING"},
        {"name": "subject", "type": "STRING"},
        {"name": "sys_code", "type": "STRING"},
        {"name": "system", "type": "STRING"},
        {"name": "system_code", "type": "STRING"},
        {"name": "template_code", "type": "STRING"},
        {"name": "template_content", "type": "STRING"},
        {"name": "write_date", "type": "TIMESTAMP"},
        {"name": "write_uid", "type": "NUMERIC"},
    ],
    params_fn=compose(
        parse_dt,
        get_last_ts("MessageList", "create_date"),
        lambda body: (body.get("start"), body.get("end")),
    ),
    id_key="id",
    cursor_key="create_date",
)
