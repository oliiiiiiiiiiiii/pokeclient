from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Name
from encounter_condition_value import EncounterConditionValue

@dataclass(frozen=True)
class EncounterCondition:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]

    @property
    def values(self):
        return [EncounterConditionValue(_) for _ in self.data.get("values")]