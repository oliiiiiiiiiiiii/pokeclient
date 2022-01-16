from abc import ABC, abstractmethod
import httpx
from dataclasses import dataclass
from pydantic import BaseModel, root_validator
from typing import Any, Dict, Optional, Union
from Pokemon.caching import CacheDict
import json

Payload = Dict[str, Any]
base_url = "https://pokeapi.co/api/v2/"


class BaseType1(BaseModel, ABC):

    id: Optional[Union[int, str]]
    name: Optional[str]
    from_cache: Optional[bool]
    async_mode: Optional[bool]

    @root_validator(pre=True)
    @classmethod
    def id_or_name(cls, vals: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Checks if either of name or id is
        passed returns error if none of
        them is passed or both are passed"""

        if "id" not in vals and "name" not in vals:
            raise TypeError("Missing Arguments : name or id")
        elif "id" in vals and "name" in vals:
            raise TypeError("Too many Arguments provided : name and id")
        return vals

    @property
    @abstractmethod
    def cache(self) -> object:
        ...

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    @property
    @abstractmethod
    def error(self) -> Exception:
        ...

    @property
    def url(self) -> str:
        return (
            f"{base_url}{self.address}/{self.id or self.name}"
        )

    @property
    def raw_data(self) -> CacheDict[int,CacheDict[str,Any]]:
        id_or_name = self.id or self.name
        id_and_name_list  = [i for h in self.cache.name_id_map.items() for i in h]
        print(id_and_name_list)
        if not id_or_name in id_and_name_list:
            try:
                response = CacheDict(httpx.get(self.url).json())
                self.cache.add_new(self.address,response)
            except json.JSONDecodeError:
                raise self.error(arg=id_or_name)
            else:
                return response
        #if not 
        #id = self.cache.name_id_map[self.name]
        #response = self.cache.cached_data[]

    class Config:
        allow_mutation = False


class BaseType2(BaseModel, ABC):

    id: Union[int, str]
    async_mode: Optional[bool]

    @property
    @abstractmethod
    def cache(self) -> object:
        ...

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    @property
    @abstractmethod
    def error(self) -> Exception:
        ...

    @property
    def url(self) -> str:
        return f"{base_url}{self.address}/{self.id}"

    @property
    def raw_data(self) -> CacheDict[int,CacheDict[str,Any]]:
        if not id in self.cache.cached_data:
            try:
                response = CacheDict(httpx.get(self.url).json())
                self.cache.add_new(self.address,response)
            except json.JSONDecodeError:
                raise self.error(arg=self.id)
            else:
                return response
        return self.cache.cached_data[self.id][self.address]

        ...

    class Config:
        allow_mutation = False


@dataclass(frozen=True)
class BaseParser1(ABC):
    data: Payload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")


@dataclass(frozen=True)
class BaseParser2(ABC):
    data: Payload

    @property
    def id(self):
        return self.data.get("id")


@dataclass(frozen=True)
class UtilsParser(ABC):
    data: Payload
