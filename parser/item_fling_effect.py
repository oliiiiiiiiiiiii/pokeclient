from dataclasses import dataclass
from payload import DataPayload
from item import Item

@dataclass(frozen=True)
class ItemFlingEffect:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def items(self):
        return [Item(_) for _ in self.data.get("items")]

    @property
    def effect_entries(self):
        return [_ for _ in self.data.get("effect_entries")]