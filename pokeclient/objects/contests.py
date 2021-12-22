from typing import Union, Any
from dataclasses import dataclass
import httpx
import json
from ..url import base_url
from ..cache import Contests
from ..errors import ContestNotFound

ContestCache = Contests()


@dataclass(frozen=True)
class ContestType:
    """Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests."""

    name_or_id: Union[str, int]
    from_cache: bool = False

    @property
    def url(self) -> str:
        return f"{base_url}contest-type/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ContestNotFound(self.name_or_id)
            else:
                ContestCache.add_contest_type(data.get('id'), data)
                ContestCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ContestCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ContestCache(self.name_or_id)
                        else:
                            ContestCache.add_contest_type(data.get('id'), data)
                            ContestCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ContestNotFound(self.name_or_id)
        data = ContestCache.contest_types.get(id)
        return data


@dataclass(frozen=True)
class ContestEffect:
    """Contest effects refer to the effects of moves when used in contests."""

    id: int
    from_cache: bool = False

    @property
    def url(self) -> str:
        return f"{base_url}contest-effect/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ContestNotFound(self.id)
            else:
                ContestCache.add_contest_effect(data.get('id'), data)
                return data 
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise ContestNotFound(self.id)
                    else:
                        ContestCache.add_contest_effect(data.get('id'), data)
                        return data 
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise ContestNotFound(self.id)
        data = ContestCache.contest_effects.get(id)
        return data 

@dataclass(frozen=True)
class SuperContestEffect:
    """Super contest effects refer to the effects of moves when used in super contests."""

    id: int
    from_cache: bool = False

    @property
    def url(self) -> str:
        return f"{base_url}super-contest-effect/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ContestNotFound(self.id)
            else:
                ContestCache.add_super_contest_effect(data.get('id'), data)
                return data 
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise ContestNotFound(self.id)
                    else:
                        ContestCache.add_super_contest_effect(data.get('id'), data)
                        return data 
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise ContestNotFound(self.id)
        data = ContestCache.super_contest_effects.get(id)
        return data 
