from dataclasses import dataclass
from common_models import Name

@dataclass
class Language:
    id:int
    name:str
    official:bool
    iso639:str
    iso3166:str
    names:Name