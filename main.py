import httpx

class poke_client:  

    base_url = 'https://pokeapi.co/api/v2/'

    def poke_name_by_id(self,number:int)->str:
        return httpx.get(f"{poke_client.base_url}pokemon/{str(number)}").json()["name"]
        

    def poke_id_by_name(self,name:int)->str:
        return httpx.get(f"{poke_client.base_url}pokemon/{str(name)}").json()['id']

a = poke_client().poke_name_by_id(5)
print(a)
a = poke_client().poke_id_by_name('charmeleon')
print(a)