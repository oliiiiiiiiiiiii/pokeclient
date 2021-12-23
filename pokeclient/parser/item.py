from dataclasses import dataclass
from payload import DataPayload
from ..utility.common_models import Name
from evolution_chain import EvolutionChain

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


'''
TODO:
fling_effect
attributes
category
effect_entries
flavor_text_entries
game_indices
held_by_pokemon
machines
'''