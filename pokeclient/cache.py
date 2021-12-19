class CacheManager:
    def __init__(self) -> None:
        self.name_to_id_dict = dict()


class Berries(CacheManager):
    def __init__(self) -> None:
        super().__init__()
        self.berry_firmness = dict()
        self.berry_flavor = dict()
        self.berries = dict()

    def add_berry_firmness(self, id, data: dict):
        self.berry_firmness[id] = data

    def add_berry_flavour(self, id, data: dict):
        self.berry_flavour[id] = data

    def add_berry(self, id, data: dict):
        self.berry_flavour[id] = data


class Contests(CacheManager):
    def __init__(self) -> None:
        super().__init__()
        self.contest_types = dict()
        self.contest_effects = dict()
        self.super_contest_effects = dict()

    def add_contest_type(self, id, data: dict):
        self.contest_types[id] = data

    def add_contest_effect(self, id, data: dict):
        self.contest_effects[id] = data

    def add_super_contest_effect(self, id, data: dict):
        self.super_contest_effects[id] = data


class Encounters(CacheManager):
    def __init__(self) -> None:
        super().__init__()
        self.encounter_methods = dict()
        self.encounter_conditions = dict()
        self.encounter_condition_values = dict()

    def add_encounter_method(self, id, data: dict):
        self.encounter_methods[id] = data

    def add_encounter_condition(self, id, data: dict):
        self.encounter_conditions[id] = data

    def add_encounter_condition_value(self, id, data: dict):
        self.encounter_condition_values[id] = data


class Evolutions(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.evolution_chains = dict()
        self.encounter_triggers = dict()

    def add_evolution_chains(self, id, data: dict):
        self.evolution_chains[id] = data

    def add_encounter_triggers(self, id, data: dict):
        self.encounter_triggers[id] = data


class Games(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.generations = dict()
        self.versions = dict()
        self.version_groups = dict()

    def add_generation(self, id, data: dict):
        self.generations[id] = data

    def add_version(self, id, data: dict):
        self.versions[id] = data

    def add_version_group(self, id, data: dict):
        self.version_groups[id] = data


class Items(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.item_attributes = dict()
        self.item_categories = dict()
        self.item_fling_effects = dict()
        self.item_pockets = dict()
        self.items = dict()

    def add_item_attribute(self, id, data: dict):
        self.item_attributes[id] = data

    def add_item_category(self, id, data: dict):
        self.item_categories[id] = data

    def add_item_fling_effect(self, id, data: dict):
        self.item_fling_effects[id] = data

    def add_item_pocket(self, id, data: dict):
        self.item_pockets[id] = data

class Locations(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.locations = dict()
        self.location_areas = dict()
        self.pal_park_areas = dict()
        self.regions = dict()

    def add_location(self, id, data: dict):
        self.locations[id] = data

    def add_location_area(self, id, data: dict):
        self.location_areas[id] = data

    def add_pal_park_area(self, id, data: dict):
        self.pal_park_areas[id] = data

    def add_region(self, id, data: dict):
        self.regions[id] = data


class Machines(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.machines = dict()

    def add_machine(self, id, data: dict):
        self.machines[id] = data


class Moves(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.moves = dict()
        self.move_ailments = dict()
        self.move_battle_styles = dict()
        self.move_categories = dict()
        self.move_damage_classes = dict()
        self.move_learn_methods = dict()
        self.move_targets = dict()

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

class Pokemons(CacheManager):
    def __init__(self) -> None:
        super().__init__()
        self.abilities = dict()
        self.characteristics = dict()
        self.genders = dict()
        self.growth_rates = dict()
        self.natures = dict()
        self.pokeathlon_stats = dict()
        self.pokemons = dict()
        self.pokemon_location_areas = dict()
        self.pokemon_colors = dict()
        self.pokemon_forms = dict()
        self.pokemon_habitats = dict()
        self.pokemon_shapes = dict()
        self.pokemon_species = dict()
        self.stats = dict()
        self.types = dict()

        
    def add_ability(self, id, data: dict):
        self.abilities[id] = data

    def add_characteristic(self, id, data: dict):
        self.characteristics[id] = data

    def add_gender(self, id, data: dict):
        self.genders[id] = data

    def add_growth_rate(self, id, data: dict):
        self.growth_rates[id] = data

    def add_nature(self, id, data: dict):
        self.natures[id] = data

    def add_pokeathlon_stat(self, id, data: dict):
        self.pokeathlon_stats[id] = data

    def add_pokemon(self, id, data: dict):
        self.pokemons[id] = data   

    def add_pokemon_location_area(self, id, data: dict):
        self.pokemon_location_areas[id] = data 

    def add_pokemon_color(self, id, data: dict):
        self.pokemon_colors[id] = data

    def add_pokemon_form(self, id, data: dict):
        self.pokemon_forms[id] = data

    def add_pokemon_habitat(self, id, data: dict):
        self.pokemon_habitats[id] = data

    def add_pokemon_shape(self, id, data: dict):
        self.pokemon_shapes[id] = data

    def add_pokemon_species(self, id, data: dict):
        self.pokemon_species[id] = data

    def add_stat(self, id, data: dict):
        self.pokemon_stats[id] = data