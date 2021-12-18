from typing import Union
from dataclasses import dataclass
import httpx
import json
from ..url import base_url
from ..cache import Berries
from ..errors import BerryNotFound

BerryCache = Berries()


@dataclass(frozen=True)
class BerryFirmness:
    """Determination of berry's softness or hardness."""

    name_or_id: Union[str, int]
    from_cache: bool = False

    @property
    def url(self) -> str:
        return f"{base_url}berry-firmness/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise BerryNotFound(self.name_or_id)
            else:
                BerryCache.add_berry_firmness(data.get('id'), data)
                BerryCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = BerryCache.name_to_id_dict.get(
                            self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise BerryNotFound(self.name_or_id)
                        else:
                            BerryCache.add_berry_firmness(
                                data.get('id'), data)
                            BerryCache.name_to_id_dict[data.get(
                                'name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise BerryNotFound(self.name_or_id)
                return
        data = BerryCache.berry_firmness.get(id)
        return data


@dataclass(frozen=True)
class BerryFlavour:
    """Flavors determine whether a Pokémon will benefit or suffer from eating a berry based
    on their nature."""

    name_or_id: Union[str, int]
    from_cache: bool = False

    @property
    def url(self) -> str:
        return f"{base_url}berry-flavor/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise BerryNotFound(self.name_or_id)
            else:
                BerryCache.add_berry_flavour(data.get('id'), data)
                BerryCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = BerryCache.name_to_id_dict.get(
                            self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise BerryNotFound(self.name_or_id)
                        else:
                            BerryCache.add_berry_flavour(data.get('id'), data)
                            BerryCache.name_to_id_dict[data.get(
                                'name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise BerryNotFound(self.name_or_id)
                return
        data = BerryCache.add_berry_flavour.get(id)
        return data


@dataclass(frozen=True)
class Berry:
    """Berries are small fruits that can provide HP and status condition restoration, stat enhancement,
    and even damage negation when eaten by Pokémon."""

    name_or_id: Union[str, int]
    from_cache: bool = False

    @property
    def url(self) -> str:
        return f"{base_url}berry/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise BerryNotFound(self.name_or_id)
            else:
                BerryCache.add_berry(data.get('id'), data)
                BerryCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = BerryCache.name_to_id_dict.get(
                            self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise BerryNotFound(self.name_or_id)
                        else:
                            BerryCache.add_berry(data.get('id'), data)
                            BerryCache.name_to_id_dict[data.get(
                                'name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise BerryNotFound(self.name_or_id)
                return
        data = BerryCache.add_berry.get(id)
        return data
