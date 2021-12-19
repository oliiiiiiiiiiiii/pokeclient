from typing import Union, Any
from dataclasses import dataclass
from ..url import base_url
import httpx

@dataclass(frozen=True)
class Machine:

    """Machines are the representation of items that
    teach moves to Pokémon. They vary from version to version, so it is not certain that one
    specific TM or HM corresponds to a single Machine."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}machine/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()