from typing import Union
from dataclasses import dataclass
from .. import url

base_url = url.base_url


@dataclass(frozen=True)
class location:

    """Locations that can be visited within the games.
    Locations make up sizable portions of regions,
    like cities or routes."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}location/{self.name_or_id}"


@dataclass(frozen=True)
class location_area:

    """Location areas are sections of areas,
    such as floors in a building or cave.
    Each area has its own set of
    possible Pokémon encounters."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}location-area/{self.name_or_id}"


@dataclass(frozen=True)
class pal_park_area:

    """Areas used for grouping Pokémon encounters in Pal Park."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pal-park-area/{self.name_or_id}"


@dataclass(frozen=True)
class region:

    """A region is an organized area of the Pokémon world.
    Most often, the main difference
    between regions is the species
    of Pokémon that can be encountered within them."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}region/{self.name_or_id}"
