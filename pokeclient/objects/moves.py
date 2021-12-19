from typing import Union, Any
from dataclasses import dataclass
from ..url import base_url
import httpx

@dataclass(frozen=True)
class Move:

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
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class MoveAilment:

    """Move Ailments are status conditions
    caused by moves used during battle."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-ailment/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class MoveBattleStyle:

    """Styles of moves when used in the Battle Palace."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-battle-style/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class MoveCategory:

    """Very general categories that loosely
    group move effects."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-category/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class MoveDamageClass:

    """Damage classes moves can have,
    e.g. physical, special, or non-damaging."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-damage-class/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class MoveLearnMethod:

    """Methods by which Pokémon can learn moves."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-learn-method/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()

@dataclass(frozen=True)
class MoveTarget:

    """Targets moves can be directed at during battle.
    Targets can be Pokémon, environments
    or even other moves."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}move-target/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        return httpx.get(self.url).json()