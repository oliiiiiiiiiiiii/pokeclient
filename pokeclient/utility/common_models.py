from dataclasses import dataclass
from languages import Language
from ..payload import DataPayload


@dataclass
class APIResource:

    data:DataPayload

    @property
    def url(self):
        return self.data.get("url")

@dataclass
class Description:

    data:DataPayload

    @property
    def description(self):
        return self.data.get("description")

    @property
    def language(self):
        return Language(self.data.get("language"))

@dataclass
class Effect:
    data:DataPayload

    @property
    def language(self):
        return Language(self.data.get("language"))

    @property
    def effect(self):
        return self.data.get("effect")

@dataclass
class Encounter:
    min_level:int
    max_level:int
    chance:int
    data:DataPayload

    @property
    def chance(self):
        return self.data.get("chance")

    @property
    def effect(self):
        return self.data.get("effect")

    '''
    TODO:
    condition_values
    method
    '''

@dataclass
class FlavorText:
    data:DataPayload

    @property
    def flavor_text(self):
        return self.data.get("chance")

    @property
    def name(self):
        return Language(self.data.get("name"))
    '''
    TODO:
    version
    '''    

@dataclass
class GenerationGameIndex:
    data:DataPayload

    @property
    def game_index(self):
        return self.data.get("game_index")

    '''
    TODO:
    generation
    '''    

@dataclass
class MachineVersionDetail:
    data:DataPayload
    '''
    TODO:
    machine
    version_group
    '''    


@dataclass
class Name:
    data:DataPayload

    @property
    def name(self):
        return self.data.get("name")

    @property
    def language(self):
        return Language(self.data.get("language"))