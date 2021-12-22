from dataclasses import dataclass
from payload import DataPayload


@dataclass(frozen=True)
class Berry:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def growth_time(self):
        return self.data.get("growth_time")

    @property
    def max_harvest(self):
        return self.data.get("max_harvest")

    @property
    def natural_gift_power(self):
        return self.data.get("natural_gift_power")

    @property
    def size(self):
        return self.data.get("size")

    @property
    def smoothness(self):
        return self.data.get("smoothness")

    @property
    def soil_dryness(self):
        return self.data.get("soil_dryness")

"""
TODO : 
firmness
flavors
item
natural_gift_type
"""