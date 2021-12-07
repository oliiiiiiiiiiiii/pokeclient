from typing import Union
import attr
from url import base_url


@attr.s(frozen=True)
class berry_firmnesses:

    """Determination of berry's softness or hardness."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}berry-firmness/{self.name_or_id}"


@attr.s(frozen=True)
class berry_flavor:

    """Flavors determine whether a Pokémon will benefit or suffer from eating a berry based
    on their nature."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}berry-flavor/{self.name_or_id}"



@attr.s(frozen=True)
class berry:

    """Berries are small fruits that can provide HP and status condition restoration, stat enhancement,
    and even damage negation when eaten by Pokémon."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self) -> str:
        return f"{base_url}berry/{self.name_or_id}"