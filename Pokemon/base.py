from abc import ABC, abstractmethod
from pydantic import BaseModel, root_validator
from typing import Any, Dict, Optional, Union

base_url = "https://pokeapi.co/api/v2/"


class Base(BaseModel, ABC):

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
            raise TypeError("Two many Arguments provided : name and id")
        return values

    @property
    def url(self) -> None:...

    @url.getter
    @abstractmethod
    def url(self) -> None:...

    @property
    def raw_data(self) -> None:...

    @raw_data.getter
    @abstractmethod
    def raw_data(self) -> None:...

    @property
    def parsed_data(self) -> None:...

    @parsed_data.getter
    @abstractmethod
    def parsed_data(self) -> None:...

    class Config:
        allow_mutation = False


class Base2(BaseModel, ABC):

    id: Optional[Union[int, str]]
    from_cache: bool

    @root_validator(pre=True)
    @classmethod
    def check_id_or_name(cls, values: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Check if id is passed raises TypeError if id is not passed"""
        if "id" not in values:
            raise TypeError("Missing Argument : id")
        return values

    @property
    def url(self) -> None:...

    @url.getter
    @abstractmethod
    def url(self) -> None:...

    @property
    def raw_data(self) -> None:...

    @raw_data.getter
    @abstractmethod
    def raw_data(self) -> None:...

    @property
    def parsed_data(self) -> None:...

    @parsed_data.getter
    @abstractmethod
    def parsed_data(self) -> None:...

    class Config:
        allow_mutation = False
