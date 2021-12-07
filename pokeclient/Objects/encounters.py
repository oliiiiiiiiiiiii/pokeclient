from typing import Union
import attr
from url import base_url


@attr.s(frozen=True)
class encounter_method:

    """Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self):
        return f"{base_url}encounter-method/{self.name_or_id}"


@attr.s(frozen=True)
class encounter_condition:

    """Conditions which affect what pokemon might appear in the wild, e.g., day or night."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self):
        return f"{base_url}encounter-condition/{self.name_or_id}"


@attr.s(frozen=True)
class encounter_condition_values:

    """Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night."""

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)

    @property
    def url(self):
        return f"{base_url}encounter-condition-value/{self.name_or_id}"

@attr.s(frozen=True)
class encounter:

    def __init__(self, name_or_id: Union[str, int]) -> None:
        object.__setattr__(self,'name_or_id',name_or_id)