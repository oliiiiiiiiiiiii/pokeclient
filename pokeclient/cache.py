from dataclasses import dataclass

@dataclass
class berriess:
    berry_firmness : dict
    berry_flavor : dict
    berries : dict


@dataclass
class contests:
    contest_types : dict
    contest_effects : dict
    super_contest_effects : dict


@dataclass
class encounters:
    encounter_methods : dict
    encounter_conditions : dict
    encounter_condition_values : dict


@dataclass
class evolutions:
    evolution_chains : dict
    encounter_triggers : dict


@dataclass
class games:
    generations : dict
    versions : dict
    version_groups : dict


@dataclass
class itemss:
    item_attributes : dict
    item_categories : dict
    item_fling_effects : dict
    item_pockets : dict
    items : dict

@dataclass
class locationss:
    locations : dict
    location_areas : dict
    pal_park_areas : dict
    regions : dict


@dataclass
class machiness:
    machines : dict

@dataclass
class movess:
    moves : dict
    move_ailment : dict
    move_battle_style : dict
    move_categories : dict
    move_damage_classes : dict
    move_learn_methods : dict
    move_targets : dict

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