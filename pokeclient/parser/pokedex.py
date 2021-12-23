from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Description
from version_group import VersionGroup

@dataclass(frozen=True)
class PokemonEntry:

    data : DataPayload

    @property
    def entry_number(self):
        return self.data.get("entry_number")

    '''
    TODO:
    pokemon_species
    '''


@dataclass(frozen=True)
class Pokedex:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def is_main_series(self):
        return self.data.get("is_main_series")

    @property
    def names(self):
        return self.data.get("names")

    @property
    def pokemon_entries(self):
        return [PokemonEntry(_) for _ in self.data.get("pokemon_entries")]

    @property
    def descriptions(self):
        return [Description(_) for _ in self.data.get("descriptions")]

    @property
    def version_groups(self):
        return [VersionGroup(_) for _ in self.data.get("version_groups")]

    '''
    TODO:
    region
    '''