from dataclasses import dataclass

@dataclass
class CacheManager:
    name_to_id_dict = dict()


@dataclass
class Berries(CacheManager):
    berry_firmness = dict()
    berry_flavor = dict()
    berries = dict()

    def add_berry_firmness(self, id, data: dict):
        self.berry_firmness[id] = data

    def add_berry_flavour(self, id, data: dict):
        self.berry_flavour[id] = data

    def add_berry(self, id, data: dict):
        self.berry_flavour[id] = data


@dataclass
class Contests(CacheManager):
    contest_types = dict()
    contest_effects = dict()
    super_contest_effects = dict()

    def add_contest_type(self, id, data: dict):
        self.contest_types[id] = data

    def add_contest_effect(self, id, data: dict):
        self.contest_effects[id] = data

    def add_super_contest_effect(self, id, data: dict):
        self.super_contest_effects[id] = data


@dataclass
class Encounters(CacheManager):
    encounter_methods = dict()
    encounter_conditions = dict()
    encounter_condition_values = dict()

    def add_encounter_method(self, id, data: dict):
        self.encounter_methods[id] = data

    def add_encounter_condition(self, id, data: dict):
        self.encounter_conditions[id] = data

    def add_encounter_condition_value(self, id, data: dict):
        self.encounter_condition_values[id] = data


@dataclass
class Evolutions(CacheManager):
    evolution_chains = dict()
    encounter_triggers = dict()

    def add_evolution_chains(self, id, data: dict):
        self.evolution_chains[id] = data

    def add_encounter_triggers(self, id, data: dict):
        self.encounter_triggers[id] = data


@dataclass
class Games(CacheManager):
    generations = dict()
    versions = dict()
    version_groups = dict()

    def add_generation(self, id, data: dict):
        self.generations[id] = data

    def add_version(self, id, data: dict):
        self.versions[id] = data

    def add_version_group(self, id, data: dict):
        self.version_groups[id] = data


@dataclass
class Items(CacheManager):
    item_attributes = dict()
    item_categories = dict()
    item_fling_effects = dict()
    item_pockets = dict()
    items = dict()

    def add_item_attribute(self, id, data: dict):
        self.item_attributes[id] = data

    def add_item_category(self, id, data: dict):
        self.item_categories[id] = data

    def add_item_fling_effect(self, id, data: dict):
        self.item_fling_effects[id] = data

    def add_item_pocket(self, id, data: dict):
        self.item_pockets[id] = data

@dataclass
class Locations(CacheManager):
    locations = dict()
    location_areas = dict()
    pal_park_areas = dict()
    regions = dict()

    def add_location(self, id, data: dict):
        self.locations[id] = data

    def add_location_area(self, id, data: dict):
        self.location_areas[id] = data

    def add_pal_park_area(self, id, data: dict):
        self.pal_park_areas[id] = data

    def add_region(self, id, data: dict):
        self.regions[id] = data


@dataclass
class Machines(CacheManager):
    machines = dict()

    def add_machine(self, id, data: dict):
        self.machines[id] = data


@dataclass
class Moves(CacheManager):
    moves = dict()
    move_ailments = dict()
    move_battle_styles = dict()
    move_categories = dict()
    move_damage_classes = dict()
    move_learn_methods = dict()
    move_targets = dict()

    def add_move(self, id, data: dict):
        self.moves[id] = data

    def add_move_ailment(self, id, data: dict):
        self.move_ailments[id] = data

    def add_battle_style(self, id, data: dict):
        self.move_battle_styles[id] = data

    def add_move_category(self, id, data: dict):
        self.move_categories[id] = data

    def add_move_damage_class(self, id, data: dict):
        self.move_damage_classes[id] = data

    def add_move_learn_method(self, id, data: dict):
        self.move_learn_methods[id] = data

    def add_move_target(self, id, data: dict):
        self.move_targets[id] = data   

@dataclass
class Pokemons(CacheManager):
    abilities = dict()
    characteristics = dict()
    genders = dict()
    growth_rates = dict()
    natures = dict()
    pokeathlon_stats = dict()
    pokemons = dict()
    pokemon_location_areas = dict()
    pokemon_colors = dict()
    pokemon_forms = dict()
    pokemon_habitats = dict()
    pokemon_shapes = dict()
    pokemon_species = dict()
    stats = dict()
    types = dict()