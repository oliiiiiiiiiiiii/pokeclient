from base import BaseType1, BaseType2
from errors import (
    BerryNotFound,
    ContestNotFound,
    EncounterNotFound,
    EvolutionNotFound,
    GameNotFound,
    ItemNotFound,
    LocationNotFound,
    MachineNotFound,
    MoveNotFound,
    PokemonNotFound,
)


class Berry(BaseType1):
    @property
    def address(self) -> str:
        return "berry"

    @property
    def error(self) -> type:
        return BerryNotFound

    @property
    def parsed_data(self) -> object:
        return


class BerryFirmness(BaseType1):
    @property
    def address(self) -> str:
        return "berry-firmness"

    @property
    def error(self) -> type:
        return BerryNotFound

    @property
    def parsed_data(self) -> object:
        return


class BerryFlavour(BaseType1):
    @property
    def address(self) -> str:
        return "berry-flavour"

    @property
    def error(self) -> type:
        return BerryNotFound

    @property
    def parsed_data(self) -> object:
        return


class ContestType(BaseType1):
    @property
    def address(self) -> str:
        return "contest-type"

    @property
    def error(self) -> type:
        return ContestNotFound

    @property
    def parsed_data(self) -> object:
        return


class ContestEffect(BaseType2):
    @property
    def address(self) -> str:
        return "contest-effect"

    @property
    def error(self) -> type:
        return ContestNotFound

    @property
    def parsed_data(self) -> object:
        return


class SuperContestEffect(BaseType2):
    @property
    def address(self) -> str:
        return "super-contest-effect"

    @property
    def error(self) -> type:
        return ContestNotFound

    @property
    def parsed_data(self) -> object:
        return


class EncounterMethod(BaseType1):
    @property
    def address(self) -> str:
        return "encounter-method"

    @property
    def error(self) -> type:
        return EncounterNotFound

    @property
    def parsed_data(self) -> object:
        return


class EncounterCondition(BaseType1):
    @property
    def address(self) -> str:
        return "encounter-condition"

    @property
    def error(self) -> type:
        return EncounterNotFound

    @property
    def parsed_data(self) -> object:
        return


class EncounterConditionValue(BaseType1):
    @property
    def address(self) -> str:
        return "encounter-condition-value"

    @property
    def error(self) -> type:
        return EncounterNotFound

    @property
    def parsed_data(self) -> object:
        return


class EvolutionChain(BaseType2):
    @property
    def address(self) -> str:
        return "evolution-chain"

    @property
    def error(self) -> type:
        return EvolutionNotFound

    @property
    def parsed_data(self) -> object:
        return


class EvolutionTrigger(BaseType2):
    @property
    def address(self) -> str:
        return "evolution-trigger"

    @property
    def error(self) -> type:
        return EvolutionNotFound

    @property
    def parsed_data(self) -> object:
        return


class Generation(BaseType1):
    @property
    def address(self) -> str:
        return "generation"

    @property
    def error(self) -> type:
        return GameNotFound

    @property
    def parsed_data(self) -> object:
        return


class Pokedex(BaseType1):
    @property
    def address(self) -> str:
        return "pokedex"

    @property
    def error(self) -> type:
        return GameNotFound

    @property
    def parsed_data(self) -> object:
        return


class Version(BaseType1):
    @property
    def address(self) -> str:
        return "version"

    @property
    def error(self) -> type:
        return GameNotFound

    @property
    def parsed_data(self) -> object:
        return


class VersionGroup(BaseType1):
    @property
    def address(self) -> str:
        return "version-group"

    @property
    def error(self) -> type:
        return GameNotFound

    @property
    def parsed_data(self) -> object:
        return


class ItemAttribute(BaseType1):
    @property
    def address(self) -> str:
        return "item-attribute"

    @property
    def error(self) -> type:
        return ItemNotFound

    @property
    def parsed_data(self) -> object:
        return


class ItemCategory(BaseType1):
    @property
    def address(self) -> str:
        return "item-category"

    @property
    def error(self) -> type:
        return ItemNotFound

    @property
    def parsed_data(self) -> object:
        return


class ItemFlingEffect(BaseType1):
    @property
    def address(self) -> str:
        return "item-fling-effect"

    @property
    def error(self) -> type:
        return ItemNotFound

    @property
    def parsed_data(self) -> object:
        return


class Item(BaseType1):
    @property
    def address(self) -> str:
        return "item"

    @property
    def error(self) -> type:
        return ItemNotFound

    @property
    def parsed_data(self) -> object:
        return


class Location(BaseType1):
    @property
    def address(self) -> str:
        return "location"

    @property
    def error(self) -> type:
        return LocationNotFound

    @property
    def parsed_data(self) -> object:
        return


class LocationArea(BaseType1):
    @property
    def address(self) -> str:
        return "location-area"

    @property
    def error(self) -> type:
        return LocationNotFound

    @property
    def parsed_data(self) -> object:
        return


class PalParkArea(BaseType1):
    @property
    def address(self) -> str:
        return "pal-park-area"

    @property
    def error(self) -> type:
        return LocationNotFound

    @property
    def parsed_data(self) -> object:
        return


class Region(BaseType1):
    @property
    def address(self) -> str:
        return "region"

    @property
    def error(self) -> type:
        return LocationNotFound

    @property
    def parsed_data(self) -> object:
        return


class Machine(BaseType2):
    @property
    def address(self) -> str:
        return "machine"

    @property
    def error(self) -> type:
        return MachineNotFound

    @property
    def parsed_data(self) -> object:
        return


class Move(BaseType1):
    @property
    def address(self) -> str:
        return "move"

    @property
    def error(self) -> type:
        return MoveNotFound

    @property
    def parsed_data(self) -> object:
        return


class MoveAilment(BaseType1):
    @property
    def address(self) -> str:
        return "move-ailment"

    @property
    def error(self) -> type:
        return MoveNotFound

    @property
    def parsed_data(self) -> object:
        return


class MoveBattleStyle(BaseType1):
    @property
    def address(self) -> str:
        return "move-battle-style"

    @property
    def error(self) -> type:
        return MoveNotFound

    @property
    def parsed_data(self) -> object:
        return


class MoveCategory(BaseType1):
    @property
    def address(self) -> str:
        return "move-category"

    @property
    def error(self) -> type:
        return MoveNotFound

    @property
    def parsed_data(self) -> object:
        return


class MoveDamageClass(BaseType1):
    @property
    def address(self) -> str:
        return "move-damage-class"

    @property
    def error(self) -> type:
        return MoveNotFound

    @property
    def parsed_data(self) -> object:
        return


class MoveLearnMethod(BaseType1):
    @property
    def address(self) -> str:
        return "move-learn-method"

    @property
    def error(self) -> type:
        return MoveNotFound

    @property
    def parsed_data(self) -> object:
        return


class MoveTarget(BaseType1):
    @property
    def address(self) -> str:
        return "move-target"

    @property
    def error(self) -> type:
        return MoveNotFound

    @property
    def parsed_data(self) -> object:
        return


class Ability(BaseType1):
    @property
    def address(self) -> str:
        return "ability"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class Characteristic(BaseType2):
    @property
    def address(self) -> str:
        return "characteristic"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class Gender(BaseType2):
    @property
    def address(self) -> str:
        return "gender"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class GrowthRate(BaseType2):
    @property
    def address(self) -> str:
        return "growth-rate"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class Nature(BaseType1):
    @property
    def address(self) -> str:
        return "nature"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class PokeathlonStat(BaseType1):
    @property
    def address(self) -> str:
        return "pokeathlon-stat"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class Pokemon(BaseType1):
    @property
    def address(self) -> str:
        return "pokemon"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class PokemonLocationArea(BaseType1):
    @property
    def address(self) -> str:
        return "pokemon"

    @property
    def url(self) -> str:
        return (
            f"https://pokeapi.co/api/v2/{self.address}/{self.id}/encounters"
            or f"https://pokeapi.co/api/v2/{self.address}{self.name}/encounters"
        )

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class PokemonColor(BaseType1):
    @property
    def address(self) -> str:
        return "pokemon-color"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class PokemonForm(BaseType1):
    @property
    def address(self) -> str:
        return "pokemon-form"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class PokemonHabitat(BaseType1):
    @property
    def address(self) -> str:
        return "pokemon-habitat"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class PokemonShape(BaseType1):
    @property
    def address(self) -> str:
        return "pokemon-shape"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class PokemonSpecies(BaseType1):
    @property
    def address(self) -> str:
        return "pokemon-species"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class Stat(BaseType1):
    @property
    def address(self) -> str:
        return "stat"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return


class Type(BaseType1):
    @property
    def address(self) -> str:
        return "type"

    @property
    def error(self) -> type:
        return PokemonNotFound

    @property
    def parsed_data(self) -> object:
        return
