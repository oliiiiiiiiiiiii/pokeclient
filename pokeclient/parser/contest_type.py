from dataclasses import dataclass
from payload import DataPayload

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
        return self.data.get("language")


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

"""
TODO : 
berry_flavor
"""