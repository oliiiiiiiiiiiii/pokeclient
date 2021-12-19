from typing import Union
from dataclasses import dataclass
import httpx
import json
from ..url import base_url
from ..cache import Contests
from ..errors import ContestNotFound
from typing import Any

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
                ContestCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ContestCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ContestCache(self.name_or_id)
                        else:
                            ContestCache.contest_type(data.get('id'), data)
                            ContestCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ContestNotFound(self.name_or_id)
                return
        data = ContestCache.contest_type.get(id)
        return data


@dataclass(frozen=True)
class ContestEffect:
    """Contest effects refer to the effects of moves when used in contests."""

    name_or_id: Union[str, int]
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
                raise ContestNotFound(self.name_or_id)
            else:
                ContestCache.add_contest_effect(data.get('id'), data)
                ContestCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ContestCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ContestCache(self.name_or_id)
                        else:
                            ContestCache.contest_effect(data.get('id'), data)
                            ContestCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ContestNotFound(self.name_or_id)
                return
        data = ContestCache.contest_effect.get(id)
        return data


@dataclass(frozen=True)
class SuperContestEffect:
    """Super contest effects refer to the effects of moves when used in super contests."""

    name_or_id: Union[str, int]
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
                raise ContestNotFound(self.name_or_id)
            else:
                ContestCache.add_super_contest_effect(data.get('id'), data)
                ContestCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ContestCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ContestCache(self.name_or_id)
                        else:
                            ContestCache.super_contest_effect(data.get('id'), data)
                            ContestCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ContestNotFound(self.name_or_id)
                return
        data = ContestCache.super_contest_effect.get(id)
        return data
