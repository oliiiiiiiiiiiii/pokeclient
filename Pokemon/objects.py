from .base import BaseType1, BaseType2
import Pokemon.caching as caching
import Pokemon.errors as errors

berry_cache = caching.BerryCache()
contest_cache = caching.ContestCache()
encounter_cache = caching.EncounterCache()
evolution_cache = caching.EvolutionCache()
game_cache = caching.GameCache()
item_cache = caching.ItemCache()
location_cache = caching.LocationCache()
machine_cache = caching.MachineCache()
move_cache = caching.MoveCache()
pokemon_cache = caching.PokemonCache()


class BerryGroup(BaseType1):
    @property
    def cache(self) -> object:
        return berry_cache

    @property
    def error(self) -> Exception:
        return errors.BerryNotFound

    @property
    def parsed_data(self) -> object:
        ...

    @property
    def address(self) -> str:
        ...


class Berry(BerryGroup):
    @property
    def address(self) -> str:
        return "berry"

    @property
    def parsed_data(self) -> object:
        return


class BerryFirmness(BerryGroup):
    @property
    def address(self) -> str:
        return "berry-firmness"

    @property
    def parsed_data(self) -> object:
        return


class BerryFlavour(BerryGroup):
    @property
    def address(self) -> str:
        return "berry-flavour"

    @property
    def parsed_data(self) -> object:
        return


class ContestGroup(BaseType2):
    @property
    def cache(self) -> object:
        return contest_cache

    @property
    def error(self) -> Exception:
        return errors.ContestNotFound

    @property
    def parsed_data(self) -> object:
        ...

    @property
    def address(self) -> str:
        ...


class ContestType(BaseType1):
    @property
    def address(self) -> str:
        return "contest-type"

    @property
    def cache(self) -> object:
        return contest_cache

    @property
    def error(self) -> Exception:
        return errors.ContestNotFound

    @property
    def parsed_data(self) -> object:
        ...


class ContestEffect(ContestGroup):
    @property
    def address(self) -> str:
        return "contest-effect"

    @property
    def parsed_data(self) -> object:
        return


class SuperContestEffect(ContestGroup):
    @property
    def address(self) -> str:
        return "super-contest-effect"

    @property
    def parsed_data(self) -> object:
        return


class EncounterGroup(BaseType1):
    @property
    def address(self) -> str:
        ...

    @property
    def cache(self) -> object:
        return encounter_cache

    @property
    def error(self) -> Exception:
        return errors.EncounterNotFound

    @property
    def parsed_data(self) -> object:
        ...


class EncounterMethod(EncounterGroup):
    @property
    def address(self) -> str:
        return "encounter-method"

    @property
    def parsed_data(self) -> object:
        return


class EncounterCondition(EncounterGroup):
    @property
    def address(self) -> str:
        return "encounter-condition"

    @property
    def parsed_data(self) -> object:
        return


class EncounterConditionValue(EncounterGroup):
    @property
    def address(self) -> str:
        return "encounter-condition-value"

    @property
    def parsed_data(self) -> object:
        return


class EvolutionGroup(BaseType2):
    @property
    def address(self) -> str:
        ...

    @property
    def cache(self) -> object:
        return evolution_cache

    @property
    def error(self) -> Exception:
        return errors.EvolutionNotFound

    @property
    def parsed_data(self) -> object:
        ...


class EvolutionChain(EvolutionGroup):
    @property
    def address(self) -> str:
        return "evolution-chain"

    @property
    def parsed_data(self) -> object:
        return


class EvolutionTrigger(EvolutionGroup):
    @property
    def address(self) -> str:
        return "evolution-trigger"

    @property
    def parsed_data(self) -> object:
        return


class GameGroup(BaseType1):
    @property
    def address(self) -> str:
        ...
    @property
    def cache(self) -> object:
        return game_cache

    @property
    def error(self) -> Exception:
        return errors.GameNotFound

    @property
    def parsed_data(self) -> object:
        ...


class Generation(GameGroup):
    @property
    def address(self) -> str:
        return "generation"

    @property
    def parsed_data(self) -> object:
        return


class Pokedex(GameGroup):
    @property
    def address(self) -> str:
        return "pokedex"

    @property
    def parsed_data(self) -> object:
        return


class Version(GameGroup):
    @property
    def address(self) -> str:
        return "version"

    @property
    def parsed_data(self) -> object:
        return


class VersionGroup(GameGroup):
    @property
    def address(self) -> str:
        return "version-group"

    @property
    def parsed_data(self) -> object:
        return


class ItemGroup(BaseType1):
    @property
    def address(self) -> str:
        ...
    @property
    def cache(self) -> object:
        return item_cache

    @property
    def error(self) -> Exception:
        return errors.ItemNotFound

    @property
    def parsed_data(self) -> object:
        ...


class ItemAttribute(ItemGroup):
    @property
    def address(self) -> str:
        return "item-attribute"

    @property
    def parsed_data(self) -> object:
        return


class ItemCategory(ItemGroup):
    @property
    def address(self) -> str:
        return "item-category"

    @property
    def parsed_data(self) -> object:
        return


class ItemFlingEffect(ItemGroup):
    @property
    def address(self) -> str:
        return "item-fling-effect"

    @property
    def parsed_data(self) -> object:
        return


class Item(ItemGroup):
    @property
    def address(self) -> str:
        return "item"

    @property
    def parsed_data(self) -> object:
        return


class LocationGroup(BaseType1):
    @property
    def address(self) -> str:
        ...    
    @property
    def cache(self) -> object:
        return location_cache

    @property
    def error(self) -> Exception:
        return errors.LocationNotFound

    @property
    def parsed_data(self) -> object:
        ...


class Location(LocationGroup):
    @property
    def address(self) -> str:
        return "location"

    @property
    def parsed_data(self) -> object:
        return


class LocationArea(LocationGroup):
    @property
    def address(self) -> str:
        return "location-area"

    @property
    def parsed_data(self) -> object:
        return


class PalParkArea(LocationGroup):
    @property
    def address(self) -> str:
        return "pal-park-area"

    @property
    def parsed_data(self) -> object:
        return


class Region(LocationGroup):
    @property
    def address(self) -> str:
        return "region"

    @property
    def parsed_data(self) -> object:
        return


class Machine(BaseType2):
    @property
    def address(self) -> str:
        return "machine"

    @property
    def cache(self) -> object:
        return machine_cache

    @property
    def error(self) -> Exception:
        return errors.MachineNotFound

    @property
    def parsed_data(self) -> object:
        return


class MoveGroup(BaseType1):
    @property
    def address(self) -> str:
        ...    
    @property
    def error(self) -> Exception:
        return errors.MoveNotFound

    @property
    def cache(self) -> object:
        return move_cache

    @property
    def parsed_data(self) -> object:
        ...


class Move(MoveGroup):
    @property
    def address(self) -> str:
        return "move"

    @property
    def parsed_data(self) -> object:
        return


class MoveAilment(MoveGroup):
    @property
    def address(self) -> str:
        return "move-ailment"

    @property
    def parsed_data(self) -> object:
        return


class MoveBattleStyle(MoveGroup):
    @property
    def address(self) -> str:
        return "move-battle-style"

    @property
    def parsed_data(self) -> object:
        return


class MoveCategory(MoveGroup):
    @property
    def address(self) -> str:
        return "move-category"

    @property
    def parsed_data(self) -> object:
        return


class MoveDamageClass(MoveGroup):
    @property
    def address(self) -> str:
        return "move-damage-class"

    @property
    def parsed_data(self) -> object:
        return


class MoveLearnMethod(MoveGroup):
    @property
    def address(self) -> str:
        return "move-learn-method"

    @property
    def parsed_data(self) -> object:
        return


class MoveTarget(MoveGroup):
    @property
    def address(self) -> str:
        return "move-target"

    @property
    def parsed_data(self) -> object:
        return


class PokemonGroup(BaseType1):
    @property
    def address(self) -> str:
        ...    
    @property
    def error(self) -> Exception:
        return errors.PokemonNotFound

    @property
    def cache(self) -> object:
        return pokemon_cache

    @property
    def parsed_data(self) -> object:
        ...


class Ability(PokemonGroup):
    @property
    def address(self) -> str:
        return "ability"

    @property
    def parsed_data(self) -> object:
        return

class Characteristic(BaseType2):
    @property
    def address(self) -> str:
        return "characteristic"

    @property
    def parsed_data(self) -> object:
        return

    @property
    def error(self) -> Exception:
        return errors.PokemonNotFound

    @property
    def cache(self) -> object:
        return pokemon_cache


class Gender(BaseType2):
    @property
    def address(self) -> str:
        return "gender"

    @property
    def parsed_data(self) -> object:
        return

    @property
    def error(self) -> Exception:
        return errors.PokemonNotFound

    @property
    def cache(self) -> object:
        return pokemon_cache



class GrowthRate(BaseType2):
    @property
    def address(self) -> str:
        return "growth-rate"

    @property
    def parsed_data(self) -> object:
        return

    @property
    def error(self) -> Exception:
        return errors.PokemonNotFound

    @property
    def cache(self) -> object:
        return pokemon_cache



class Nature(PokemonGroup):
    @property
    def address(self) -> str:
        return "nature"

    @property
    def parsed_data(self) -> object:
        return


class PokeathlonStat(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokeathlon-stat"

    @property
    def parsed_data(self) -> object:
        return


class Pokemon(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon"

    @property
    def parsed_data(self) -> object:
        return


class PokemonLocationArea(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon"

    @property
    def url(self) -> str:
        return (
            f"https://pokeapi.co/api/v2/pokemon/{self.id}/encounters"
            or f"https://pokeapi.co/api/v2/pokemon{self.name}/encounters"
        )

    @property
    def parsed_data(self) -> object:
        return


class PokemonColor(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-color"

    @property
    def parsed_data(self) -> object:
        return


class PokemonForm(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-form"

    @property
    def parsed_data(self) -> object:
        return


class PokemonHabitat(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-habitat"

    @property
    def parsed_data(self) -> object:
        return


class PokemonShape(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-shape"

    @property
    def parsed_data(self) -> object:
        return


class PokemonSpecies(PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-species"

    @property
    def parsed_data(self) -> object:
        return


class Stat(PokemonGroup):
    @property
    def address(self) -> str:
        return "stat"

    @property
    def parsed_data(self) -> object:
        return


class Type(PokemonGroup):
    @property
    def address(self) -> str:
        return "type"

    @property
    def parsed_data(self) -> object:
        return
