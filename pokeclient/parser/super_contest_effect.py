from dataclasses import dataclass
from ..payload import DataPayload


@dataclass(frozen=True)
class SuperContestEffect:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def appeal(self):
        return self.data.get('appeal')

'''
TODO :
flavor_text_entries
moves
'''