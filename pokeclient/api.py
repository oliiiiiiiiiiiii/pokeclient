import json
import httpx
from .pokemon import Pokemon
from typing import Union, Optional
from .errors import PokeNotFound
import random


class PokeClient:

    base_url = 'https://pokeapi.co/api/v2/'

    def fetch_pokemon(self, poke: Union[str, int]) -> Optional[Pokemon]:
        try:
            if isinstance(poke, str):
                try:
                    address = int(poke)
                except ValueError:
                    address = poke.lower()
            else:
                address = str(poke)
            data = httpx.get(f"{self.base_url}pokemon/{address}").json()
            return Pokemon(data)
        except json.decoder.JSONDecodeError:
            raise PokeNotFound

    def can_move(self, poke: Union[str, int], move: str) -> Optional[bool]:
        data = self.fetch_pokemon(poke)
        return move.lower() in data.moves

    def random_pokemon(self) -> Optional[Pokemon]:
        data = [
            httpx.get(f"{self.base_url}pokemon?limit=1118").json().get(
                'results')[_].get('name') for _ in range(1118)
        ]
        return self.fetch_pokemon(random.choice(data))
