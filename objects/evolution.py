from typing import Any
from dataclasses import dataclass
import json
from ..url import base_url
from ..cache import Evolutions
from ..errors import EvolutionNotFound
import httpx

EvolutionCache = Evolutions()

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise EvolutionNotFound(self.id)
            else:
                EvolutionCache.add_evolution_chain(data.get('id'), data)
                return data 
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise EvolutionNotFound(self.id)
                    else:
                        EvolutionCache.add_evolution_chain(data.get('id'), data)
                        return data 
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise EvolutionNotFound(self.id)
        data = EvolutionCache.evolution_chains.get(id)
        return data 

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise EvolutionNotFound(self.id)
            else:
                EvolutionCache.add_evolution_trigger(data.get('id'), data)
                return data
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise EvolutionNotFound(self.id)
                    else:
                        EvolutionCache.add_evolution_trigger(data.get('id'), data)
                        return data
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise EvolutionNotFound(self.id)
        data = EvolutionCache.evolution_triggers.get(id)
        return data