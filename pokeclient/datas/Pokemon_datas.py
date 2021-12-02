from dataclasses import dataclass

@dataclass
class Move:
  name:str

@dataclass
class Species:
    name: str

@dataclass
class Stat:
    base_stat: int
    effort: int
    name: str

@dataclass
class Type:
    slot: int
    name: str