from dataclasses import dataclass

@dataclass
class Pokemon:
    id:int
    name:str
    types:list[str]
    moves:list[str]