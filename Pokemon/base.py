from abc import ABC, abstractmethod
import httpx
from pydantic import BaseModel, root_validator
from typing import Any, Dict, Optional, Union
from errors import (
    BerryNotFound,
    ContestNotFound,
    EncounterNotFound,
    EvolutionNotFound,
    GameNotFound,
    ItemNotFound,
    LocationNotFound,
    MachineNotFound,
    MoveNotFound,
    PokemonNotFound,
)

base_url = "https://pokeapi.co/api/v2/"


class BaseType1(BaseModel, ABC):

    id: Optional[Union[int, str]]
    name: Optional[str]
    from_cache: bool

    @root_validator(pre=True)
    @classmethod
    def check_id_or_name(cls, values: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Checks if either of name or id is passed returns error if none of them is passed or both are passed"""
        if "id" not in values and "name" not in values:
            raise TypeError("Missing Arguments : name or id")
        elif "id" in values and "name" in values:
            raise TypeError("Too many Arguments provided : name and id")
        return values

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    @property
    def url(self) -> str:
        return (
            f"{base_url}{self.address}{self.id}"
            or f"{base_url}{self.address}{self.name}"
        )

    @property
    def raw_data(self) -> Dict[str, Any]:
        return httpx.get(self.url).json()

    @property
    @abstractmethod
    def parsed_data(self) -> object:
        ...

    class Config:
        allow_mutation = False


class BaseType2(BaseModel, ABC):

    id: Union[int, str]
    from_cache: bool

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    @property
    def url(self) -> str:
        return f"{base_url}{self.address}{self.id}"

    @property
    def raw_data(self) -> Dict[str, Any]:
        return httpx.get(self.url).json()

    @property
    @abstractmethod
    def parsed_data(self) -> object:
        ...

    class Config:
        allow_mutation = False
