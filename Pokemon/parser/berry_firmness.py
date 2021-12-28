from dataclasses import dataclass
from ..payload import DataPayload
from berry import Berry
from ..utility.common_models import Name

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
        return [Name(_) for _ in self.data.get('names')]

    @property
    def berries(self):
        return [Berry(_) for _ in self.data.get('berries')]
