from typing import Optional

from dateutil.parser import parse


def parse_ts(x: Optional[str]) -> Optional[str]:
    return parse(x).isoformat(timespec="seconds") if x else None
