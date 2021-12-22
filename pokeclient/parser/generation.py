from dataclasses import dataclass
from payload import DataPayload

@dataclass(frozen=True)
class Generation:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def names(self):
        return self.data.get("names")

'''
TODO:
abilities
main_region
moves
pokemon_species
types
version_groups
'''