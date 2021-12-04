from typing import Optional, Dict, List, Any
from dataclasses import dataclass
from .payload import DataPayload


class Move:
    def __init__(self, data: DataPayload):
        self.__data = data

    def __repr__(self):
        return f"{self.name}"

    @property
    def name(self) -> str:
        return self.__data.get("name")
