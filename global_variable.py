import pyxel
import json
from prog_type import *

draw_loop_count= 0
mob_attrib= None
ui_dict= None
state= None
mod_arg= None
fight_coord= None
fight_mob= None

def update_global_variable():
    global fight_mob

    match state:
        case Prog_state.END:
            return

        case Prog_state.UI:
            return

        case Prog_state.GAME_OVER:
            return

        case Prog_state.IN_GAME:
            return

        case Prog_state.FLIGHT_FIGHT:
            file = open("flight_fight.json", "r")
            file_content = file.read()
            fight_mob = json.loads(file_content)[mod_arg]["mob"]
            print(fight_mob)
