from dataclasses import dataclass
from ..payload import DataPayload
from item import Item
from version_group import VersionGroup

@dataclass(frozen=True)
class Machine:

    data:DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def item(self):
        return Item(self.data.get('item'))

    @property
    def version_group(self):
        return VersionGroup(self.data.get('version_group'))

'''
TODO:
move
'''