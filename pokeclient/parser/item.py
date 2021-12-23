from dataclasses import dataclass
from payload import DataPayload
from ..utility.common_models import Name

@dataclass(frozen=True)
class ItemSprites:

    data : DataPayload

    @property
    def default(self):
        return self.data.get("default")

@dataclass(frozen=True)
class Item:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def cost(self):
        return self.data.get("cost")

    @property
    def fling_power(self):
        return self.data.get("fling_power")

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]