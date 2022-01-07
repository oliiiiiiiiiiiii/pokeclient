from typing import Dict


from typing import Dict, Any

class CacheDict(dict):

    def __add__(self,other:Dict[Any,Any]) -> Dict[Any,Any]:
        return {**self,**other}