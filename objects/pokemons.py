from typing import Union, Any
from dataclasses import dataclass
from ..url import base_url
from ..cache import Pokemons
from ..errors import PokemonNotFound
import json
import httpx

PokemonsCache = Pokemons()

@dataclass(frozen=True)
class Ability:

    """Abilities provide passive effects for
    Pokémon in battle or in the overworld.
    Pokémon have multiple possible abilities
    but can have only one ability at a time."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}ability/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_ability(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_ability(data.get('id'), data)
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.abilities.get(id)
        return data

@dataclass(frozen=True)
class Characteristic:

    """Characteristics indicate which
    stat contains a Pokémon's highest IV.
    A Pokémon's Characteristic is determined
    by the remainder of its highest IV
    divided by 5 (gene_modulo)."""

    id: int
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}characteristic/{self.id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.id)
            else:
                PokemonsCache.add_characteristic(data.get('id'), data)
                return data
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise PokemonNotFound(self.id)
                    else:
                        PokemonsCache.add_characteristic(data.get('id'), data)
                        return data
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise PokemonNotFound(self.id)
        data = PokemonsCache.characteristics.get(id)
        return data

@dataclass(frozen=True)
class Gender:

    """Genders were introduced in Generation II
    for the purposes of breeding
    Pokémon but can also result in visual differences
    or even different evolutionary lines."""

    id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}gender/{self.id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.id)
            else:
                PokemonsCache.add_gender(data.get('id'), data)
                return data
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise PokemonNotFound(self.id)
                    else:
                        PokemonsCache.add_gender(data.get('id'), data)
                        return data
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise PokemonNotFound(self.id)
        data = PokemonsCache.genders.get(id)
        return data

@dataclass(frozen=True)
class GrowthRate:

    """Growth rates are the speed with which
    Pokémon gain levels through experience."""

    id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}gender/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.id)
            else:
                PokemonsCache.add_growth_rate(data.get('id'), data)
                return data
        else:
            if isinstance(self.id, str):
                try:
                    id = int(self.id)
                except ValueError:
                    try:
                        data = httpx.get(self.url).json()
                    except json.decoder.JSONDecodeError:
                        raise PokemonNotFound(self.id)
                    else:
                        PokemonsCache.add_growth_rate(data.get('id'), data)
                        return data
            elif isinstance(self.id, int):
                id = self.id
            else:
                raise PokemonNotFound(self.id)
        data = PokemonsCache.growth_rates.get(id)
        return data

@dataclass(frozen=True)
class Nature:

    """Natures influence how a Pokémon's stats grow."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}nature/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_nature(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_nature(data.get('id'), data)
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.natures.get(id)
        return data

@dataclass(frozen=True)
class PokeathlonStat:

    """Pokeathlon Stats are different attributes of
    a Pokémon's performance in Pokéathlons.
    In Pokéathlons, competitions happen on different courses;
    one for each of the different Pokéathlon stats."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokeathlon-stat/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokeathlon_stat(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokeathlon_stat(data.get('id'), data)
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokeathlon_stats.get(id)
        return data

@dataclass(frozen=True)
class Pokemon:

    """Pokémon are the creatures that
    inhabit the world of the Pokémon games.
    They can be caught using Pokéballs
    and trained by battling with other Pokémon.
    Each Pokémon belongs to a specific
    species but may take on a
    variant which makes it differ from
    other Pokémon of the same species,
    such as base stats, available abilities and typings."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokemon/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokemon(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokemon(data.get('id'), data)
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokemons.get(id)
        return data

@dataclass(frozen=True)
class PokemonLocationArea:

    """Pokémon Location Areas are ares where Pokémon can be found."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokemon/{self.name_or_id}/encounters"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokemon_location_area(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokemon_location_area(data.get('id'), data)
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokemon_location_areas.get(id)
        return data

@dataclass(frozen=True)
class PokemonColor:

    """Colors used for sorting Pokémon in a Pokédex.
    The color listed in the Pokédex is usually the
    color most apparent or covering each Pokémon's body.
    No orange category exists; Pokémon that are primarily
    orange are listed as red or brown."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-color/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokemon_color(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokemon_color((data.get('id'), data))
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokemon_colors.get(id)
        return data

@dataclass(frozen=True)
class PokemonForm:

    """Some Pokémon may appear in
    one of multiple, visually different forms.
    These differences are purely cosmetic.
    For variations within a Pokémon species,
    which do differ in more than just visuals,
    the 'Pokémon' entity is used to
    represent such a variety."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-form/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokemon_form(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokemon_form((data.get('id'), data))
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokemon_forms.get(id)
        return data

@dataclass(frozen=True)
class PokemonHabitat:

    """Habitats are generally different
    terrain Pokémon can be
    found in but can also be areas
    designated for rare or legendary Pokémon."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-habitat/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokemon_habitat(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokemon_habitat((data.get('id'), data))
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokemon_habitats.get(id)
        return data

@dataclass(frozen=True)
class PokemonShape:

    """Shapes used for sorting Pokémon in a Pokédex."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-shape/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokemon_shape(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokemon_shape((data.get('id'), data))
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokemon_shapes.get(id)
        return data

@dataclass(frozen=True)
class PokemonSpecies:

    """A Pokémon Species forms the basis
    for at least one Pokémon.
    Attributes of a Pokémon species are shared across
    all varieties of Pokémon within the species.
    A good example is Wormadam; Wormadam is the
    species which can be found in three different varieties,
    Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-species/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_pokemon_species(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_pokemon_species((data.get('id'), data))
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.pokemon_species.get(id)
        return data

@dataclass(frozen=True)
class Stat:

    """Stats determine certain aspects of battles.
    Each Pokémon has a value for each stat
    which grows as they gain levels and can
    be altered momentarily by effects in battles."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}stat/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_stat(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_stat((data.get('id'), data))
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.stats.get(id)
        return data

@dataclass(frozen=True)
class Type:

    """Types are properties for Pokémon and their moves.
    Each type has three properties: which types of
    Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against."""

    name_or_id: Union[str, int]
    from_cache : bool = False

    @property
    def url(self) -> str:
        return f"{base_url}type/{self.name_or_id}"

    @property
    def raw_data(self) -> Any:
        if not self.from_cache:
            try:
                data = httpx.get(self.url).json()
            except json.decoder.JSONDecodeError:
                raise PokemonNotFound(self.name_or_id)
            else:
                PokemonsCache.add_type(data.get('id'), data)
                PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                return data
        else:
            if isinstance(self.name_or_id, str):
                try:
                    id = int(self.name_or_id)
                except ValueError:
                    try:
                        id = PokemonsCache.name_id_map.get(self.name_or_id).lower()
                    except AttributeError:
                        try:
                            data = httpx.get(self.url).json()
                        except json.decoder.JSONDecodeError:
                            raise PokemonNotFound(self.name_or_id)
                        else:
                            PokemonsCache.add_type((data.get('id'), data))
                            PokemonsCache.name_id_map[data.get('name')] = data.get('id')
                            return data
            elif isinstance(self.name_or_id, int):
                id = self.name_or_id
            else:
                raise PokemonNotFound(self.name_or_id)
        data = PokemonsCache.types.get(id)
        return data