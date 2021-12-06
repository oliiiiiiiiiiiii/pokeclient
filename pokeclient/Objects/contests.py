from typing import Union
import attr
from url import base_url


@attr.s(frozen=True)
class contest:
    def __init__(self, name_or_id: Union[str, int]) -> None:
        self.name_or_id = name_or_id


class contest_type(contest):

    """Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        super().__init__(name_or_id=name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}contest-type/{self.name_or_id}"


@attr.s(frozen=True)
class contest_effect(contest):

    """Contest effects refer to the effects of moves when used in contests."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        super().__init__(name_or_id=name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}contest-effect/{self.name_or_id}"


@attr.s(frozen=True)
class super_contest_effect(contest):

    """Super contest effects refer to the effects of moves when used in super contests."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        super().__init__(name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}super-contest-effect/{self.name_or_id}"
