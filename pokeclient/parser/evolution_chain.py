from dataclasses import dataclass
from ..payload import DataPayload
from evoluion_trigger import EvolutionTrigger
from item import Item

@dataclass(frozen=True)
class EvolutionDetail:

    data : DataPayload

    @property
    def gender(self):
        return self.data.get('gender')

    @property
    def min_level(self):
        return self.data.get('min_level')

    @property
    def min_happiness(self):
        return self.data.get('min_happiness')

    @property
    def min_affection(self):
        return self.data.get('min_affection')    

    @property
    def needs_overworld_rain(self):
        return self.data.get('needs_overworld_rain')        

    @property
    def relative_physical_stats(self):
        return self.data.get('relative_physical_stats')

    @property
    def time_of_day(self):
        return self.data.get('time_of_day')

    @property
    def turn_upside_down(self):
        return self.data.get('turn_upside_down')

    @property
    def trigger(self):
        return [EvolutionTrigger(_) for _ in self.data.get('trigger')]

    @property
    def item(self):
        return Item(self.data.get('item'))

    @property
    def held_item(self):
        return Item(self.data.get('held_item'))

    '''
    TODO : 
    known_move
    known_move_type
    location
    party_species
    party_type
    trade_species
    '''

@dataclass(frozen=True)
class ChainLink:

    data : DataPayload

    @property
    def is_baby(self):
        return self.data.get('is_baby')

    @property
    def evolution_details(self):
        return [EvolutionDetail(_) for _ in self.data.get('evolution_details')]

    @property
    def evolves_to(self):
        return self.data.get('evolves_to')

    '''
    TODO :
    species
    '''


@dataclass(frozen=True)
class EvolutionChain:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def chain(self):
        return ChainLink(self.data.get('chain'))