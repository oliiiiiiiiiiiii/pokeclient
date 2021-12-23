from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Name

@dataclass(frozen=True)
class EvolutionTrigger:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def id(self):
        return self.data.get('name')

    @property
    def names(self):
        return [Name(_) for _  in self.data.get('names')]

'''
TODO :
pokemon_species
'''  