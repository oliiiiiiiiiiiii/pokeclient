from typing import Dict, Any
from base import BaseParser1, BaseParser2, UtilsParser

class APIResource(UtilsParser):
    @property
    def url(self)->str:
        return self.data.get("url")

class Description(UtilsParser):
    @property
    def description(self):
        return self.data.get("description")

    @property
    def language(self):
        return Language(self.data.get("language"))

class Effect(UtilsParser):
    @property
    def language(self):
        return Language(self.data.get("language"))

    @property
    def effect(self):
        return self.data.get("effect")

class Encounter(UtilsParser):
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
        return EncounterConditionValue(self.data.get("condition_values"))

    @property
    def method(self):
        return EncounterMethod(self.data.get("method"))

class FlavorText(UtilsParser):
    @property
    def flavor_text(self):
        return self.data.get("flavor_text")

    @property
    def name(self):
        return Language(self.data.get("name"))

    @property
    def version(self):
        return Version((self.data.get("version")))

class GenerationGameIndex(UtilsParser):
    @property
    def game_index(self):
        return self.data.get("game_index")

    @property
    def generation(self):
        return Generation(self.data.get("generation"))
   

class MachineVersionDetail(UtilsParser):
    @property
    def machine(self):
        return Machine(self.data.get("machine"))

    @property
    def version_group(self):
        return VersionGroup(self.data.get("version_group"))


class Name(UtilsParser):
    @property
    def name(self):
        return self.data.get("name")

    @property
    def language(self):
        return Language(self.data.get("language"))

class Language(BaseParser1):
    @property
    def official(self):
        return self.data.get("official")

    @property
    def iso639(self):
        return self.data.get("iso639")

    @property
    def iso3166(self):
        return self.data.get("iso3166")

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]


class BerryFirmness(BaseParser1):
    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]

    @property
    def berries(self):
        return [Berry(_) for _ in self.data.get("berries")]


class FlavorBerryMap(UtilsParser):
    @property
    def potency(self):
        return self.data.get("potency")

    @property
    def berry(self):
        Berry(self.data.get("berry"))


class BerryFlavor(BaseParser1):
    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]

    @property
    def berries(self):
        return [FlavorBerryMap(_) for _ in self.data.get("berries")]

    @property
    def berries(self):
        return [ContestType(_) for _ in self.data.get("contest_type")]


class BerryFlavorMap(UtilsParser):
    @property
    def potency(self):
        return self.data.get("potency")

    @property
    def potency(self):
        return self.data.get("flavor")


class Berry(BaseParser1):
    @property
    def growth_time(self):
        return self.data.get("growth_time")

    @property
    def max_harvest(self):
        return self.data.get("max_harvest")

    @property
    def natural_gift_power(self):
        return self.data.get("natural_gift_power")

    @property
    def size(self):
        return self.data.get("size")

    @property
    def smoothness(self):
        return self.data.get("smoothness")

    @property
    def soil_dryness(self):
        return self.data.get("soil_dryness")

    @property
    def firmness(self):
        return BerryFirmness(self.data.get("firmness"))

    @property
    def item(self):
        return Item(self.data.get("item"))

    @property
    def natural_gift_type(self):
        return Item(self.data.get("natural_gift_type"))

    @property
    def flavors(self):
        return [BerryFlavorMap(_) for _ in self.data.get("flavors")]
