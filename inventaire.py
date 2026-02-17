import global_variable

"""
La fonction prend en parametre un str item t un int item_nombre
La fonction retire item_nombre d'item dans inventaire
Returne True si l'item est present en quantiter superieur a item_nombre dans la variable global global_variable.inventory
Returne False si l'item n'est pas present en quantiter superieur a item_nombre dans la variable global global_variable.inventory
"""
def check_inventaire(item:str, item_nombre:int) -> bool:
    global global_variable
    if item not in global_variable.inventory:
        return False
    else:
        if global_variable.inventory[item] < item_nombre:
            return False
        else:
            global_variable.inventory[item] = global_variable.inventory[item] - item_nombre
            return True






"""
La fonction prend en parametre un str item t un int item_nombre
La fonction ajoute item_nombre a global_variable.inventory[item] ou cree un item de item_nombre
"""
def ajouter_inventaire(item:str, item_nombre:int):
    global global_variable
    if item not in global_variable.inventory:
        global_variable.inventory[item] = item_nombre
    else:
        global_variable.inventory[item] = global_variable.inventory[item] < item_nombre
