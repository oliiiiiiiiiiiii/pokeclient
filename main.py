import httpx

class poke_client:  

    base_url = 'https://pokeapi.co/api/v2/'

    def get_poke_name_by_id(self,number:int)->str:
        data = httpx.get(f"{poke_client.base_url}pokemon/{str(number)}")
        return data.json()["name"]
        
a = poke_client().get_poke_name_by_id(5)
print(a)