import json
import httpx
from .pokemon import Pokemon
from typing import Union, Optional
from .errors import PokeNotFound

class PokeClient:  

    base_url = 'https://pokeapi.co/api/v2/'

    def fetch_pokemon_with_id(self, number: Union[str, int]) -> Optional[Pokemon]:
        try:
            data = httpx.get(f"{self.base_url}pokemon/{str(number)}").json()
            return Pokemon(data)
        except json.decoder.JSONDecodeError:
            raise PokeNotFound

    def fetch_pokemon_with_name(self, name: str)-> Optional[Pokemon]:
        try:
            data = httpx.get(f"{self.base_url}pokemon/{str(name)}").json()
            return Pokemon(data)
        except json.decoder.JSONDecodeError:
            raise PokeNotFound
