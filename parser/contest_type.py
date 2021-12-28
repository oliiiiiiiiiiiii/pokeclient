from dataclasses import dataclass
from ..payload import DataPayload
from berry_flavor import BerryFlavor
from utility.languages import Language

@dataclass(frozen=True)
class ContestName:
    data : DataPayload

    @property
    def name(self):
        return self.data.get("name")

    @property
    def color(self):
        return self.data.get("color")

    @property
    def language(self):
        return Language(self.data.get("language"))


@dataclass(frozen=True)
class ContestType:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def names(self):
        return [ContestName(_) for _ in self.data.get("names")]

    @property
    def berry_flavor(self):
        return BerryFlavor(self.data.get('berry_flavor'))
