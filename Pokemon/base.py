from abc import ABC, abstractmethod
import httpx
from dataclasses import dataclass
from pydantic import BaseModel, root_validator
from typing import Any, Dict, Optional, Union

Payload = Dict[str, Any]
base_url = "https://pokeapi.co/api/v2/"


class BaseType1(BaseModel, ABC):

    id: Optional[Union[int, str]]
    name: Optional[str]
    from_cache: bool
    async_mode: bool

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
    def cache(self) -> object:
        ...

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    @property
    def url(self) -> str:
        return (
            f"{base_url}{self.address}/{self.id}"
            or f"{base_url}{self.address}{self.name}"
        )

    @property
    @abstractmethod
    def error(self) -> Exception:
        ...

    @property
    def error(self) -> Exception:
        ...

    @property
    def raw_data(self) -> Optional[Dict[str, Any]]:
        return httpx.get(self.url).json() or None

    @property
    @abstractmethod
    def parsed_data(self) -> object:
        ...

    class Config:
        allow_mutation = False


class BaseType2(BaseModel, ABC):

    id: Union[int, str]
    from_cache: bool
    async_mode: bool

    @property
    def cache(self) -> object:
        ...

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    @property
    def url(self) -> str:
        return f"{base_url}{self.address}/{self.id}"

    @property
    @abstractmethod
    def error(self) -> Exception:
        ...

    @property
    def raw_data(self) -> Optional[Dict[str, Any]]:
        return httpx.get(self.url).json() or None

    @property
    @abstractmethod
    def parsed_data(self) -> object:
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
