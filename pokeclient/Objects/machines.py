from typing import Union
from dataclasses import dataclass
from url import base_url


@dataclass(frozen=True)
class machine:

    """Machines are the representation of items that
    teach moves to Pokémon. They vary from version to version, so it is not certain that one
    specific TM or HM corresponds to a single Machine."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}machine/{self.name_or_id}"
