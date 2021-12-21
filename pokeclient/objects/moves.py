from typing import Union, Any
from dataclasses import dataclass
from ..url import base_url
from ..cache import Moves
from ..errors import MoveNotFound
import json
import httpx

MovesCache = Moves()

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MoveNotFound(self.name_or_id)
            else:
                MovesCache.add_move(data.get('id'), data)
                MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MovesCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MoveNotFound(self.name_or_id)
                        else:
                            MovesCache.add_move(data.get('id'), data)
                            MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MoveNotFound(self.name_or_id)
                return
        data = MovesCache.moves.get(id)
        return data

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MoveNotFound(self.name_or_id)
            else:
                MovesCache.add_move_ailment(data.get('id'), data)
                MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MovesCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MoveNotFound(self.name_or_id)
                        else:
                            MovesCache.add_move_ailment(data.get('id'), data)
                            MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MoveNotFound(self.name_or_id)
                return
        data = MovesCache.move_ailments.get(id)
        return data

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MoveNotFound(self.name_or_id)
            else:
                MovesCache.add_move_battle_style(data.get('id'), data)
                MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MovesCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MoveNotFound(self.name_or_id)
                        else:
                            MovesCache.add_move_battle_style(data.get('id'), data)
                            MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MoveNotFound(self.name_or_id)
                return
        data = MovesCache.move_battle_styles.get(id)
        return data

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MoveNotFound(self.name_or_id)
            else:
                MovesCache.add_move_category(data.get('id'), data)
                MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MovesCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MoveNotFound(self.name_or_id)
                        else:
                            MovesCache.add_move_category(data.get('id'), data)
                            MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MoveNotFound(self.name_or_id)
                return
        data = MovesCache.move_categories.get(id)
        return data

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MoveNotFound(self.name_or_id)
            else:
                MovesCache.add_move_damage_class(data.get('id'), data)
                MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MovesCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MoveNotFound(self.name_or_id)
                        else:
                            MovesCache.add_move_damage_class(data.get('id'), data)
                            MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MoveNotFound(self.name_or_id)
                return
        data = MovesCache.move_damage_classes.get(id)
        return data

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MoveNotFound(self.name_or_id)
            else:
                MovesCache.add_move_learn_method(data.get('id'), data)
                MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MovesCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MoveNotFound(self.name_or_id)
                        else:
                            MovesCache.add_move_learn_method(data.get('id'), data)
                            MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MoveNotFound(self.name_or_id)
                return
        data = MovesCache.move_learn_methods.get(id)
        return data

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
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise MoveNotFound(self.name_or_id)
            else:
                MovesCache.add_move_target(data.get('id'), data)
                MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = MovesCache.name_to_id_dict.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise MoveNotFound(self.name_or_id)
                        else:
                            MovesCache.add_move_target(data.get('id'), data)
                            MovesCache.name_to_id_dict[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise MoveNotFound(self.name_or_id)
                return
        data = MovesCache.move_targets.get(id)
        return data