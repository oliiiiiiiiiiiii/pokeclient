from base import BaseParser1, BaseParser2, UtilsParser

get_names = lambda data: [Name(_) for _ in data.get("names")]


class APIResource(UtilsParser):
    @property
    def url(self) -> str:
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
        get_names(self.data)


class BerryFirmness(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

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
        get_names(self.data)

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


class ContestName(UtilsParser):
    @property
    def name(self):
        return self.data.get("name")

    @property
    def color(self):
        return self.data.get("color")

    @property
    def language(self):
        return Language(self.data.get("language"))


class ContestType(BaseParser1):
    @property
    def names(self):
        return [ContestName(_) for _ in self.data.get("names")]

    @property
    def berry_flavor(self):
        return BerryFlavor(self.data.get("berry_flavor"))


class ContestEffect(BaseParser2):
    @property
    def appeal(self):
        return self.data.get("appeal")

    @property
    def jam(self):
        return self.data.get("jam")

    @property
    def effect_entries(self):
        return [_ for _ in self.data.get("effect_entries")]

    @property
    def flavor_text_entries(self):
        return [_ for _ in self.data.get("flavor_text_entries")]


class SuperContestEffect(BaseParser2):
    @property
    def appeal(self):
        return self.data.get("appeal")

    @property
    def flavor_text_entries(self):
        return [_ for _ in self.data.get("flavor_text_entries")]

    @property
    def moves(self):
        return [_ for _ in self.data.get("moves")]


class EncounterMethod(BaseParser1):
    @property
    def order(self):
        return self.data.get("order")

    @property
    def names(self):
        get_names(self.data)


class EncounterCondition(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def values(self):
        return [EncounterConditionValue(_) for _ in self.data.get("values")]


class EncounterConditionValue(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def condition(self):
        return EncounterCondition(self.data.get("condition"))


class EvolutionDetail(UtilsParser):
    @property
    def gender(self):
        return self.data.get("gender")

    @property
    def min_level(self):
        return self.data.get("min_level")

    @property
    def min_happiness(self):
        return self.data.get("min_happiness")

    @property
    def min_affection(self):
        return self.data.get("min_affection")

    @property
    def needs_overworld_rain(self):
        return self.data.get("needs_overworld_rain")

    @property
    def relative_physical_stats(self):
        return self.data.get("relative_physical_stats")

    @property
    def time_of_day(self):
        return self.data.get("time_of_day")

    @property
    def turn_upside_down(self):
        return self.data.get("turn_upside_down")

    @property
    def trigger(self):
        return [EvolutionTrigger(_) for _ in self.data.get("trigger")]

    @property
    def item(self):
        return Item(self.data.get("item"))

    @property
    def held_item(self):
        return Item(self.data.get("held_item"))

    @property
    def known_move(self):
        return self.data.get("known_move")

    @property
    def known_move_type(self):
        return self.data.get("known_move_type")

    @property
    def location(self):
        return Location(self.data.get("location"))

    @property
    def party_species(self):
        return self.data.get("party_species")

    @property
    def party_type(self):
        return self.data.get("party_type")

    @property
    def trade_species(self):
        return self.data.get("trade_species")


class ChainLink(UtilsParser):
    @property
    def is_baby(self):
        return self.data.get("is_baby")

    @property
    def evolution_details(self):
        return [EvolutionDetail(_) for _ in self.data.get("evolution_details")]

    @property
    def evolves_to(self):
        return self.data.get("evolves_to")

    @property
    def species(self):
        return self.data.get("species")


class EvolutionChain(BaseParser2):
    @property
    def chain(self):
        return ChainLink(self.data.get("chain"))


class EvolutionTrigger(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def pokemon_species(self):
        return [Name(_) for _ in self.data.get("pokemon_species")]


class PokemonEntry(UtilsParser):
    @property
    def entry_number(self):
        return self.data.get("entry_number")

    @property
    def pokemon_species(self):
        return self.data.get("pokemon_species")


class Pokedex(BaseParser1):
    @property
    def is_main_series(self):
        return self.data.get("is_main_series")

    @property
    def names(self):
        get_names(self.data)

    @property
    def region(self):
        return self.data.get("region")

    @property
    def pokemon_entries(self):
        return [PokemonEntry(_) for _ in self.data.get("pokemon_entries")]

    @property
    def descriptions(self):
        return [Description(_) for _ in self.data.get("descriptions")]

    @property
    def version_groups(self):
        return [VersionGroup(_) for _ in self.data.get("version_groups")]


class Generation(BaseParser1):
    @property
    def main_region(self):
        return self.data.get("main_region")

    @property
    def names(self):
        get_names(self.data)

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


class Version(BaseParser1):
    @property
    def name(self):
        get_names(self.data)

    @property
    def version_group(self):
        return [VersionGroup(_) for _ in self.data.get("version_group")]


class VersionGroup(BaseParser1):
    @property
    def order(self):
        return self.data.get("order")

    @property
    def versions(self):
        return [Version(_) for _ in self.data.get("versions")]

    @property
    def pokedexes(self):
        return [Pokedex(_) for _ in self.data.get("pokedexes")]

    @property
    def pokedexes(self):
        return [Generation(_) for _ in self.data.get("generation")]

    @property
    def regions(self):
        return [_ for _ in self.data.get("regions")]

    @property
    def move_learn_methods(self):
        return [_ for _ in self.data.get("move_learn_methods")]


class ItemAttribute(BaseParser1):
    @property
    def items(self):
        return [Item(_) for _ in self.data.get("items")]

    @property
    def names(self):
        get_names(self.data)

    @property
    def names(self):
        return [Description(_) for _ in self.data.get("descriptions")]


class ItemCategory(BaseParser1):
    @property
    def items(self):
        return [Item(_) for _ in self.data.get("items")]

    @property
    def names(self):
        get_names(self.data)


class ItemHolderPokemonVersionDetail(UtilsParser):
    @property
    def rarity(self):
        return self.data.get("rarity")

    @property
    def version(self):
        return Version(self.data.get("version"))


class ItemHolderPokemon(UtilsParser):
    @property
    def pokemon(self):
        return self.data.get("pokemon")

    @property
    def version_details(self):
        return ItemHolderPokemonVersionDetail(self.data.get("version_details"))


class ItemSprite(UtilsParser):
    @property
    def default(self):
        return self.data.get("default")


class Item(BaseParser1):
    @property
    def cost(self):
        return self.data.get("cost")

    @property
    def fling_power(self):
        return self.data.get("fling_power")

    @property
    def names(self):
        get_names(self.data)

    @property
    def sprites(self):
        return ItemSprite(self.data.get("sprites"))

    @property
    def baby_trigger_for(self):
        return EvolutionChain(self.data.get("baby_trigger_for"))

    @property
    def category(self):
        return ItemCategory(self.data.get("category"))

    @property
    def held_by_pokemon(self):
        return ItemHolderPokemon(self.data.get("held_by_pokemon"))

    @property
    def fling_effect(self):
        return ItemFlingEffect(self.data.get("fling_effect"))

    @property
    def attributes(self):
        return [ItemAttribute(_) for _ in self.data.get("attributes")]

    @property
    def machines(self):
        return [_ for _ in self.data.get("machines")]

    @property
    def effect_entries(self):
        return [_ for _ in self.data.get("effect_entries")]

    @property
    def flavor_text_entries(self):
        return [_ for _ in self.data.get("flavor_text_entries")]

    @property
    def game_indices(self):
        return [_ for _ in self.data.get("game_indices")]


class ItemPocket(BaseParser1):
    @property
    def categories(self):
        return [ItemCategory(_) for _ in self.data.get("categories")]

    @property
    def names(self):
        get_names(self.data)


class ItemFlingEffect(BaseParser1):
    @property
    def items(self):
        return [Item(_) for _ in self.data.get("items")]

    @property
    def effect_entries(self):
        return [_ for _ in self.data.get("effect_entries")]


class Machine(BaseParser2):
    @property
    def item(self):
        return Item(self.data.get("item"))

    @property
    def version_group(self):
        return VersionGroup(self.data.get("version_group"))

    @property
    def version_group(self):
        return VersionGroup(self.data.get("move"))


class Location(BaseParser1):
    @property
    def region(self):
        return self.data.get("region")

    @property
    def names(self):
        get_names(self.data)

    @property
    def region(self):
        return self.data.get("game_indices")

    @property
    def region(self):
        return [LocationArea(_) for _ in self.data.get("areas")]


class PokemonEncounter(UtilsParser):
    @property
    def pokemon(self):
        return self.data.get("pokemon")

    @property
    def version_details(self):
        return Version(self.data.get("version_details"))


class EncounterVersionDetails(UtilsParser):
    @property
    def encounter_method(self):
        return self.data.get("rate")

    @property
    def version(self):
        return Version(self.data.get("version"))


class EncounterMethodRate(UtilsParser):
    @property
    def encounter_method(self):
        return EncounterMethod(self.data.get("encounter_method"))

    @property
    def version_details(self):
        return EncounterMethod(self.data.get("version_details"))


class LocationArea(BaseParser1):
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
        get_names(self.data)


class Move(BaseParser1):
    @property
    def accuracy(self):
        return self.data.get("accuracy")

    @property
    def effect_chance(self):
        return self.data.get("effect_chance")

    @property
    def pp(self):
        return self.data.get("pp")

    @property
    def priority(self):
        return self.data.get("priority")

    @property
    def power(self):
        return self.data.get("power")

    @property
    def contest_combos(self):
        return self.data.get("contest_combos")

    @property
    def contest_type(self):
        return self.data.get("contest_type")

    @property
    def contest_effect(self):
        return self.data.get("contest_effect")

    @property
    def damage_class(self):
        return self.data.get("damage_class")

    @property
    def effect_entries(self):
        return self.data.get("effect_entries")

    @property
    def effect_changes(self):
        return self.data.get("effect_changes")

    @property
    def learned_by_pokemon(self):
        return self.data.get("learned_by_pokemon")

    @property
    def flavor_text_entries(self):
        return self.data.get("flavor_text_entries")

    @property
    def generation(self):
        return self.data.get("generation")

    @property
    def machines(self):
        return self.data.get("machines")

    @property
    def meta(self):
        return self.data.get("meta")

    @property
    def names(self):
        get_names(self.data)

    @property
    def past_values(self):
        return self.data.get("past_values")

    @property
    def stat_changes(self):
        return self.data.get("stat_changes")

    @property
    def super_contest_effect(self):
        return self.data.get("super_contest_effect")

    @property
    def target(self):
        return self.data.get("target")

    @property
    def type(self):
        return self.data.get("type")


class ContestComboSets(UtilsParser):
    @property
    def normal(self):
        return self.data.get("normal")

    @property
    def super(self):
        return self.data.get("super")


class ContestComboDetail(UtilsParser):
    @property
    def use_before(self):
        return self.data.get("use_before")

    @property
    def use_after(self):
        return self.data.get("use_after")


class MoveFlavorText(UtilsParser):
    @property
    def flavor_text(self):
        return self.data.get("flavor_text")

    @property
    def language(self):
        return self.data.get("language")

    @property
    def version_group(self):
        return self.data.get("version_group")


class MoveMetaData(UtilsParser):
    @property
    def ailment(self):
        return self.data.get("ailment")

    @property
    def category(self):
        return self.data.get("category")

    @property
    def min_hits(self):
        return self.data.get("min_hits")

    @property
    def max_hits(self):
        return self.data.get("max_hits")

    @property
    def min_turns(self):
        return self.data.get("min_turns")

    @property
    def max_turns(self):
        return self.data.get("max_turns")

    @property
    def drain(self):
        return self.data.get("drain")

    @property
    def healing(self):
        return self.data.get("healing")

    @property
    def crit_rate(self):
        return self.data.get("crit_rate")

    @property
    def ailment_chance(self):
        return self.data.get("ailment_chance")

    @property
    def flinch_chance(self):
        return self.data.get("flinch_chance")

    @property
    def stat_chance(self):
        return self.data.get("stat_chance")


class MoveStatChange(UtilsParser):
    @property
    def change(self):
        return self.data.get("change")

    @property
    def stat(self):
        return self.data.get("stat")


class MoveMetaData(UtilsParser):
    @property
    def accuracy(self):
        return self.data.get("accuracy")

    @property
    def effect_chance(self):
        return self.data.get("effect_chance")

    @property
    def power(self):
        return self.data.get("power")

    @property
    def pp(self):
        return self.data.get("pp")

    @property
    def effect_entries(self):
        return self.data.get("effect_entries")

    @property
    def type(self):
        return self.data.get("type")

    @property
    def version_group(self):
        return self.data.get("version_group")
