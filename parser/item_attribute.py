from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Description, Name
from item import Item

@dataclass(frozen=True)
class ItemAttribute:

    data:DataPayload

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
    def names(self):
        return [Name(_) for _ in self.data.get("names")]

    @property
    def names(self):
        return [Description(_) for _ in self.data.get("descriptions")]