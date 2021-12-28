from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Name
from version_group import VersionGroup

@dataclass(frozen=True)
class Version:

    data : DataPayload

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def name(self):
        return [Name(_) for _ in self.data.get('name')]

    @property
    def version_group(self):
        return [VersionGroup(_) for _ in self.data.get('version_group')]