from typing import Dict,Any
from dataclasses import dataclass
from common_models import Name
from ..base import DataPayload

@dataclass
class Language:

    data:Dict[str, Any]

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")   

    @property
    def official(self):
        return self.data.get("official")  

    @property
    def iso639(self):
        return self.data.get("iso639")  

    @property
    def iso3166(self):
        return self.data.get("iso3166") 

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]