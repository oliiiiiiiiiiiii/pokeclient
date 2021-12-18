from typing import Union
from dataclasses import dataclass
from ..url import base_url
import httpx

@dataclass(frozen=True)
class EncounterMethod:

    """Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}encounter-method/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class EncounterCondition:

    """Conditions which affect what pokemon might appear in the wild, e.g., day or night."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}encounter-condition/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class EncounterConditionValue:

    """Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}encounter-condition-value/{self.name_or_id}"
        
    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()