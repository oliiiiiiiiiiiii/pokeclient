from dataclasses import dataclass
from payload import DataPayload
from ..utility.common_models import Name
from item import Item
from item_pocket import ItemPocket

@dataclass(frozen=True)
class ItemCategory:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def name(self):
        return ItemPocket(self.data.get("name"))

    @property
    def items(self):
        return [Item(_) for _ in self.data.get("items")]

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]