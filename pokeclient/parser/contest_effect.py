from dataclasses import dataclass
from payload import DataPayload

@dataclass(frozen=True)
class ContestEffect:
    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def appeal(self):
        return self.data.get('appeal')

    @property
    def jam(self):
        return self.data.get('jam')

'''
TODO :
effect_entries
flavor_text_entries
'''