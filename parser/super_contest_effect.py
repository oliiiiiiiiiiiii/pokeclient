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

    @property
    def flavor_text_entries(self):
        return [_ for _ in self.data.get('flavor_text_entries')]

    @property
    def moves(self):
        return [_ for _ in self.data.get('moves')]