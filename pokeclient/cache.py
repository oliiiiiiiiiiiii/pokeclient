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


@dataclass
class encounters:
    encounter_methods : dict
    encounter_conditions : dict
    encounter_condition_values : dict
    name_to_id_dict : dict


@dataclass
class evolutions:
    evolution_chains : dict
    encounter_triggers : dict
    name_to_id_dict : dict


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