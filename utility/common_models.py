from dataclasses import dataclass
from languages import Language
from ..payload import DataPayload
from ..parser import encounter_method,encounter_condition_value,version,generation,version_group,machine

@dataclass
class APIResource:

    data:DataPayload

    @property
    def url(self):
        return self.data.get("url")

@dataclass
class Description:

    data:DataPayload

    @property
    def description(self):
        return self.data.get("description")

    @property
    def language(self):
        return Language(self.data.get("language"))

@dataclass
class Effect:
    data:DataPayload

    @property
    def language(self):
        return Language(self.data.get("language"))

    @property
    def effect(self):
        return self.data.get("effect")

@dataclass
class Encounter:
    data:DataPayload

    @property
    def chance(self):
        return self.data.get("chance")

    @property
    def max_level(self):
        return self.data.get("max_level")

    @property
    def max_level(self):
        return self.data.get("min_level")

    @property
    def condition_values(self):
        return encounter_condition_value.EncounterConditionValue(self.data.get("condition_values"))

    @property
    def method(self):
        return encounter_method.EncounterMethod(self.data.get("method"))

@dataclass
class FlavorText:
    data:DataPayload

    @property
    def flavor_text(self):
        return self.data.get("flavor_text")

    @property
    def name(self):
        return Language(self.data.get("name"))

    @property
    def version(self):
        return version.Version((self.data.get("version")))

@dataclass
class GenerationGameIndex:
    data:DataPayload

    @property
    def game_index(self):
        return self.data.get("game_index")

    @property
    def generation(self):
        return generation.Generation(self.data.get("generation"))
   

@dataclass
class MachineVersionDetail:
    data:DataPayload

    @property
    def machine(self):
        return machine.Machine(self.data.get("machine"))

    @property
    def version_group(self):
        return version_group.VersionGroup(self.data.get("version_group"))


@dataclass
class Name:
    data:DataPayload

    @property
    def name(self):
        return self.data.get("name")

    @property
    def language(self):
        return Language(self.data.get("language"))