from typing import Union
import attr
from url import base_url


@attr.s(frozen=True)
class evolution:
    def __init__(self, id: int) -> None:
        self.id = id


@attr.s(frozen=True)
class evolution_chain(evolution):

    """Evolution chains are essentially family trees.
    They start with the lowest
    stage within a family and detail evolution
    conditions for each as well as
    Pokémon they can evolve into up through the hierarchy."""

    def __init__(self, id: int) -> None:
        super().__init__(id)

    @property
    def url(self):
        return f"{base_url}evolution-chain/{self.id}"


@attr.s(frozen=True)
class evolution_trigger(evolution):

    """Evolution triggers are the events and
    conditions that cause a Pokémon to evolve."""

    def __init__(self, id: int) -> None:
        super().__init__(id)

    @property
    def url(self):
        return f"{base_url}evolution-trigger/{self.id}"
