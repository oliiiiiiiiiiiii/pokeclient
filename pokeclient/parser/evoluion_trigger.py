from dataclasses import dataclass
from payload import DataPayload

@dataclass(frozen=True)
class EvolutionTrigger:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def id(self):
        return self.data.get('name')

'''
TODO :
names
pokemon_species
'''  