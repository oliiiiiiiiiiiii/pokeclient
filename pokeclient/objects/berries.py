from typing import Union
from dataclasses import dataclass
from ..url import base_url

@dataclass(frozen=True)
class berry_firmnesses:

    """Determination of berry's softness or hardness."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}berry-firmness/{self.name_or_id}"


@dataclass(frozen=True)
class berry_flavor:

    """Flavors determine whether a Pokémon will benefit or suffer from eating a berry based
    on their nature."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}berry-flavor/{self.name_or_id}"


@dataclass(frozen=True)
class berry:

    """Berries are small fruits that can provide HP and status condition restoration, stat enhancement,
    and even damage negation when eaten by Pokémon."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}berry/{self.name_or_id}"
