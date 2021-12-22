from dataclasses import dataclass
from payload import DataPayload


@dataclass(frozen=True)
class BerryFirmness:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def names(self):
        return self.data.get('names')

"""
Todo : 
berries
"""