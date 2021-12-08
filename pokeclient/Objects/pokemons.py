from typing import Union
from dataclasses import dataclass
from url import base_url


@dataclass(frozen=True)
class ability:

    """Abilities provide passive effects for
    Pokémon in battle or in the overworld.
    Pokémon have multiple possible abilities
    but can have only one ability at a time."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}ability/{self.name_or_id}"


@dataclass(frozen=True)
class characteristic:

    """Characteristics indicate which
    stat contains a Pokémon's highest IV.
    A Pokémon's Characteristic is determined
    by the remainder of its highest IV
    divided by 5 (gene_modulo)."""

    id: int

    @property
    def url(self) -> str:
        return f"{base_url}characteristic/{self.id}"


@dataclass(frozen=True)
class gender:

    """Genders were introduced in Generation II
    for the purposes of breeding
    Pokémon but can also result in visual differences
    or even different evolutionary lines."""

    id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}gender/{self.id}"


@dataclass(frozen=True)
class gender:

    """Growth rates are the speed with which
    Pokémon gain levels through experience."""

    id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}gender/{self.name_or_id}"


@dataclass(frozen=True)
class nature:

    """Natures influence how a Pokémon's stats grow."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}nature/{self.name_or_id}"


@dataclass(frozen=True)
class pokeathlon_stat:

    """Pokeathlon Stats are different attributes of
    a Pokémon's performance in Pokéathlons.
    In Pokéathlons, competitions happen on different courses;
    one for each of the different Pokéathlon stats."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokeathlon-stat/{self.name_or_id}"


@dataclass(frozen=True)
class pokemon:

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

    @property
    def url(self) -> str:
        return f"{base_url}pokemon/{self.name_or_id}"


@dataclass(frozen=True)
class pokemon_location_area:

    """Pokémon Location Areas are ares where Pokémon can be found."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokemon/{self.name_or_id}/encounters"


@dataclass(frozen=True)
class pokemon_color:

    """Colors used for sorting Pokémon in a Pokédex.
    The color listed in the Pokédex is usually the
    color most apparent or covering each Pokémon's body.
    No orange category exists; Pokémon that are primarily
    orange are listed as red or brown."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-color/{self.name_or_id}"


@dataclass(frozen=True)
class pokemon_form:

    """Some Pokémon may appear in
    one of multiple, visually different forms.
    These differences are purely cosmetic.
    For variations within a Pokémon species,
    which do differ in more than just visuals,
    the 'Pokémon' entity is used to
    represent such a variety."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-form/{self.name_or_id}"


@dataclass(frozen=True)
class pokemon_habitat:

    """Habitats are generally different
    terrain Pokémon can be
    found in but can also be areas
    designated for rare or legendary Pokémon."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-habitat/{self.name_or_id}"


@dataclass(frozen=True)
class pokemon_shape:

    """Shapes used for sorting Pokémon in a Pokédex."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-shape/{self.name_or_id}"


@dataclass(frozen=True)
class pokemon_species:

    """A Pokémon Species forms the basis
    for at least one Pokémon.
    Attributes of a Pokémon species are shared across
    all varieties of Pokémon within the species.
    A good example is Wormadam; Wormadam is the
    species which can be found in three different varieties,
    Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}pokemon-species/{self.name_or_id}"


@dataclass(frozen=True)
class stat:

    """Stats determine certain aspects of battles.
    Each Pokémon has a value for each stat
    which grows as they gain levels and can
    be altered momentarily by effects in battles."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}stat/{self.name_or_id}"


@dataclass(frozen=True)
class Type:

    """Types are properties for Pokémon and their moves.
    Each type has three properties: which types of
    Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against."""

    name_or_id: Union[str, int]

    @property
    def url(self) -> str:
        return f"{base_url}type/{self.name_or_id}"
