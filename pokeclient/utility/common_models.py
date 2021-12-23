from dataclasses import dataclass
from languages import Language
from ..parser
@dataclass
class APIResource:
    url:str

@dataclass
class Description:
    description:str
    language:Language

@dataclass
class Effect:
    effect:str
    language:Language

@dataclass
class Encounter:
    min_level:int
    max_level:int
    chance:int
    '''
    TODO:
    condition_values
    method
    '''

@dataclass
class FlavorText:
    flavor_text:str
    language:Language
    '''
    TODO:
    version
    '''    

@dataclass
class GenerationGameIndex:
    game_index:str
    '''
    TODO:
    generation
    '''    

@dataclass
class MachineVersionDetail:
    '''
    TODO:
    machine
    version_group
    '''    


@dataclass
class Name:
    name:str
    language:Language