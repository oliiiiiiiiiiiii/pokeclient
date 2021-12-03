from pokeclient.api import PokeClient


print(a:=PokeClient().fetch_pokemon("PIKACHU"))
print(dir(a))