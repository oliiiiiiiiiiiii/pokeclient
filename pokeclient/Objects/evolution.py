from typing import Union
from dataclasses import dataclass
from url import base_url


@dataclass(frozen=True)
class evolution_chain:

    """Evolution chains are essentially family trees.
    They start with the lowest
    stage within a family and detail evolution
    conditions for each as well as
    Pokémon they can evolve into up through the hierarchy."""

    id: int

    @property
    def url(self) -> str:
        return f"{base_url}evolution-chain/{self.id}"


@dataclass(frozen=True)
class evolution_trigger:

    """Evolution triggers are the events and
    conditions that cause a Pokémon to evolve."""

    id: int

    @property
    def url(self) -> str:
        return f"{base_url}evolution-trigger/{self.id}"
