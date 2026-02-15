#!/bin/python 

import json
import pyxel
from enum import *

import global_variable
from mob import *
from ui import *
from prog_type import *

#global_variable.init()
global_variable.state = Prog_state.IN_GAME
global_variable.fight_coord = {"x":128, "y":112}

file = open("mob_attrib.json", "r")
file_content = file.read()
global_variable.mob_attrib = json.loads(file_content)

file = open("ui.json", "r")
file_content = file.read()
global_variable.ui_dict = json.loads(file_content)

pyxel.init(256, 224, title="Boomberman pyrate")

pyxel.load("my_resource.pyxres")

mob = [[create_mob(0,0,50,50)],[{
        "x":100,
        "y":100,
        "animation_index":0,
        "animation_start":0,
        "text":["hello","I ame mario"],
        "name":"mario",
        "answer":[["hello","non","hellololo"],["hellla"]],
        "answer_action":[[Answer_action.FLIGHT_FIGHT,0,1],[0]]
    }]]

tilemap_x:int = 0
tilemap_y:int = 0

running:bool = True
def update():
    movement_x:int = 0
    movement_y:int = 0

    match global_variable.state:
        case Prog_state.IN_GAME:
            if pyxel.btn(pyxel.KEY_Z):
                movement_y = -1
            if pyxel.btn(pyxel.KEY_Q):
                movement_x = -1
            if pyxel.btn(pyxel.KEY_S):
                movement_y = 1
            if pyxel.btn(pyxel.KEY_D):
                movement_x = 1

            if pyxel.btn(pyxel.KEY_E):
                for i in range(1, len(mob)):
                    for j in range(len(mob[i])):
                        if 10 > mob[Mob_enum.JOTARO][0]["x"]-mob[i][j]["x"] > -10:
                            global_variable.state = talk(mob[i][j])
                            if(global_variable.state != Prog_state.IN_GAME):
                                global_variable.update_global_variable()
                                print(global_variable.fight_mob)


            mob[Mob_enum.JOTARO][0]["x"]+=movement_x
            mob[Mob_enum.JOTARO][0]["y"]+=movement_y

            if mob[Mob_enum.JOTARO][0]["x"] > 200:
                mob[Mob_enum.JOTARO][0]["x"] = 200
                tilemap_x += 1
            if mob[Mob_enum.JOTARO][0]["y"] > 200:
                mob[Mob_enum.JOTARO][0]["y"] = 200
                tilemap_y += 1

        case Prog_state.FLIGHT_FIGHT:
            if pyxel.btn(pyxel.KEY_Z):
                movement_y = -1
            if pyxel.btn(pyxel.KEY_Q):
                movement_x = -1
            if pyxel.btn(pyxel.KEY_S):
                movement_y = 1
            if pyxel.btn(pyxel.KEY_D):
                movement_x = 1

            if pyxel.btn(pyxel.KEY_O):
                global_variable.fight_mob[Mob_enum.PROJECTILE].append({"x":mob[Mob_enum.JOTARO][0]["x"], "y":mob[Mob_enum.JOTARO][0]["y"]})


            global_variable.fight_mob[Mob_enum.JOTARO][0]["x"]+=movement_x
            global_variable.fight_mob[Mob_enum.JOTARO][0]["y"]+=movement_y

            for i in global_variable.fight_mob[Mob_enum.PROJECTILE]:
                i["x"]+=1



def draw():
    global state

    pyxel.bltm(0, 0, 0, tilemap_x, tilemap_y, 256, 224)

    match global_variable.state:
        case Prog_state.END:
            running = False
        case Prog_state.UI:
            state = render_ui(global_variable.ui_dict[0])
        case Prog_state.GAME_OVER:
            return
        case Prog_state.IN_GAME:
            for i in range(len(mob)):
                for j in range(len(mob[i])):
                    draw_mob(mob[i][j], i)
        case Prog_state.FLIGHT_FIGHT:
            print(global_variable.fight_mob)
            for i in range(len(global_variable.fight_mob)):
                print(i)
                for j in range(len(global_variable.fight_mob[i])):
                    print("   ",j)
                    draw_mob(global_variable.fight_mob[i][j], i)

pyxel.run(update, draw)
print(global_variable.draw_loop_count)
