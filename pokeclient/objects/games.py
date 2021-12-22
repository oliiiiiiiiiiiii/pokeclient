from typing import Union, Any
from dataclasses import dataclass
import httpx
import json
from ..url import base_url
from ..cache import Games
from ..errors import GameNotFound

GameCache = Games()

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
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise GameNotFound(self.name_or_id)
            else:
                GameCache.add_generation(data.get('id'), data)
                GameCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = GameCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise GameNotFound(self.name_or_id)
                        else:
                            GameCache.add_generation(data.get('id'), data)
                            GameCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise GameNotFound(self.name_or_id)
        data = GameCache.generations.get(id)
        return data

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
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise GameNotFound(self.name_or_id)
            else:
                GameCache.add_pokedex(data.get('id'), data)
                GameCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = GameCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise GameNotFound(self.name_or_id)
                        else:
                            GameCache.add_pokedex(data.get('id'), data)
                            GameCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise GameNotFound(self.name_or_id)
        data = GameCache.pokedexes.get(id)
        return data

@dataclass(frozen=True)
class Version:

    """Versions of the games, e.g., Red, Blue or Yellow."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}version/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise GameNotFound(self.name_or_id)
            else:
                GameCache.add_version(data.get('id'), data)
                GameCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = GameCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise GameNotFound(self.name_or_id)
                        else:
                            GameCache.add_version(data.get('id'), data)
                            GameCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise GameNotFound(self.name_or_id)
        data = GameCache.versions.get(id)
        return data

@dataclass(frozen=True)
class VersionGroup:

    """Version groups categorize highly similar versions of the games."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}version-group/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise GameNotFound(self.name_or_id)
            else:
                GameCache.add_version_group(data.get('id'), data)
                GameCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = GameCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise GameNotFound(self.name_or_id)
                        else:
                            GameCache.add_version_group(data.get('id'), data)
                            GameCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise GameNotFound(self.name_or_id)
        data = GameCache.version_groups.get(id)
        return data