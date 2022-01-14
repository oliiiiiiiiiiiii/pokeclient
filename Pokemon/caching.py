from typing import Dict, Any
from abc import ABC


class CacheDict(dict):
    def __add__(self, other: Dict[Any, Any]) -> Dict[Any, Any]:
        return CacheDict({**self, **other})

    def __iadd__(self, other: Dict[Any, Any]) -> Dict[Any, Any]:
        return CacheDict({**self, **other})


class CacheBase(ABC):
    def __init__(self) -> None:
        self.name_id_map = CacheDict()
        self.cached_data = CacheDict()

    def add_new(self, field: str, other: Dict[Any, Any]):
        self.name_id_map += CacheDict({other.get("name"): other.get("id")})
        try:
            self.cached_data[other.get("id")] += CacheDict({field: other})
        except KeyError:
            self.cached_data[other.get("id")] = CacheDict({field: other})


class BerryCache(CacheBase):
    ...


class ContestCache(CacheBase):
    ...


class EncounterCache(CacheBase):
    ...


class EvolutionCache(CacheBase):
    ...


class GameCache(CacheBase):
    ...


class ItemCache(CacheBase):
    ...


class LocationCache(CacheBase):
    ...


class MachineCache(CacheBase):
    ...


class MoveCache(CacheBase):
    ...


class PokemonCache(CacheBase):
    ...
