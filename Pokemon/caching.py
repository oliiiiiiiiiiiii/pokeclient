import typing
import abc


class CacheDict(dict):
    def __add__(
        self, other: typing.Dict[typing.Any, typing.Any]
    ) -> typing.Dict[typing.Any, typing.Any]:
        return CacheDict({**self, **other})

    def __iadd__(
        self, other: typing.Dict[typing.Any, typing.Any]
    ) -> typing.Dict[typing.Any, typing.Any]:
        return CacheDict({**self, **other})


class CacheBase(abc.ABC):
    def __init__(self) -> None:
        self.name_id_map = CacheDict()
        self.cached_data = CacheDict()

    def add_new(self, field: str, other: typing.Dict[typing.Any, typing.Any]):
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
