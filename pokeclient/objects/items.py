from typing import Union
from dataclasses import dataclass
from ..url import base_url


@dataclass(frozen=True)
class item_attribute:

    """An item is an object in the games which the
    player can pick up, keep in their bag, and use
    in some manner. They have various uses,
    including healing, powering up,
    helping catch Pokémon, or to access a new area."""

    name_or_id: Union[str, int]

    @property
    def url(self):
        return f"{base_url}item-attribute/{self.name_or_id}/"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class item_category:

    """Item categories determine where
    items will be placed in the players bag."""

    name_or_id: Union[str, int]

    @property
    def url(self):
        return f"{base_url}item-category/{self.name_or_id}/"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class item_fling_effect:

    """The various effects of the move
    "Fling" when used with different items."""

    name_or_id: Union[str, int]

    @property
    def url(self):
        return f"{base_url}item-fling-effect/{self.name_or_id}/"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class item_pocket:

    """Pockets within the
    players bag used for storing items by category."""

    name_or_id: Union[str, int]

    @property
    def url(self):
        return f"{base_url}item-pocket/{self.name_or_id}/"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class item:

    """An item is an object in the games which
    the player can pick up, keep in their bag,
    and use in some manner.
    They have various uses, including healing, powering up,
    helping catch Pokémon, or to access a new area."""

    name_or_id: Union[str, int]

    @property
    def url(self):
        return f"{base_url}item/{self.name_or_id}/"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()