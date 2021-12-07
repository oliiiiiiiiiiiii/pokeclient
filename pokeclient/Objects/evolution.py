from typing import Union
import attr
from url import base_url

@attr.s(frozen=True)
class evolution_chain:

    """Evolution chains are essentially family trees.
    They start with the lowest
    stage within a family and detail evolution
    conditions for each as well as
    Pokémon they can evolve into up through the hierarchy."""

    def __init__(self, id: int) -> None:
        object.__setattr__(self,'name_or_id',id)

    @property
    def url(self):
        return f"{base_url}evolution-chain/{self.id}"


@attr.s(frozen=True)
class evolution_trigger:

    """Evolution triggers are the events and
    conditions that cause a Pokémon to evolve."""

    def __init__(self, id: int) -> None:
        object.__setattr__(self,'name_or_id',id)

    @property
    def url(self):
        return f"{base_url}evolution-trigger/{self.id}"

@attr.s(frozen=True)
class evolution:

    def __init__(self, id: int) -> None:
        object.__setattr__(self,'name_or_id',id)
