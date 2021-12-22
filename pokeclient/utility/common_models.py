from dataclasses import dataclass
from languages import Language

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
class Name:
    name:str
    language:Language