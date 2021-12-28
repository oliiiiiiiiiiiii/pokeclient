from dataclasses import dataclass
from payload import DataPayload
from ..utility.common_models import Name
from item_category import ItemCategory

@dataclass(frozen=True)
class ItemPocket:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def categories(self):
        return [ItemCategory(_) for _ in self.data.get("categories")]

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]