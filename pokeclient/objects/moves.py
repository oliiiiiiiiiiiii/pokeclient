from typing import Union
from dataclasses import dataclass
from ..url import base_url
import httpx

@dataclass(frozen=True)
class move:

    """Moves are the skills of Pokémon in battle.
    In battle, a Pokémon uses one move each turn.
    Some moves (including those learned by Hidden Machine)
    can be used outside of battle as well, usually for the
    purpose of removing obstacles or exploring new areas."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class move_ailment:

    """Move Ailments are status conditions
    caused by moves used during battle."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-ailment/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class move_battle_style:

    """Styles of moves when used in the Battle Palace."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-battle-style/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class move_category:

    """Very general categories that loosely
    group move effects."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-category/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class move_damage_class:

    """Damage classes moves can have,
    e.g. physical, special, or non-damaging."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-damage-class/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class move_learn_method:

    """Methods by which Pokémon can learn moves."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-learn-method/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class move_target:

    """Targets moves can be directed at during battle.
    Targets can be Pokémon, environments
    or even other moves."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-target/{self.name_or_id}"

    @property
    def raw_data(self) -> int:
        return httpx.get(self.url).json()