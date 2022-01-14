from base import BaseType1, BaseType2
from abc import ABC
import caching
import errors

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


class BerryGroup(ABC):
    @property
    def cache(self) -> object:
        return berry_cache

    @property
    def error(self) -> Exception:
        return errors.BerryNotFound


class Berry(BaseType1, BerryGroup):
    @property
    def address(self) -> str:
        return "berry"

    @property
    def parsed_data(self) -> object:
        return


class BerryFirmness(BaseType1, BerryGroup):
    @property
    def address(self) -> str:
        return "berry-firmness"

    @property
    def parsed_data(self) -> object:
        return


class BerryFlavour(BaseType1, BerryGroup):
    @property
    def address(self) -> str:
        return "berry-flavour"

    @property
    def parsed_data(self) -> object:
        return


class ContestGroup(ABC):
    @property
    def cache(self) -> object:
        return contest_cache

    @property
    def error(self) -> Exception:
        return errors.ContestNotFound


class ContestType(BaseType1, ContestGroup):
    @property
    def address(self) -> str:
        return "contest-type"

    @property
    def parsed_data(self) -> object:
        return


class ContestEffect(BaseType2, ContestGroup):
    @property
    def address(self) -> str:
        return "contest-effect"

    @property
    def parsed_data(self) -> object:
        return


class SuperContestEffect(BaseType2, ContestGroup):
    @property
    def address(self) -> str:
        return "super-contest-effect"

    @property
    def parsed_data(self) -> object:
        return


class EncounterGroup(ABC):
    @property
    def cache(self) -> object:
        return encounter_cache

    @property
    def error(self) -> Exception:
        return errors.EncounterNotFound


class EncounterMethod(BaseType1, EncounterGroup):
    @property
    def address(self) -> str:
        return "encounter-method"

    @property
    def parsed_data(self) -> object:
        return


class EncounterCondition(BaseType1, EncounterGroup):
    @property
    def address(self) -> str:
        return "encounter-condition"

    @property
    def parsed_data(self) -> object:
        return


class EncounterConditionValue(BaseType1, EncounterGroup):
    @property
    def address(self) -> str:
        return "encounter-condition-value"

    @property
    def parsed_data(self) -> object:
        return


class EvolutionGroup(ABC):
    @property
    def cache(self) -> object:
        return evolution_cache

    @property
    def error(self) -> Exception:
        return errors.EvolutionNotFound


class EvolutionChain(BaseType2, EvolutionGroup):
    @property
    def address(self) -> str:
        return "evolution-chain"

    @property
    def parsed_data(self) -> object:
        return


class EvolutionTrigger(BaseType2, EvolutionGroup):
    @property
    def address(self) -> str:
        return "evolution-trigger"

    @property
    def parsed_data(self) -> object:
        return


class GameGroup(ABC):
    @property
    def cache(self) -> object:
        return game_cache

    @property
    def error(self) -> Exception:
        return errors.GameNotFound


class Generation(BaseType1, GameGroup):
    @property
    def address(self) -> str:
        return "generation"

    @property
    def parsed_data(self) -> object:
        return


class Pokedex(BaseType1, GameGroup):
    @property
    def address(self) -> str:
        return "pokedex"

    @property
    def parsed_data(self) -> object:
        return


class Version(BaseType1, GameGroup):
    @property
    def address(self) -> str:
        return "version"

    @property
    def parsed_data(self) -> object:
        return


class VersionGroup(BaseType1, GameGroup):
    @property
    def address(self) -> str:
        return "version-group"

    @property
    def parsed_data(self) -> object:
        return


class ItemGroup(ABC):
    @property
    def cache(self) -> object:
        return item_cache

    @property
    def error(self) -> Exception:
        return errors.ItemNotFound


class ItemAttribute(BaseType1, ItemGroup):
    @property
    def address(self) -> str:
        return "item-attribute"

    @property
    def parsed_data(self) -> object:
        return


class ItemCategory(BaseType1, ItemGroup):
    @property
    def address(self) -> str:
        return "item-category"

    @property
    def parsed_data(self) -> object:
        return


class ItemFlingEffect(BaseType1, ItemGroup):
    @property
    def address(self) -> str:
        return "item-fling-effect"

    @property
    def parsed_data(self) -> object:
        return


class Item(BaseType1, ItemGroup):
    @property
    def address(self) -> str:
        return "item"

    @property
    def parsed_data(self) -> object:
        return


class LocationGroup(ABC):
    @property
    def cache(self) -> object:
        return location_cache

    @property
    def error(self) -> Exception:
        return errors.LocationNotFound


class Location(BaseType1, LocationGroup):
    @property
    def address(self) -> str:
        return "location"

    @property
    def parsed_data(self) -> object:
        return


class LocationArea(BaseType1, LocationGroup):
    @property
    def address(self) -> str:
        return "location-area"

    @property
    def parsed_data(self) -> object:
        return


class PalParkArea(BaseType1, LocationGroup):
    @property
    def address(self) -> str:
        return "pal-park-area"

    @property
    def parsed_data(self) -> object:
        return


class Region(BaseType1, LocationGroup):
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


class MoveGroup(ABC):
    @property
    def error(self) -> Exception:
        return errors.MoveNotFound

    @property
    def cache(self) -> object:
        return move_cache


class Move(BaseType1, MoveGroup):
    @property
    def address(self) -> str:
        return "move"

    @property
    def parsed_data(self) -> object:
        return


class MoveAilment(BaseType1, MoveGroup):
    @property
    def address(self) -> str:
        return "move-ailment"

    @property
    def parsed_data(self) -> object:
        return


class MoveBattleStyle(BaseType1, MoveGroup):
    @property
    def address(self) -> str:
        return "move-battle-style"

    @property
    def parsed_data(self) -> object:
        return


class MoveCategory(BaseType1, MoveGroup):
    @property
    def address(self) -> str:
        return "move-category"

    @property
    def parsed_data(self) -> object:
        return


class MoveDamageClass(BaseType1, MoveGroup):
    @property
    def address(self) -> str:
        return "move-damage-class"

    @property
    def parsed_data(self) -> object:
        return


class MoveLearnMethod(BaseType1, MoveGroup):
    @property
    def address(self) -> str:
        return "move-learn-method"

    @property
    def parsed_data(self) -> object:
        return


class MoveTarget(BaseType1, MoveGroup):
    @property
    def address(self) -> str:
        return "move-target"

    @property
    def parsed_data(self) -> object:
        return


class PokemonGroup(ABC):
    @property
    def error(self) -> Exception:
        return errors.PokemonNotFound

    @property
    def cache(self) -> object:
        return pokemon_cache


class Ability(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "ability"

    @property
    def parsed_data(self) -> object:
        return


class Characteristic(BaseType2, PokemonGroup):
    @property
    def address(self) -> str:
        return "characteristic"

    @property
    def parsed_data(self) -> object:
        return


class Gender(BaseType2, PokemonGroup):
    @property
    def address(self) -> str:
        return "gender"

    @property
    def parsed_data(self) -> object:
        return


class GrowthRate(BaseType2, PokemonGroup):
    @property
    def address(self) -> str:
        return "growth-rate"

    @property
    def parsed_data(self) -> object:
        return


class Nature(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "nature"

    @property
    def parsed_data(self) -> object:
        return


class PokeathlonStat(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "pokeathlon-stat"

    @property
    def parsed_data(self) -> object:
        return


class Pokemon(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon"

    @property
    def parsed_data(self) -> object:
        return


class PokemonLocationArea(BaseType1, PokemonGroup):
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


class PokemonColor(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-color"

    @property
    def parsed_data(self) -> object:
        return


class PokemonForm(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-form"

    @property
    def parsed_data(self) -> object:
        return


class PokemonHabitat(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-habitat"

    @property
    def parsed_data(self) -> object:
        return


class PokemonShape(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-shape"

    @property
    def parsed_data(self) -> object:
        return


class PokemonSpecies(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "pokemon-species"

    @property
    def parsed_data(self) -> object:
        return


class Stat(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "stat"

    @property
    def parsed_data(self) -> object:
        return


class Type(BaseType1, PokemonGroup):
    @property
    def address(self) -> str:
        return "type"

    @property
    def parsed_data(self) -> object:
        return
