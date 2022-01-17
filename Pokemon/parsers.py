from Pokemon.base import BaseParser1, BaseParser2, UtilsParser

get_names = lambda data: [NameParser(_) for _ in data.get("names")]


class APIResourceParser(UtilsParser):
    @property
    def url(self) -> str:
        return self.data.get("url")


class DescriptionParser(UtilsParser):
    @property
    def descriptionParserDescriptionParser(self):
        return self.data.get("description")

    @property
    def language(self):
        return LanguageParser(self.data.get("language"))


class EffectParser(UtilsParser):
    @property
    def language(self):
        return LanguageParser(self.data.get("language"))

    @property
    def effect(self):
        return self.data.get("effect")


class EncounterParser(UtilsParser):
    @property
    def chance(self):
        return self.data.get("chance")

    @property
    def max_level(self):
        return self.data.get("max_level")

    @property
    def min_level(self):
        return self.data.get("min_level")

    @property
    def condition_values(self):
        return EncounterConditionValueParser(self.data.get("condition_values"))

    @property
    def method(self):
        return EncounterMethodParser(self.data.get("method"))


class FlavorTextParser(UtilsParser):
    @property
    def flavor_text(self):
        return self.data.get("flavor_text")

    @property
    def name(self):
        return LanguageParser(self.data.get("name"))

    @property
    def version(self):
        return VersionParser((self.data.get("version")))


class GenerationGameIndexParser(UtilsParser):
    @property
    def game_index(self):
        return self.data.get("game_index")

    @property
    def generation(self):
        return GenerationParser(self.data.get("generation"))


class MachineVersionDetailParser(UtilsParser):
    @property
    def machine(self):
        return Machine(self.data.get("machine"))

    @property
    def version_group(self):
        return VersionGroupParser(self.data.get("version_group"))


class NameParser(UtilsParser):
    @property
    def name(self):
        return self.data.get("name")

    @property
    def language(self):
        return LanguageParser(self.data.get("language"))


class LanguageParser(BaseParser1):
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


class BerryFirmnessParser(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def berries(self):
        return [BerryParser(_) for _ in self.data.get("berries")]


class FlavorBerryMapParser(UtilsParser):
    @property
    def potency(self):
        return self.data.get("potency")

    @property
    def berry(self):
        BerryParser(self.data.get("berry"))


class BerryFlavorParser(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def berries(self):
        return [FlavorBerryMapParser(_) for _ in self.data.get("berries")]

    @property
    def berries(self):
        return [ContestTypeParser(_) for _ in self.data.get("contest_type")]


class BerryFlavorMapParser(UtilsParser):
    @property
    def potency(self):
        return self.data.get("potency")

    @property
    def flavor(self):
        return self.data.get("flavor")


class BerryParser(BaseParser1):
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
        return BerryFirmnessParser(self.data.get("firmness"))

    @property
    def ItemParser(self):
        return ItemParser(self.data.get("item"))

    @property
    def natural_gift_type(self):
        return ItemParser(self.data.get("natural_gift_type"))

    @property
    def flavors(self):
        return [BerryFlavorMapParser(_) for _ in self.data.get("flavors")]


class ContestNameParser(UtilsParser):
    @property
    def name(self):
        return self.data.get("name")

    @property
    def color(self):
        return self.data.get("color")

    @property
    def language(self):
        return LanguageParser(self.data.get("language"))


class ContestTypeParser(BaseParser1):
    @property
    def names(self):
        return [ContestNameParser(_) for _ in self.data.get("names")]

    @property
    def berry_flavor(self):
        return BerryFlavorParser(self.data.get("berry_flavor"))


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


class EncounterMethodParser(BaseParser1):
    @property
    def order(self):
        return self.data.get("order")

    @property
    def names(self):
        get_names(self.data)


class EncounterConditionParser(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def values(self):
        return [EncounterConditionValueParser(_) for _ in self.data.get("values")]


class EncounterConditionValueParser(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def condition(self):
        return EncounterConditionParser(self.data.get("condition"))


class EvolutionDetailParser(UtilsParser):
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
        return [EvolutionTriggerParser(_) for _ in self.data.get("trigger")]

    @property
    def item(self):
        return ItemParser(self.data.get("item"))

    @property
    def held_item(self):
        return ItemParser(self.data.get("held_item"))

    @property
    def known_move(self):
        return self.data.get("known_move")

    @property
    def known_move_type(self):
        return self.data.get("known_move_type")

    @property
    def locationParser(self):
        return LocationParser(self.data.get("location"))

    @property
    def party_species(self):
        return self.data.get("party_species")

    @property
    def party_type(self):
        return self.data.get("party_type")

    @property
    def trade_species(self):
        return self.data.get("trade_species")


class ChainLinkParser(UtilsParser):
    @property
    def is_baby(self):
        return self.data.get("is_baby")

    @property
    def evolution_details(self):
        return [EvolutionDetailParser(_) for _ in self.data.get("evolution_details")]

    @property
    def evolves_to(self):
        return self.data.get("evolves_to")

    @property
    def species(self):
        return self.data.get("species")


class EvolutionChain(BaseParser2):
    @property
    def chain(self):
        return ChainLinkParser(self.data.get("chain"))


class EvolutionTriggerParser(BaseParser1):
    @property
    def names(self):
        get_names(self.data)

    @property
    def pokemon_species(self):
        return [NameParser(_) for _ in self.data.get("pokemon_species")]


class PokemonEntryParser(UtilsParser):
    @property
    def entry_number(self):
        return self.data.get("entry_number")

    @property
    def pokemon_species(self):
        return self.data.get("pokemon_species")


class PokedexParser(BaseParser1):
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
        return [PokemonEntryParser(_) for _ in self.data.get("pokemon_entries")]

    @property
    def descriptions(self):
        return [DescriptionParser(_) for _ in self.data.get("descriptions")]

    @property
    def version_groups(self):
        return [VersionGroupParser(_) for _ in self.data.get("version_groups")]


class GenerationParser(BaseParser1):
    @property
    def main_region(self):
        return self.data.get("main_region")

    @property
    def names(self):
        get_names(self.data)

    @property
    def version_groups(self):
        return [VersionGroupParser(_) for _ in self.data.get("version_groups")]

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


class VersionParser(BaseParser1):
    @property
    def name(self):
        get_names(self.data)

    @property
    def version_group(self):
        return [VersionGroupParser(_) for _ in self.data.get("version_group")]


class VersionGroupParser(BaseParser1):
    @property
    def order(self):
        return self.data.get("order")

    @property
    def versions(self):
        return [VersionParser(_) for _ in self.data.get("versions")]

    @property
    def pokedexes(self):
        return [PokedexParser(_) for _ in self.data.get("pokedexes")]

    @property
    def pokedexes(self):
        return [GenerationParser(_) for _ in self.data.get("generation")]

    @property
    def regions(self):
        return [_ for _ in self.data.get("regions")]

    @property
    def move_learn_methods(self):
        return [_ for _ in self.data.get("move_learn_methods")]


class ItemAttributeParser(BaseParser1):
    @property
    def items(self):
        return [ItemParser(_) for _ in self.data.get("items")]

    @property
    def names(self):
        get_names(self.data)

    @property
    def names(self):
        return [DescriptionParser(_) for _ in self.data.get("descriptions")]


class ItemCategoryParser(BaseParser1):
    @property
    def items(self):
        return [ItemParser(_) for _ in self.data.get("items")]

    @property
    def names(self):
        get_names(self.data)


class ItemHolderPokemonVersionDetailParser(UtilsParser):
    @property
    def rarity(self):
        return self.data.get("rarity")

    @property
    def versionParser(self):
        return VersionParser(self.data.get("version"))


class ItemHolderPokemonParser(UtilsParser):
    @property
    def pokemon(self):
        return self.data.get("pokemon")

    @property
    def version_details(self):
        return ItemHolderPokemonVersionDetailParser(self.data.get("version_details"))


class ItemSpriteParser(UtilsParser):
    @property
    def default(self):
        return self.data.get("default")


class ItemParser(BaseParser1):
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
        return ItemSpriteParser(self.data.get("sprites"))

    @property
    def baby_trigger_for(self):
        return EvolutionChain(self.data.get("baby_trigger_for"))

    @property
    def category(self):
        return ItemCategoryParser(self.data.get("category"))

    @property
    def held_by_pokemon(self):
        return ItemHolderPokemonParser(self.data.get("held_by_pokemon"))

    @property
    def fling_effect(self):
        return ItemFlingEffectParser(self.data.get("fling_effect"))

    @property
    def attributes(self):
        return [ItemAttributeParser(_) for _ in self.data.get("attributes")]

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


class ItemPocketParser(BaseParser1):
    @property
    def categories(self):
        return [ItemCategoryParser(_) for _ in self.data.get("categories")]

    @property
    def names(self):
        get_names(self.data)


class ItemFlingEffectParser(BaseParser1):
    @property
    def items(self):
        return [ItemParser(_) for _ in self.data.get("items")]

    @property
    def effect_entries(self):
        return [_ for _ in self.data.get("effect_entries")]


class Machine(BaseParser2):
    @property
    def ItemParser(self):
        return ItemParser(self.data.get("item"))

    @property
    def version_group(self):
        return VersionGroupParser(self.data.get("version_group"))

    @property
    def version_group(self):
        return VersionGroupParser(self.data.get("move"))


class LocationParser(BaseParser1):
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
        return [LocationAreaParser(_) for _ in self.data.get("areas")]


class PokemonEncounterParser(UtilsParser):
    @property
    def pokemon(self):
        return self.data.get("pokemon")

    @property
    def version_details(self):
        return VersionParser(self.data.get("version_details"))


class EncounterVersionDetailsParser(UtilsParser):
    @property
    def encounter_method(self):
        return self.data.get("rate")

    @property
    def versionParser(self):
        return VersionParser(self.data.get("version"))


class EncounterMethodRateParser(UtilsParser):
    @property
    def encounter_method(self):
        return EncounterMethodParser(self.data.get("encounter_method"))

    @property
    def version_details(self):
        return EncounterMethodParser(self.data.get("version_details"))


class LocationAreaParser(BaseParser1):
    @property
    def game_index(self):
        return self.data.get("game_index")

    @property
    def location(self):
        return LocationParser(self.data.get("location"))

    @property
    def pokemon_encounters(self):
        return [PokemonEncounterParser(_) for _ in self.data.get("pokemon_encounters")]

    @property
    def encounter_method_rates(self):
        return [EncounterMethodRateParser(_) for _ in self.data.get("encounter_method_rates")]

    @property
    def names(self):
        get_names(self.data)


class MoveParser(BaseParser1):
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
    def generationParser(self):
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


class ContestComboSetsParser(UtilsParser):
    @property
    def normal(self):
        return self.data.get("normal")

    @property
    def super(self):
        return self.data.get("super")


class ContestComboDetailParser(UtilsParser):
    @property
    def use_before(self):
        return self.data.get("use_before")

    @property
    def use_after(self):
        return self.data.get("use_after")


class MoveFlavorTextParser(UtilsParser):
    @property
    def flavor_text(self):
        return self.data.get("flavor_text")

    @property
    def language(self):
        return self.data.get("language")

    @property
    def version_group(self):
        return self.data.get("version_group")


class MoveMetaDataParser(UtilsParser):
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


class MoveStatChangeParser(UtilsParser):
    @property
    def change(self):
        return self.data.get("change")

    @property
    def stat(self):
        return self.data.get("stat")


class MoveMetaDataParser(UtilsParser):
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


class MoveAilmentParser(BaseParser1):
    @property
    def moves(self):
        return self.data.get("moves")

    @property
    def names(self):
        get_names(self.data)


class MoveBattleStyleParser(BaseParser1):
    @property
    def names(self):
        get_names(self.data)


class MoveCategoryParser(BaseParser1):
    @property
    def moves(self):
        return self.data.get("moves")

    @property
    def descriptions(self):
        return self.data.get("descriptions")


class MoveLearnMethodParser(BaseParser1):
    @property
    def version_groups(self):
        return self.data.get("version_groups")

    @property
    def names(self):
        get_names(self.data)

    @property
    def moves(self):
        return self.data.get("descriptions")


class MoveTargetParser(BaseParser1):
    @property
    def moves(self):
        return self.data.get("moves")

    @property
    def names(self):
        get_names(self.data)

    @property
    def descriptions(self):
        return self.data.get("descriptions")
