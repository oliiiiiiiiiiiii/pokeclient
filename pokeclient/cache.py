from dataclasses import dataclass



@dataclass
class berriess:
    berry_firmness : dict
    berry_flavor : dict
    berries : dict
    name_to_id_dict : dict
    
    def add_berry_firmness(self,id,data:dict):
        self.berry_firmness[id] = data

    def add_berry_flavour(self,id,data:dict):
        self.berry_flavour[id] = data

    def add_berry(self,id,data:dict):
        self.berry_flavour[id] = data

@dataclass
class contests:
    contest_types : dict
    contest_effects : dict
    super_contest_effects : dict
    name_to_id_dict : dict

    def add_contest_types(self,id,data:dict):
        self.contest_types[id] = data

    def add_contest_effects(self,id,data:dict):
        self.contest_effects[id] = data

    def add_super_contest_effects(self,id,data:dict):
        self.super_contest_effects[id] = data

@dataclass
class encounters:
    encounter_methods : dict
    encounter_conditions : dict
    encounter_condition_values : dict
    name_to_id_dict : dict

    def add_encounter_methods(self,id,data:dict):
        self.encounter_methods[id] = data

    def add_encounter_conditions(self,id,data:dict):
        self.encounter_conditions[id] = data

    def add_encounter_condition_values(self,id,data:dict):
        self.encounter_condition_values[id] = data


@dataclass
class evolutions:
    evolution_chains : dict
    encounter_triggers : dict
    name_to_id_dict : dict

    def add_evolution_chains(self,id,data:dict):
        self.evolution_chains[id] = data

    def add_encounter_triggers(self,id,data:dict):
        self.encounter_triggers[id] = data


@dataclass
class games:
    generations : dict
    versions : dict
    version_groups : dict
    name_to_id_dict : dict


@dataclass
class itemss:
    item_attributes : dict
    item_categories : dict
    item_fling_effects : dict
    item_pockets : dict
    items : dict
    name_to_id_dict : dict

@dataclass
class locationss:
    locations : dict
    location_areas : dict
    pal_park_areas : dict
    regions : dict
    name_to_id_dict : dict


@dataclass
class machiness:
    machines : dict
    name_to_id_dict : dict

@dataclass
class movess:
    moves : dict
    move_ailment : dict
    move_battle_style : dict
    move_categories : dict
    move_damage_classes : dict
    move_learn_methods : dict
    move_targets : dict
    name_to_id_dict : dict

@dataclass
class pokemonss:
    abilities : dict
    characteristics : dict
    genders : dict
    growth_rates : dict
    natures : dict
    pokeathlon_stats : dict
    pokemons : dict
    pokemon_location_areas : dict
    pokemon_colors : dict
    pokemon_forms : dict
    pokemon_habitats : dict
    pokemon_shapes : dict
    pokemon_species : dict
    stats : dict
    types : dict
    name_to_id_dict : dict


berry_cache = berriess(dict(),dict(),dict(),dict())
contest_cache = contests(dict(),dict(),dict(),dict())
encounter_cache = encounters(dict(),dict(),dict(),dict())
evolution_cache = evolutions(dict(),dict(),dict())
game_cache = games(dict(),dict(),dict(),dict())
items_cache = itemss(dict(),dict(),dict(),dict(),dict(),dict())
location_cache = locationss(dict(),dict(),dict(),dict(),dict())
machine_cache = machiness(dict(),dict())
move_cache = movess(dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict())
poke_cache = pokemonss(dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict())