from hapi.hapi.interface import Resource
from hapi.hapi.utils import parse_ts

upload_list = Resource(
    "UploadList",
    "list_uploads",
    lambda rows: [
        {
            "campaign": row.get("campaign"),
            "create_date": parse_ts(row.get("create_date")),
            "create_uid": row.get("create_uid"),
            "errors": row.get("errors"),
            "id": row.get("id"),
            "message_type": row.get("message_type"),
            "name": row.get("name"),
            "process_mode": row.get("process_mode"),
            "sends": row.get("sends"),
            "service": row.get("service"),
            "status": row.get("status"),
            "system": row.get("system"),
            "template": row.get("template"),
            "total": row.get("total"),
            "write_date": parse_ts(row.get("write_date")),
            "write_uid": row.get("write_uid"),
        }
        for row in rows
    ],
    [
        {"name": "campaign", "type": "NUMERIC"},
        {"name": "create_date", "type": "TIMESTAMP"},
        {"name": "create_uid", "type": "NUMERIC"},
        {"name": "errors", "type": "NUMERIC"},
        {"name": "id", "type": "NUMERIC"},
        {"name": "message_type", "type": "STRING"},
        {"name": "name", "type": "STRING"},
        {"name": "process_mode", "type": "STRING"},
        {"name": "sends", "type": "NUMERIC"},
        {"name": "service", "type": "NUMERIC"},
        {"name": "status", "type": "STRING"},
        {"name": "system", "type": "NUMERIC"},
        {"name": "template", "type": "NUMERIC"},
        {"name": "total", "type": "NUMERIC"},
        {"name": "write_date", "type": "TIMESTAMP"},
        {"name": "write_uid", "type": "NUMERIC"},
    ],
)
