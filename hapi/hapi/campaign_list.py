from hapi.hapi.interface import Resource
from hapi.hapi.utils import parse_ts

campaign_list = Resource(
    "CampaignList",
    "list_campaigns",
    lambda rows: [
        {
            "code": row.get("code"),
            "create_date": parse_ts(row.get("create_date")),
            "create_uid": row.get("create_uid"),
            "description": row.get("description"),
            "end_date": parse_ts(row.get("end_date")),
            "id": row.get("id"),
            "is_active": row.get("is_active"),
            "name": row.get("name"),
            "start_date": parse_ts(row.get("start_date")),
            "system": row.get("system"),
            "write_date": parse_ts(row.get("write_date")),
            "write_uid": row.get("write_uid"),
        }
        for row in rows
    ],
    [
        {"name": "code", "type": "STRING"},
        {"name": "create_date", "type": "TIMESTAMP"},
        {"name": "create_uid", "type": "NUMERIC"},
        {"name": "description", "type": "STRING"},
        {"name": "end_date", "type": "TIMESTAMP"},
        {"name": "id", "type": "NUMERIC"},
        {"name": "is_active", "type": "BOOLEAN"},
        {"name": "name", "type": "STRING"},
        {"name": "start_date", "type": "TIMESTAMP"},
        {"name": "system", "type": "NUMERIC"},
        {"name": "write_date", "type": "TIMESTAMP"},
        {"name": "write_uid", "type": "NUMERIC"},
    ],
)
