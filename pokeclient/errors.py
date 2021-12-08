class BerryNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Berry was not found : {arg}")


class ContestNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Contest was not found : {arg}")


class EncounterNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Encounter was not found : {arg}")


class EvolutionNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Evolution was not found : {arg}")


class GameNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Game was not found : {arg}")


class ItemNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Item was not found : {arg}")


class LocationNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Location was not found : {arg}")


class MachineNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Machine was not found : {arg}")


class MoveNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Move was not found : {arg}")

class PokemonNotFound(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Pokemon was not found : {arg}")
