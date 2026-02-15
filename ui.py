import pyxel

from prog_type import *

"""
La dict ui peut contenir different tableau:
button      contien la posision du centre du boutton avec un text qui affectera sa taille
text        contien la position et les text a afficher
image       contien la posion, les coordonne uv, l'indice de l'image et la taille de l'image

il y a aussi d'autre variable:
background  contien la couleur du fond (si egale -1 alors pas de fond
selected    contien l'indice du button selectionner
"""

def render_ui(ui_dict:dict)->Prog_state:
    if(ui_dict["background"] != -1):
        pyxel.cls(ui_dict["background"])
    for i in range(len(ui_dict["button"])):
        text_col = 7
        if ui_dict["selected"] == i:
            text_col = 9
        if ui_dict["selected"] == i and ui_dict["over"]:
            text_col = 3
        pyxel.text(ui_dict["button"][i]["x"], ui_dict["button"][i]["y"], ui_dict["button"][i]["text"], text_col)

    if(ui_dict["over"]):
        return Prog_state.ui

    return Prog_state.UI
