import json
import httpx

class poke_client:  

    base_url = 'https://pokeapi.co/api/v2/'

    def poke_name_by_id(self,number:int)->str:
        try:
            return httpx.get(f"{poke_client.base_url}pokemon/{str(number)}").json()["name"]
        except json.decoder.JSONDecodeError:
            return None

    def poke_id_by_name(self,name:int)->str:
        try:
            return httpx.get(f"{poke_client.base_url}pokemon/{str(name)}").json()['id']
        except json.decoder.JSONDecodeErrorJSONDecodeError:
            return None
