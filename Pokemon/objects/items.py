from typing import Union, Any
from dataclasses import dataclass
import httpx
import json
from ..url import base_url
from ..cache import Items
from ..errors import ItemNotFound

ItemCache = Items()

@dataclass(frozen=True)
class ItemAttribute:

    """An item is an object in the games which the
    player can pick up, keep in their bag, and use
    in some manner. They have various uses,
    including healing, powering up,
    helping catch Pokémon, or to access a new area."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}item-attribute/{self.name_or_id}/"


    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ItemNotFound(self.name_or_id)
            else:
                ItemCache.add_item_attribute(data.get('id'), data)
                ItemCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ItemCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ItemNotFound(self.name_or_id)
                        else:
                            ItemCache.add_item_attribute(data.get('id'), data)
                            ItemCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ItemNotFound(self.name_or_id)
        data = ItemCache.item_attributes.get(id)
        return data
@dataclass(frozen=True)
class ItemCategory:

    """Item categories determine where
    items will be placed in the players bag."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}item-category/{self.name_or_id}/"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ItemNotFound(self.name_or_id)
            else:
                ItemCache.add_item_category(data.get('id'), data)
                ItemCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ItemCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ItemNotFound(self.name_or_id)
                        else:
                            ItemCache.add_item_category(data.get('id'), data)
                            ItemCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ItemNotFound(self.name_or_id)
        data = ItemCache.item_categories.get(id)
        return data

@dataclass(frozen=True)
class ItemFlingEffect:

    """The various effects of the move
    "Fling" when used with different items."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}item-fling-effect/{self.name_or_id}/"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ItemNotFound(self.name_or_id)
            else:
                ItemCache.add_item_fling_effect(data.get('id'), data)
                ItemCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ItemCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ItemNotFound(self.name_or_id)
                        else:
                            ItemCache.add_item_fling_effect(data.get('id'), data)
                            ItemCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ItemNotFound(self.name_or_id)
        data = ItemCache.item_fling_effects.get(id)
        return data

@dataclass(frozen=True)
class ItemPocket:

    """Pockets within the
    players bag used for storing items by category."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}item-pocket/{self.name_or_id}/"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ItemNotFound(self.name_or_id)
            else:
                ItemCache.add_item_pocket(data.get('id'), data)
                ItemCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ItemCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ItemNotFound(self.name_or_id)
                        else:
                            ItemCache.add_item_pocket(data.get('id'), data)
                            ItemCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ItemNotFound(self.name_or_id)
        data = ItemCache.item_pockets.get(id)
        return data

@dataclass(frozen=True)
class Item:

    """An item is an object in the games which
    the player can pick up, keep in their bag,
    and use in some manner.
    They have various uses, including healing, powering up,
    helping catch Pokémon, or to access a new area."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self):
        return f"{base_url}item/{self.name_or_id}/"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise ItemNotFound(self.name_or_id)
            else:
                ItemCache.add_item(data.get('id'), data)
                ItemCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = ItemCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise ItemNotFound(self.name_or_id)
                        else:
                            ItemCache.add_item(data.get('id'), data)
                            ItemCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise ItemNotFound(self.name_or_id)
        data = ItemCache.items.get(id)
        return data