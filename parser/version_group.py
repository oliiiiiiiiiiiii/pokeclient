from dataclasses import dataclass
from ..payload import DataPayload
from version import Version
from pokedex import Pokedex
from generation import Generation

@dataclass(frozen=True)
class VersionGroup:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def order(self):
        return self.data.get('order')

    @property
    def versions(self):
        return [Version(_) for _ in self.data.get('versions')]

    @property
    def pokedexes(self):
        return [Pokedex(_) for _ in self.data.get('pokedexes')]

    @property
    def pokedexes(self):
        return [Generation(_) for _ in self.data.get('generation')]

    @property
    def regions(self):
        return [_ for _ in self.data.get('regions')]

    @property
    def move_learn_methods(self):
        return [_ for _ in self.data.get('move_learn_methods')]