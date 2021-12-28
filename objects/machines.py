from typing import Union, Any
from dataclasses import dataclass
from ..url import base_url
from ..cache import Machines
from ..errors import MachineNotFound
import json
import httpx

MachineCache = Machines()

@dataclass(frozen=True)
class Machine:

    """Machines are the representation of items that
    teach moves to Pokémon. They vary from version to version, so it is not certain that one
    specific TM or HM corresponds to a single Machine."""

    id : int
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}machine/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MachineNotFound(self.id)
            else:
                MachineCache.add_machine(data.get('id'), data)
                return data 
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise MachineNotFound(self.id)
                    else:
                        MachineCache.add_machine(data.get('id'), data)
                        return data 
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise MachineNotFound(self.id)
        data = MachineCache.machines.get(id)
        return data 