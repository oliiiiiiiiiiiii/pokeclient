from typing import Union
from dataclasses import dataclass
from ..url import base_url
import httpx

@dataclass(frozen=True)
class Generation:

    """A generation is a grouping of the Pokémon games that
    separates them based on the Pokémon they include.
    In each generation, a new set of Pokémon, Moves,
    Abilities and Types that did not exist
    in the previous generation are released."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}generation/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class Pokedex:

    """A Pokédex is a handheld electronic encyclopedia device;
    one which is capable of recording and retaining information
    of the various Pokémon in a given region with the exception of the national
    dex and some smaller dexes related to portions of a region."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokedex/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class Version:

    """Versions of the games, e.g., Red, Blue or Yellow."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}version/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class VersionGroup:

    """Version groups categorize highly similar versions of the games."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}version-group/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()