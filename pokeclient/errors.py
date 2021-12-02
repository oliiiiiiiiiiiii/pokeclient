class PokeNotFound(Exception):
  def __init__(self):
    super().__init__("No such pokemon found")

class MoveNotFound(Exception):
  def __init__(self):
    super().__init__("No such move found")