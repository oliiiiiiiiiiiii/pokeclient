from typing import Optional, Dict, List, Any
from dataclasses import dataclass

PokemonPayload: Dict[str, Any] = Any

@dataclass
class Stat:
    base_stat: int
    effort: int
    name: str

class Pokemon:
    def __init__(self, data: PokemonPayload):
        self.__data = data

    def __str__(self):
        return f'Pokemon( id = {self.id}, name = {self.name})'

    @property
    def name(self) -> str:
        return self.__data.get("name")

    @property
    def id(self) -> int:
        return int(self.__data.get("id"))

    @property
    def height(self) -> int:
        return int(self.__data.get("height"))

    @property
    def weight(self) -> int:
        return int(self.__data.get("weight"))

    @property
    def default(self) -> bool:
        return bool(self.__data.get("is_default"))

    @property
    def location_area_encounters(self) -> str:
        return self.__data.get("location_area_encounters") #TODO use GET method to amke http request with the url returned.

    @property
    def species(self) -> Optional[Dict[str, Any]]:
        data = self.__data.get("species")
        if not data:
            return None
        return data.get("name")

    @property
    def stats(self) -> Optional[List[Stat]]:
        if not self.__data.get("stats"):
            return None

        return [Stat(data.get("base_stat"), data.get("effort"), data.get("stat").get("name")) for data in self.__data.get("stats")]

    @property
    def types(self) -> Optional[List[str]]:
        if not self.__data.get("types"):
            return None

        return [(data.get("slot"), data.get("type").get("name")) for data in self.__data.get("types")]


    @property
    def moves(self) -> Optional[List[str]]:
        if not self.__data.get("moves"):
            return None
        return [data.get("move").get("name") for data in self.__data.get("moves")]

    @property
    def forms(self) -> Optional[List[str]]:
        if not self.__data.get("forms"):
            return None
        return [data.get("name") for data in self.__data.get("forms")]