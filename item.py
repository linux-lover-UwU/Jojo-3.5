a:dict =
{

}

def new_item(item_dict:dict[str,int], item_name:str, .item_count=1)->int:
"""
La fonction new_item prend en parametre :
item_dict : dictionnaire des items.
item_name : nom de la clee
item_count : gere le nombre d'item a changer.

valeur de retour est le nombre d'item modifier
"""
    if item_name not in item_dict:
        return -1
    if item_dict[item_name]
