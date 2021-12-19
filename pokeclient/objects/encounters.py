from typing import Union
from dataclasses import dataclass
import httpx
import json
from ..url import base_url
from ..cache import Encounters
from ..errors import EncounterNotFound
from typing import Any


EncounterCache = Encounters()

@dataclass(frozen=True)
class EncounterMethod:

    """Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}encounter-method/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise EncounterNotFound(self.name_or_id)
            else:
                EncounterCache.add_encounter_method(data.get('id'), data)
                EncounterCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = EncounterCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise EncounterNotFound(self.name_or_id)
                        else:
                            EncounterCache.encounter_method(data.get('id'), data)
                            EncounterCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise EncounterNotFound(self.name_or_id)
                return
        data = EncounterCache.encounter_method.get(id)
        return data

@dataclass(frozen=True)
class EncounterCondition:

    """Conditions which affect what pokemon might appear in the wild, e.g., day or night."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}encounter-condition/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise EncounterNotFound(self.name_or_id)
            else:
                EncounterCache.add_encounter_condition(data.get('id'), data)
                EncounterCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = EncounterCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise EncounterNotFound(self.name_or_id)
                        else:
                            EncounterCache.encounter_condition(data.get('id'), data)
                            EncounterCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise EncounterNotFound(self.name_or_id)
                return
        data = EncounterCache.encounter_condition.get(id)
        return data

@dataclass(frozen=True)
class EncounterConditionValue:

    """Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}encounter-condition-value/{self.name_or_id}"
        
    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise EncounterNotFound(self.name_or_id)
            else:
                EncounterCache.add_encounter_condition_value(data.get('id'), data)
                EncounterCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = EncounterCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise EncounterNotFound(self.name_or_id)
                        else:
                            EncounterCache.encounter_condition_value(data.get('id'), data)
                            EncounterCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise EncounterNotFound(self.name_or_id)
                return
        data = EncounterCache.encounter_condition_value.get(id)
        return data