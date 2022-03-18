from typing import Callable, Any, Protocol, Optional
from dataclasses import dataclass


class ParamsFn(Protocol):
    def __call__(self, *args) -> dict[str, Any]:
        pass


@dataclass
class Resource:
    name: str
    uri: str
    transform: Callable[[list[dict[str, Any]]], list[dict[str, Any]]]
    schema: list[dict[str, Any]]
    params_fn: ParamsFn = lambda _: {}  # type: ignore
    id_key: Optional[str] = None
    cursor_key: Optional[str] = None
