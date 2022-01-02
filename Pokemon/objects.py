from base import BaseType1, BaseType2


class Berry(BaseType1):
    @property
    def address(self) -> str:
        return "berry/"

    @property
    def parsed_data(self) -> object:
        return


class BerryFirmness(BaseType1):
    @property
    def address(self) -> str:
        return "berry-firmness/"

    @property
    def parsed_data(self) -> object:
        return


class BerryFlavour(BaseType1):
    @property
    def address(self) -> str:
        return "berry-flavour/"

    @property
    def parsed_data(self) -> object:
        return


class ContestType(BaseType1):
    @property
    def address(self) -> str:
        return "contest-type/"

    @property
    def parsed_data(self) -> object:
        return


class ContestEffect(BaseType2):
    @property
    def address(self) -> str:
        return "contest-effect/"

    @property
    def parsed_data(self) -> object:
        return


class SuperContestEffect(BaseType2):
    @property
    def address(self) -> str:
        return "super-contest-effect/"

    @property
    def parsed_data(self) -> object:
        return


class EncounterMethod(BaseType1):
    @property
    def address(self) -> str:
        return "encounter-method/"

    @property
    def parsed_data(self) -> object:
        return


class EncounterCondition(BaseType1):
    @property
    def address(self) -> str:
        return "encounter-condition/"

    @property
    def parsed_data(self) -> object:
        return


class EncounterConditionValue(BaseType1):
    @property
    def address(self) -> str:
        return "encounter-condition-value/"

    @property
    def parsed_data(self) -> object:
        return


class EvolutionChain(BaseType2):
    @property
    def address(self) -> str:
        return "evolution-chain/"

    @property
    def parsed_data(self) -> object:
        return


class EvolutionTrigger(BaseType2):
    @property
    def address(self) -> str:
        return "evolution-trigger/"

    @property
    def parsed_data(self) -> object:
        return


class Generation(BaseType1):
    @property
    def address(self) -> str:
        return "generation/"

    @property
    def parsed_data(self) -> object:
        return


class Pokedex(BaseType1):
    @property
    def address(self) -> str:
        return "pokedex/"

    @property
    def parsed_data(self) -> object:
        return


class Version(BaseType1):
    @property
    def address(self) -> str:
        return "version/"

    @property
    def parsed_data(self) -> object:
        return


class VersionGroup(BaseType1):
    @property
    def address(self) -> str:
        return "version-group/"

    @property
    def parsed_data(self) -> object:
        return


class ItemAttribute(BaseType1):
    @property
    def address(self) -> str:
        return "item-attribute/"

    @property
    def parsed_data(self) -> object:
        return


class ItemCategory(BaseType1):
    @property
    def address(self) -> str:
        return "item-category/"

    @property
    def parsed_data(self) -> object:
        return


class ItemFlingEffect(BaseType1):
    @property
    def address(self) -> str:
        return "item-fling-effect/"

    @property
    def parsed_data(self) -> object:
        return


class Item(BaseType1):
    @property
    def address(self) -> str:
        return "item/"

    @property
    def parsed_data(self) -> object:
        return


class Location(BaseType1):
    @property
    def address(self) -> str:
        return "location/"

    @property
    def parsed_data(self) -> object:
        return


class LocationArea(BaseType1):
    @property
    def address(self) -> str:
        return "location-area/"

    @property
    def parsed_data(self) -> object:
        return


class PalParkArea(BaseType1):
    @property
    def address(self) -> str:
        return "pal-park-area/"

    @property
    def parsed_data(self) -> object:
        return


class Region(BaseType1):
    @property
    def address(self) -> str:
        return "region/"

    @property
    def parsed_data(self) -> object:
        return


class Machine(BaseType2):
    @property
    def address(self) -> str:
        return "machine/"

    @property
    def parsed_data(self) -> object:
        return
