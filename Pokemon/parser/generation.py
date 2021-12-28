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
    def main_region(self):
        return self.data.get("main_region")

    @property
    def names(self):
        return self.data.get("names")

    @property
    def version_groups(self):
        return [VersionGroup(_) for _ in self.data.get("version_groups")]

    @property
    def abilities(self):
        return [_ for _ in self.data.get("abilities")]

    @property
    def types(self):
        return [_ for _ in self.data.get("types")]

    @property
    def moves(self):
        return [_ for _ in self.data.get("moves")]

    @property
    def pokemon_species(self):
        return [_ for _ in self.data.get("pokemon_species")]