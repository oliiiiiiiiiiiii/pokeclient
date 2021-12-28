from dataclasses import dataclass
from ..payload import DataPayload
from berry import Berry
from contest_type import ContestType
from ..utility.common_models import Name

@dataclass(frozen=True)
class FlavorBerryMap:

    data : DataPayload

    @property
    def potency(self):
        return self.data.get('potency')

    @property
    def berry(self):
        Berry(self.data.get('berry'))

        
@dataclass(frozen=True)
class BerryFlavor:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def names(self):
        return [Name(_) for _ in self.data.get('names')]

    @property
    def berries(self):
        return [FlavorBerryMap(_) for _ in self.data.get('berries')]

    @property
    def berries(self):
        return [ContestType(_) for _ in self.data.get('contest_type')]