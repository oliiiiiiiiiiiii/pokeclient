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

    name_or_id: Union[str, int]
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
                raise MachineNotFound(self.name_or_id)
            else:
                MachineCache.add_machine(data.get('id'), data)
                MachineCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MachineCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MachineNotFound(self.name_or_id)
                        else:
                            MachineCache.add_machine(data.get('id'), data)
                            MachineCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MachineNotFound(self.name_or_id)
        data = MachineCache.machines.get(id)
        return data