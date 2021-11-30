import dataclasses
import httpx

@dataclasses.dataclass
class pokemon:

    def __init__(self,pokemon_name):
        self.pokemon_name = pokemon_name
        self._id = None
        self._types = None
        self._moves = None
