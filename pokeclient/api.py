import json
import httpx
from .pokemon import Pokemon
from typing import Union, Optional
from .errors import PokeNotFound


class PokeClient:

    base_url = 'https://pokeapi.co/api/v2/'

    def fetch_pokemon(self, poke: Union[str, int]) -> Optional[Pokemon]:
        try:
            if isinstance(poke, int):
                address = str(poke)
            else:
                try:
                    address = int(poke)
                except ValueError:
                    address = poke.lower()
            data = httpx.get(f"{PokeClient.base_url}pokemon/{address}").json()
            return Pokemon(data)
        except json.decoder.JSONDecodeError:
            raise PokeNotFound

    def can_move(self, poke: Union[str, int], move: str) -> Optional[bool]:
        try:
            if isinstance(poke, int):
                address = str(poke)
            else:
                try:
                    address = int(poke)
                except ValueError:
                    address = poke.lower()
            data = httpx.get(f"{PokeClient.base_url}pokemon/{address}").json()
            return move.lower() in Pokemon(data).moves
        except json.decoder.JSONDecodeError:
            raise PokeNotFound
