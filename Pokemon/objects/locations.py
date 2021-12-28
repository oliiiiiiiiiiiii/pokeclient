from typing import Union, Any
from dataclasses import dataclass
import httpx
import json
from ..url import base_url
from ..cache import Locations
from ..errors import LocationNotFound

LocationCache = Locations()

@dataclass(frozen=True)
class Location:

    """Locations that can be visited within the games.
    Locations make up sizable portions of regions,
    like cities or routes."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}location/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise LocationNotFound(self.name_or_id)
            else:
                LocationCache.add_location(data.get('id'), data)
                LocationCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = LocationCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise LocationNotFound(self.name_or_id)
                        else:
                            LocationCache.add_location(data.get('id'), data)
                            LocationCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise LocationNotFound(self.name_or_id)
        data = LocationCache.locations.get(id)
        return data

@dataclass(frozen=True)
class LocationArea:

    """Location areas are sections of areas,
    such as floors in a building or cave.
    Each area has its own set of
    possible Pokémon encounters."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}location-area/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise LocationNotFound(self.name_or_id)
            else:
                LocationCache.add_location_area(data.get('id'), data)
                LocationCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = LocationCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise LocationNotFound(self.name_or_id)
                        else:
                            LocationCache.add_location_area(data.get('id'), data)
                            LocationCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise LocationNotFound(self.name_or_id)
        data = LocationCache.location_area.get(id)
        return data

@dataclass(frozen=True)
class PalParkArea:

    """Areas used for grouping Pokémon encounters in Pal Park."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pal-park-area/{self.name_or_id}"


    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise LocationNotFound(self.name_or_id)
            else:
                LocationCache.add_pal_park_area(data.get('id'), data)
                LocationCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = LocationCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise LocationNotFound(self.name_or_id)
                        else:
                            LocationCache.add_pal_park_area(data.get('id'), data)
                            LocationCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise LocationNotFound(self.name_or_id)
        data = LocationCache.pal_park_areas.get(id)
        return data

@dataclass(frozen=True)
class Region:

    """A region is an organized area of the Pokémon world.
    Most often, the main difference
    between regions is the species
    of Pokémon that can be encountered within them."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}region/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise LocationNotFound(self.name_or_id)
            else:
                LocationCache.add_region(data.get('id'), data)
                LocationCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = LocationCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise LocationNotFound(self.name_or_id)
                        else:
                            LocationCache.add_region(data.get('id'), data)
                            LocationCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise LocationNotFound(self.name_or_id)
        data = LocationCache.regions.get(id)
        return data