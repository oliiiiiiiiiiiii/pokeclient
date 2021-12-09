from typing import Union
from dataclasses import dataclass
from .. import url

base_url = url.base_url


@dataclass(frozen=True)
class generation:

    """A generation is a grouping of the Pokémon games that
    separates them based on the Pokémon they include.
    In each generation, a new set of Pokémon, Moves,
    Abilities and Types that did not exist
    in the previous generation are released."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}generation/{self.name_or_id}"


@dataclass(frozen=True)
class pokedex:

    """A Pokédex is a handheld electronic encyclopedia device;
    one which is capable of recording and retaining information
    of the various Pokémon in a given region with the exception of the national
    dex and some smaller dexes related to portions of a region."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokedex/{self.name_or_id}"


@dataclass(frozen=True)
class version:

    """Versions of the games, e.g., Red, Blue or Yellow."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}version/{self.name_or_id}"


@dataclass(frozen=True)
class version_groups:

    """Version groups categorize highly similar versions of the games."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}version-group/{self.name_or_id}"
