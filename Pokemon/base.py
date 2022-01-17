from Pokemon.caching import CacheDict
import abc
import dataclasses
import typing
import httpx
import pydantic
import json

Payload = typing.Dict[str, typing.Any]
base_url = "https://pokeapi.co/api/v2/"


class BaseType1(pydantic.BaseModel, abc.ABC):

    id: typing.Optional[typing.Union[int, str]]
    name: typing.Optional[str]
    async_mode: typing.Optional[bool] = False

    @pydantic.root_validator(pre=True)
    @classmethod
    def id_or_name(
        cls, vals: typing.Dict[str, typing.Any]
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """Checks if either of name or id is
        passed returns error if none of
        them is passed or both are passed"""

        if "id" not in vals and "name" not in vals:
            raise TypeError("Missing Arguments : name or id")
        elif "id" in vals and "name" in vals:
            raise TypeError("Too many Arguments provided : name and id")
        return vals

    @property
    @abc.abstractmethod
    def cache(self) -> object:
        ...

    @property
    @abc.abstractmethod
    def address(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def error(self) -> Exception:
        ...

    @property
    def url(self) -> str:
        return f"{base_url}{self.address}/{self.id or self.name}"

    @property
    def raw_data(self) -> CacheDict[int, CacheDict[str, typing.Any]]:
        id_or_name = self.id or self.name
        id_and_name_list = [i for h in self.cache.name_id_map.items() for i in h]
        if not id_or_name in id_and_name_list:
            try:
                response = CacheDict(httpx.get(self.url).json())
                self.cache.add_new(self.address, response)
            except json.JSONDecodeError:
                raise self.error(arg=id_or_name)
            else:
                return response
        if not self.id:
            return self.cache.cached_data[self.cache.name_id_map.get(self.name)][
                self.address
            ]
        return self.cache.cached_data[self.id][self.address]

    class Config:
        allow_mutation = False


class BaseType2(pydantic.BaseModel, abc.ABC):

    id: typing.Union[int, str]
    async_mode: typing.Optional[bool] = False

    @property
    @abc.abstractmethod
    def cache(self) -> object:
        ...

    @property
    @abc.abstractmethod
    def address(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def error(self) -> Exception:
        ...

    @property
    def url(self) -> str:
        return f"{base_url}{self.address}/{self.id}"

    @property
    def raw_data(self) -> CacheDict[int, CacheDict[str, typing.Any]]:
        if not id in self.cache.cached_data:
            try:
                response = CacheDict(httpx.get(self.url).json())
                self.cache.add_new(self.address, response)
            except json.JSONDecodeError:
                raise self.error(arg=self.id)
            else:
                return response
        return self.cache.cached_data[self.id][self.address]

        ...

    class Config:
        allow_mutation = False


@dataclasses.dataclass(frozen=True)
class UtilsParser(abc.ABC):
    data: Payload


@dataclasses.dataclass(frozen=True)
class BaseParser1(UtilsParser):
    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")


@dataclasses.dataclass(frozen=True)
class BaseParser2(UtilsParser):
    @property
    def id(self):
        return self.data.get("id")
