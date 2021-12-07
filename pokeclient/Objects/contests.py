from typing import Union
from attr import attr
from attr.setters import frozen
from url import base_url


@attr.s(frozen=True)
class contest:
    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)


@attr.s(frozen=True)
class contest_type:

    """Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}contest-type/{self.name_or_id}"


@attr.s(frozen=True)
class contest_effect:

    """Contest effects refer to the effects of moves when used in contests."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}contest-effect/{self.name_or_id}"


@attr.s(frozen=True)
class super_contest_effect:

    """Super contest effects refer to the effects of moves when used in super contests."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}super-contest-effect/{self.name_or_id}"