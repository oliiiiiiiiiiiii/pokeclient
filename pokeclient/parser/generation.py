from dataclasses import dataclass
from ..payload import DataPayload
from version_group import VersionGroup

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

    @property
    def version_groups(self):
        return [VersionGroup(_) for _ in self.data.get("version_groups")]

'''
TODO:
abilities
main_region
moves
pokemon_species
types
'''