class CacheManager:
    def __init__(self) -> None:
        self.name_id_map = dict()


class Berries(CacheManager):
    def __init__(self) -> None:
        super().__init__()
        self.berry_firmness = dict()
        self.berry_flavors = dict()
        self.berries = dict()

    def add_berry_firmness(self, id, data: dict) -> None:
        if not len(self.name_id_map) >= 10:
            self.berry_firmness[id] = data
        else:
            self.__init__()
            self.berry_firmness[id] = data

    def add_berry_flavour(self, id, data: dict) -> None:
        if not len(self.name_id_map) >= 10:
            self.berry_flavours[id] = data
        else:
            self.__init__()
            self.berry_flavour[id] = data

    def add_berry(self, id, data: dict) -> None:
        if not len(self.name_id_map) >= 10:
            self.berries[id] = data
        else:
            self.__init__()
            self.berries[id] = data


class Contests(CacheManager):
    def __init__(self) -> None:
        super().__init__()
        self.contest_types = dict()
        self.contest_effects = dict()
        self.super_contest_effects = dict()

    def add_contest_type(self, id, data: dict) -> None:
        if (not len(self.name_id_map) >= 10
            or not len(self.contest_effects) >= 10
            or not len(self.super_contest_effects) >= 10):
            self.contest_types[id] = data
        else:
            self.__init__()
            self.contest_types[id] = data

    def add_contest_effect(self, id, data: dict) -> None:
        if (not len(self.name_id_map) >= 10
            or not len(self.contest_effects) >= 10
            or not len(self.super_contest_effects) >= 10):
            self.contest_effects[id] = data
        else:
            self.__init__()
            self.contest_effects[id] = data

    def add_super_contest_effect(self, id, data: dict) -> None:
        if (not len(self.name_id_map) >= 10
            or not len(self.contest_effects) >= 10
            or not len(self.super_contest_effects) >= 10):
            self.super_contest_effects[id] = data
        else:
            self.__init__()
            self.super_contest_effects[id] = data

class Encounters(CacheManager):
    def __init__(self) -> None:
        super().__init__()
        self.encounter_methods = dict()
        self.encounter_conditions = dict()
        self.encounter_condition_values = dict()

    def add_encounter_method(self, id, data: dict) -> None:
        if not len(self.name_id_map) >= 10:
            self.encounter_methods[id] = data
        else:
            self.__init__()
            self.encounter_methods[id] = data

    def add_encounter_condition(self, id, data: dict) -> None:
        if not len(self.name_id_map) >= 10:
            self.encounter_conditions[id] = data
        else:
            self.__init__()
            self.encounter_conditions[id] = data

    def add_encounter_condition_value(self, id, data: dict) -> None:
        if not len(self.name_id_map) >= 10:
            self.encounter_condition_values[id] = data
        else:
            self.__init__()
            self.encounter_condition_values[id] = data



class Evolutions:
    def __init__(self) -> None:   
        self.evolution_chains = dict()
        self.evolution_triggers = dict()

    def add_evolution_chain(self, id, data: dict) -> None:
        if (not len(self.evolution_chains) >= 10 or 
            not len(self.evolution_triggers) >= 10):
            self.evolution_chains[id] = data
        else:
            self.__init__()
            self.encounter_condition_values[id] = data

    def add_evolution_trigger(self, id, data: dict) -> None:
        if (not len(self.evolution_chains) >= 10 or 
            not len(self.evolution_triggers) >= 10):
            self.evolution_triggers[id] = data
        else:
            self.__init__()
            self.evolution_triggers[id] = data
        


class Games(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.generations = dict()
        self.pokedexes = dict()
        self.versions = dict()
        self.version_groups = dict()

    def add_generation(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.generations[id] = data
        else:
            self.__init__()
            self.generations[id] = data
        
    def add_pokedex(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.pokedexes[id] = data
        else:
            self.__init__()
            self.pokedexes[id] = data
        
    def add_version(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.versions[id] = data
        else:
            self.__init__()
            self.versions[id] = data
        
    def add_version_group(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.version_groups[id] = data
        else:
            self.__init__()
            self.version_groups[id] = data
        

class Items(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.item_attributes = dict()
        self.item_categories = dict()
        self.item_fling_effects = dict()
        self.item_pockets = dict()
        self.items = dict()

    def add_item_attribute(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.item_attributes[id] = data
        else:
            self.__init__()
            self.item_attributes[id] = data
        
    def add_item_category(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.item_categories[id] = data
        else:
            self.__init__()
            self.item_categories[id] = data
        
    def add_item_fling_effect(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.item_fling_effects[id] = data
        else:
            self.__init__()
            self.item_fling_effects[id] = data

    def add_item_pocket(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.item_pockets[id] = data
        else:
            self.__init__()
            self.item_pockets[id] = data
        
class Locations(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.locations = dict()
        self.location_areas = dict()
        self.pal_park_areas = dict()
        self.regions = dict()

    def add_location(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.locations[id] = data
        else:
            self.__init__()
            self.locations[id] = data
        

    def add_location_area(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.location_areas[id] = data
        else:
            self.__init__()
            self.location_areas[id] = data
        
    def add_pal_park_area(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.pal_park_areas[id] = data
        else:
            self.__init__()
            self.pal_park_areas[id] = data
        

    def add_region(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.regions[id] = data
        else:
            self.__init__()
            self.regions[id] = data
        


class Machines(CacheManager):
    def __init__(self) -> None:
        super().__init__()    
        self.machines = dict()

    def add_machine(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.machines[id] = data
        else:
            self.__init__()
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

    def add_move(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.moves[id] = data
        else:
            self.__init__()
            self.moves[id] = data

    def add_move_ailment(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.move_ailments[id] = data
        else:
            self.__init__()
            self.move_ailments[id] = data        

    def add_move_battle_style(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.move_battle_styles[id] = data
        else:
            self.__init__()
            self.move_battle_styles[id] = data          
        
    def add_move_category(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.move_categories[id] = data
        else:
            self.__init__()
            self.move_categories[id] = data  
        
    def add_move_damage_class(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.move_damage_classes[id] = data
        else:
            self.__init__()
            self.move_damage_classes[id] = data         
        
    def add_move_learn_method(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.move_learn_methods[id] = data
        else:
            self.__init__()
            self.move_learn_methods[id] = data       
        
    def add_move_target(self, id, data: dict) -> None:
        if not len(self.evolution_chains) >= 10:
            self.move_targets[id] = data   
        else:
            self.__init__()
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

        
    def add_ability(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.abilities[id] = data   
        else:
            self.__init__()
            self.abilities[id] = data          
        
    def add_characteristic(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.characteristics[id] = data  
        else:
            self.__init__()
            self.characteristics[id] = data 
        
    def add_gender(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.genders[id] = data
        else:
            self.__init__()
            self.genders[id] = data         
        
    def add_growth_rate(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.growth_rates[id] = data
        else:
            self.__init__()
            self.growth_rates[id] = data        
        

    def add_nature(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.natures[id] = data
        else:
            self.__init__()
            self.natures[id] = data         
        

    def add_pokeathlon_stat(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokeathlon_stats[id] = data
        else:
            self.__init__()
            self.pokeathlon_stats[id] = data       
        

    def add_pokemon(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokemons[id] = data   
        else:
            self.__init__()
            self.pokemons[id] = data           
        

    def add_pokemon_location_area(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokemon_location_areas[id] = data   
        else:
            self.__init__()
            self.pokemon_location_areas[id] = data         
         

    def add_pokemon_color(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokemon_colors[id] = data  
        else:
            self.__init__()
            self.pokemon_colors[id] = data         
        

    def add_pokemon_form(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokemon_forms[id] = data
        else:
            self.__init__()
            self.pokemon_forms[id] = data        
        

    def add_pokemon_habitat(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokemon_habitats[id] = data
        else:
            self.__init__()
            self.pokemon_habitats[id] = data        
        

    def add_pokemon_shape(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokemon_shapes[id] = data
        else:
            self.__init__()
            self.pokemon_shapes[id] = data       
        

    def add_pokemon_species(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.pokemon_species[id] = data
        else:
            self.__init__()
            self.pokemon_species[id] = data         
        

    def add_stat(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.stats[id] = data
        else:
            self.__init__()
            self.stats[id] = data       
        

    def add_type(self, id, data: dict) -> None:
        if (
            not len(self.name_id_map) >= 10 
            or not len(self.characteristics) >= 10 
            or not len(self.genders) >= 10
            or not len(self.growth_rates) >= 10
        ):
            self.types[id] = data
        else:
            self.__init__()
            self.types[id] = data         
        