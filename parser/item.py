from dataclasses import dataclass
from payload import DataPayload
from ..utility.common_models import Name
from evolution_chain import EvolutionChain
from item_category import ItemCategory
from version import Version
from item_fling_effect import ItemFlingEffect
from item_attribute import ItemAttribute
@dataclass(frozen=True)
class ItemHolderPokemonVersionDetail:

    data : DataPayload

    @property
    def rarity(self):
        return self.data.get("rarity")

    @property
    def version(self):
        return Version(self.data.get("version"))

@dataclass(frozen=True)
class ItemHolderPokemon:

    data : DataPayload

    @property
    def pokemon(self):
        return self.data.get("pokemon")

    @property
    def version_details(self):
        return ItemHolderPokemonVersionDetail(self.data.get("version_details"))

@dataclass(frozen=True)
class ItemSprite:

    data : DataPayload

    @property
    def default(self):
        return self.data.get("default")


@dataclass(frozen=True)
class Item:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def cost(self):
        return self.data.get("cost")

    @property
    def fling_power(self):
        return self.data.get("fling_power")

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]

    @property
    def sprites(self):
        return ItemSprite(self.data.get("sprites"))

    @property
    def baby_trigger_for(self):
        return EvolutionChain(self.data.get("baby_trigger_for"))

    @property
    def category(self):
        return ItemCategory(self.data.get("category"))

    @property
    def held_by_pokemon(self):
        return ItemHolderPokemon(self.data.get("held_by_pokemon"))

    @property
    def fling_effect(self):
        return ItemFlingEffect(self.data.get("fling_effect"))

    @property
    def attributes(self):
        return [ItemAttribute(_) for _ in self.data.get("attributes")]

    @property
    def machines(self):
        return [_ for _ in self.data.get("machines")]

    @property
    def effect_entries(self):
        return [_ for _ in self.data.get("effect_entries")]

    @property
    def flavor_text_entries(self):
        return [_ for _ in self.data.get("flavor_text_entries")]

    @property
    def game_indices(self):
        return [_ for _ in self.data.get("game_indices")]