import pyxel
import json
from prog_type import *

draw_loop_count = 0
mob_attrib = None
ui_dict = None
state = None
mod_arg = None
fight_coord = None
fight_mob = None
karaoke_pose = 0
enemy_karaoke_pose = 0
karaoke_string = None
karaoke_index = 0
enemy_karaoke_index = 0
talking_png = {"i":0, "j":0}
mob = None
karaoke_return = None
life = 20

def update_global_variable():
    global fight_mob
    global karaoke_string
    global karaoke_return

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

        case Prog_state.KARAOKE:
            file = open("karaoke.json", "r")
            file_content = file.read()
            file_dict = json.loads(file_content)
            karaoke_string = file_dict["text"][mod_arg]
            karaoke_return = file_dict["dialogue_index"][mod_arg]
            print(karaoke_return)

