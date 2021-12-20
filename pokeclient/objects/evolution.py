from typing import Any
from dataclasses import dataclass
from ..url import base_url
import httpx

@dataclass(frozen=True)
class EvolutionChain:

    """Evolution chains are essentially family trees.
    They start with the lowest
    stage within a family and detail evolution
    conditions for each as well as
    Pokémon they can evolve into up through the hierarchy."""

    id: int
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}evolution-chain/{self.id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class EvolutionTrigger:

    """Evolution triggers are the events and
    conditions that cause a Pokémon to evolve."""

    id: int
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}evolution-trigger/{self.id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()