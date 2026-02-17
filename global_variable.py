import pyxel
import json
from prog_type import *
import csv

inventory = {}
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
position_3d = [0.0, 0.0]
camera_rotation = [0.0, 0.0]
tilemap_x:int = 0
tilemap_y:int = 0
color_to_avoid:list[int] = [4, 0, 1, 5]
flight_return = None

def update_global_variable():
    global fight_mob
    global karaoke_string
    global karaoke_return
    global flight_return

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
            file_dict = json.loads(file_content)
            flight_return = file_dict["dialogue_index"][mod_arg]
            fight_mob = file_dict["mob"][mod_arg]
            print(fight_mob)

        case Prog_state.KARAOKE:
            file = open("karaoke.json", "r")
            file_content = file.read()
            file_dict = json.loads(file_content)
            karaoke_string = file_dict["text"][mod_arg]
            karaoke_return = file_dict["dialogue_index"][mod_arg]
            print(karaoke_return)

def save(x, y):
    with open("save.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        data = [["tilemap", "position"],
                [tilemap_x, x],
                [tilemap_y, y]
                ]
        writer.writerows(data)
