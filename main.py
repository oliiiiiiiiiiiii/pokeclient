from pokeclient import PokeClient

def method(obj):
    for _ in dir(obj):
        attr = getattr(obj, _, None)
        if not "data" in _ and not "__" in _:
            print(f"{_}:", attr)

client = PokeClient()
e = client.fetch_pokemon_with_id(50)
method(e)