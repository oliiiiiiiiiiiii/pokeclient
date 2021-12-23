from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Name
from encounter_condition import EncounterCondition

@dataclass(frozen=True)
class EncounterConditionValue:

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
    def condition(self):
        return EncounterCondition(self.data.get("condition"))