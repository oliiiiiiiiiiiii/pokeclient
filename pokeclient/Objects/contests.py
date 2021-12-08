from typing import Union
from dataclasses import dataclass
from url import base_url


@dataclass(frozen=True)
class contest_type:

    """Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}contest-type/{self.name_or_id}"


@dataclass(frozen=True)
class contest_effect:

    """Contest effects refer to the effects of moves when used in contests."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}contest-effect/{self.name_or_id}"


@dataclass(frozen=True)
class super_contest_effect:

    """Super contest effects refer to the effects of moves when used in super contests."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}super-contest-effect/{self.name_or_id}"
