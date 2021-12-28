from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Name
from encounter_method import EncounterMethod
from version import Version
from location import Location

@dataclass(frozen=True)
class PokemonEncounter:

    data:DataPayload

    @property
    def pokemon(self):
        return self.data.get("pokemon")

    @property
    def version_details(self):
        return Version(self.data.get("version_details"))

@dataclass(frozen=True)
class EncounterVersionDetails:

    data:DataPayload

    @property
    def encounter_method(self):
        return self.data.get("rate")

    @property
    def version(self):
        return Version(self.data.get("version"))


@dataclass(frozen=True)
class EncounterMethodRate:

    data:DataPayload

    @property
    def encounter_method(self):
        return EncounterMethod(self.data.get("encounter_method"))

    @property
    def version_details(self):
        return EncounterMethod(self.data.get("version_details"))


@dataclass(frozen=True)
class LocationArea:

    data:DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def game_index(self):
        return self.data.get("game_index")

    @property
    def location(self):
        return Location(self.data.get("location"))

    @property
    def pokemon_encounters(self):
        return [PokemonEncounter(_) for _ in self.data.get("pokemon_encounters")]

    @property
    def encounter_method_rates(self):
        return [EncounterMethodRate(_) for _ in self.data.get("encounter_method_rates")]

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]