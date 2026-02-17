from enum import *
import pyxel
import global_variable
from prog_type import *
from ui import *
from inventaire import *

class Mob_enum(IntEnum):
    JOTARO = 0
    PENGUIN = 1
    BEAR = 2
    JOTARO_FLIGHT = 3
    BAD_PROJECTILE = 4
    PROJECTILE = 5
    BAD_GUY_1 = 6
    BAD_GUY_2 = 7

class Answer_action(IntEnum):
    FLIGHT_FIGHT = -1
    KARAOKE = -2
    END = -3
    DEAD = -4
    CHECK_INVENTORY = -5
    ADD_INVENTORY = -6

def create_mob(x:int, y:int, w:int, h:int)->dict:
    return {
        "x":x,
        "y":y,
        "animation_index":1,
        "animation_start":0
    }

def draw_mob(mob:dict, mob_type:Mob_enum)->None:
    u:int = 0
    v:int = 0
    w:int = 0
    h:int = 0

    animation_image:int = (global_variable.draw_loop_count - mob["animation_start"]) % global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["image_count"]

    for i in range(len(global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["v"])):
        if animation_image > global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["image_time"][i]:
            animation_image -= global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["image_time"][i]
        else:
            u:int = global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["u"][i]
            v:int = global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["v"][i]
            w:int = global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["w"][i]
            h:int = global_variable.mob_attrib[mob_type]["animation"][mob["animation_index"]]["h"][i]
            break

    pyxel.blt(mob["x"], mob["y"], 0, u, v, w, h)

def talk(mob, dialogue_index):
    print(mob , dialogue_index)
    i = dialogue_index
    while i<len(mob["text"]):
        print(i)
        ui:dict = {"button":[{"text":mob["answer"][i][j], "x":0, "y":200+6*j} for j in range(len(mob["answer"][i]))] + [{"x": 0, "y": 150,"text": mob["name"]},{"x": 10, "y":160 ,"text": mob["text"][i]}], "background": -1 ,"selected": 0, "over": False}
        while not pyxel.btnp(pyxel.KEY_A):
            if pyxel.btnp(pyxel.KEY_Z):
                ui["selected"] -= 1
                if ui["selected"] == -1:
                    ui["selected"] = len(mob["answer"][i])-1
            if pyxel.btnp(pyxel.KEY_S):
                ui["selected"] = (ui["selected"]+1) % len(mob["answer"][i])

            pyxel.rect(0, 150, 255, 74, 1)
            render_ui(ui)
            pyxel.flip()
        pyxel.flip()
        if mob["answer_action"][i][ui["selected"]] < 0:
            global_variable.mod_arg = mob["action_arg"][i][ui["selected"]]
            match mob["answer_action"][i][ui["selected"]]:
                case Answer_action.FLIGHT_FIGHT:
                    return Prog_state.FLIGHT_FIGHT
                case Answer_action.KARAOKE:
                    return Prog_state.KARAOKE
                case Answer_action.END:
                    return Prog_state.IN_GAME
                case Answer_action.CHECK_INVENTORY:
                    if check_inventaire(mob["action_arg"][i][ui["selected"]]["item"], mob["action_arg"][i][ui["selected"]]["count"]):
                        i = mob["action_arg"][i][ui["selected"]]["check"]
                    else:
                        i = mob["action_arg"][i][ui["selected"]]["not_check"]

                case Answer_action.ADD_INVENTORY:
                    ajouter_inventaire(mob["action_arg"][i][ui["selected"]]["item"], mob["action_arg"][i][ui["selected"]]["count"])
                    i = mob["action_arg"][i][ui["selected"]]["next"]
        else:
            i = mob["answer_action"][i][ui["selected"]]
    return Prog_state.IN_GAME
