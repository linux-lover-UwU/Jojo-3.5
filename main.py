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

global_variable.mob = [[create_mob(0,0,50,50)],[{
        "x":100,
        "y":100,
        "animation_index":0,
        "animation_start":0,
        "text":["hello","I ame mario"],
        "name":"mario",
        "answer":[["hello","non","hellololo"],["hellla"]],
        "answer_action":[[Answer_action.KARAOKE,0,1],[0]]
    }]]

tilemap_x:int = 0
tilemap_y:int = 0

running:bool = True
def update():
    global global_variable

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
                for i in range(1, len(global_variable.mob)):
                    for j in range(len(global_variable.mob[i])):
                        if 10 > global_variable.mob[Mob_enum.JOTARO][0]["x"]-global_variable.mob[i][j]["x"] > -10:
                            global_variable.talking_png["i"] = i
                            global_variable.talking_png["j"] = j
                            global_variable.state = talk(global_variable.mob[i][j])
                            if(global_variable.state != Prog_state.IN_GAME):
                                global_variable.update_global_variable()


            global_variable.mob[Mob_enum.JOTARO][0]["x"]+=movement_x
            global_variable.mob[Mob_enum.JOTARO][0]["y"]+=movement_y

            if global_variable.mob[Mob_enum.JOTARO][0]["x"] > 200:
                global_variable.mob[Mob_enum.JOTARO][0]["x"] = 200
                tilemap_x += 1
            if global_variable.mob[Mob_enum.JOTARO][0]["y"] > 200:
                global_variable.mob[Mob_enum.JOTARO][0]["y"] = 200
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
                global_variable.fight_mob[Mob_enum.PROJECTILE].append({"x":global_variable.fight_mob[Mob_enum.JOTARO][0]["x"], "y":global_variable.fight_mob[Mob_enum.JOTARO][0]["y"], "animation_start":0, "animation_index":0})


            global_variable.fight_mob[Mob_enum.JOTARO][0]["x"]+=movement_x
            global_variable.fight_mob[Mob_enum.JOTARO][0]["y"]+=movement_y

            i:int = 0
            while i<len(global_variable.fight_mob[Mob_enum.PROJECTILE]):
                global_variable.fight_mob[Mob_enum.PROJECTILE][i]["x"]+=1
                if(global_variable.fight_mob[Mob_enum.PROJECTILE][i]["x"] > 256):
                    global_variable.fight_mob[Mob_enum.PROJECTILE][i] = global_variable.fight_mob[Mob_enum.PROJECTILE][len(global_variable.fight_mob[Mob_enum.PROJECTILE])-1]
                    global_variable.fight_mob[Mob_enum.PROJECTILE].remove(global_variable.fight_mob[Mob_enum.PROJECTILE][len(global_variable.fight_mob[Mob_enum.PROJECTILE])-1])
                    i-=1
                i+=1

        case Prog_state.KARAOKE:
            if pyxel.btnp(translate_char(global_variable.karaoke_string[global_variable.karaoke_index])):
                global_variable.karaoke_index += 1
                global_variable.karaoke_pose = global_variable.karaoke_pose ^ 1

            if global_variable.draw_loop_count%30 == 0:
                global_variable.enemy_karaoke_index += 1
                global_variable.enemy_karaoke_pose = global_variable.enemy_karaoke_pose ^ 1

            if global_variable.karaoke_index == len(global_variable.karaoke_string):
                global_variable.state = Prog_state.IN_GAME
                talk(global_variable.mob[global_variable.talking_png["i"]][global_variable.talking_png["j"]])
                mod_arg = True

            if global_variable.enemy_karaoke_index == len(global_variable.karaoke_string):
                global_variable.state = Prog_state.GAME_OVER

    global_variable.draw_loop_count+=1



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
            for i in range(len(global_variable.mob)):
                for j in range(len(global_variable.mob[i])):
                    draw_mob(global_variable.mob[i][j], i)

        case Prog_state.FLIGHT_FIGHT:
            pyxel.cls(1)
            for i in range(len(global_variable.fight_mob)):
                for j in range(len(global_variable.fight_mob[i])):
                    draw_mob(global_variable.fight_mob[i][j], i)

        case Prog_state.KARAOKE:
            pyxel.cls(1)
            pyxel.blt(10, 20, 2, global_variable.karaoke_pose*50, 50, 50, 50)
            pyxel.blt(150, 20, 2, global_variable.enemy_karaoke_pose*50, 50, 50, 50)
            pyxel.text(10, 80, global_variable.karaoke_string[global_variable.karaoke_index].upper(), 0)
            pyxel.text(140, 80, global_variable.karaoke_string[global_variable.enemy_karaoke_index].upper(), 0)

pyxel.run(update, draw)
