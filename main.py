#!/bin/python

import json
import pyxel
import csv
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
file.close()

file = open("ui.json", "r")
file_content = file.read()
global_variable.ui_dict = json.loads(file_content)
file.close()

pyxel.init(256, 224, title="Boomberman pyrate")

pyxel.load("my_resource.pyxres")

file = open("mob.json", "r")
file_content = file.read()
global_variable.mob = json.loads(file_content)

with open("save.csv", "r") as file:
    file_content = csv.reader(file)
    save_list = [i for i in file_content]
    global_variable.tilemap_x = int(save_list[1][0])
    global_variable.tilemap_y = int(save_list[2][0])

    global_variable.mob[Mob_enum.JOTARO][0]["x"] = int(save_list[1][1])
    global_variable.mob[Mob_enum.JOTARO][0]["y"] = int(save_list[2][1])

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
                            global_variable.state = talk(global_variable.mob[i][j], 0)
                            if(global_variable.state != Prog_state.IN_GAME):
                                global_variable.update_global_variable()


            global_variable.mob[Mob_enum.JOTARO][0]["x"]+=movement_x
            global_variable.mob[Mob_enum.JOTARO][0]["y"]+=movement_y

            if global_variable.mob[Mob_enum.JOTARO][0]["x"] > 200:
                global_variable.mob[Mob_enum.JOTARO][0]["x"] = 200
                global_variable.tilemap_x += 1
            if global_variable.mob[Mob_enum.JOTARO][0]["y"] > 200:
                global_variable.mob[Mob_enum.JOTARO][0]["y"] = 200
                global_variable.tilemap_y += 1

            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]-1, global_variable.mob[Mob_enum.JOTARO][0]["y"])==4 or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]-1, global_variable.mob[Mob_enum.JOTARO][0]["y"]+16)==4:
                global_variable.mob[Mob_enum.JOTARO][0]["x"] += 1
            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+9, global_variable.mob[Mob_enum.JOTARO][0]["y"])==4 or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+9, global_variable.mob[Mob_enum.JOTARO][0]["y"]+16)==4:
                global_variable.mob[Mob_enum.JOTARO][0]["x"] -= 1
            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"], global_variable.mob[Mob_enum.JOTARO][0]["y"]-1)==4 or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+8, global_variable.mob[Mob_enum.JOTARO][0]["y"]-1)==4:
                global_variable.mob[Mob_enum.JOTARO][0]["y"] += 1
            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"], global_variable.mob[Mob_enum.JOTARO][0]["y"]+17)==4 or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+8, global_variable.mob[Mob_enum.JOTARO][0]["y"]+17)==4:
                global_variable.mob[Mob_enum.JOTARO][0]["y"] -= 1

        case Prog_state.FLIGHT_FIGHT:
            if pyxel.btn(pyxel.KEY_Z):
                movement_y = -1
            if pyxel.btn(pyxel.KEY_Q):
                movement_x = -1
            if pyxel.btn(pyxel.KEY_S):
                movement_y = 1
            if pyxel.btn(pyxel.KEY_D):
                movement_x = 1

            if pyxel.btn(pyxel.KEY_O) and global_variable.draw_loop_count%5 == 0:
                global_variable.fight_mob[Mob_enum.PROJECTILE].append({"x":global_variable.fight_mob[Mob_enum.JOTARO][0]["x"], "y":global_variable.fight_mob[Mob_enum.JOTARO][0]["y"], "animation_start":0, "animation_index":0})



            for i in global_variable.fight_mob[Mob_enum.BAD_GUY]:
                if global_variable.draw_loop_count%10 == 0:
                    global_variable.fight_mob[Mob_enum.BAD_PROJECTILE].append({"x":i["x"], "y":i["y"], "animation_start":0, "animation_index":0})


            global_variable.fight_mob[Mob_enum.JOTARO][0]["x"]+=movement_x
            global_variable.fight_mob[Mob_enum.JOTARO][0]["y"]+=movement_y

            projectile_index:int = 0
            while projectile_index<len(global_variable.fight_mob[Mob_enum.PROJECTILE]):
                for i in range(len(global_variable.fight_mob[Mob_enum.BAD_GUY])):
                    if(global_variable.fight_mob[Mob_enum.BAD_GUY][i]["y"]<global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index]["y"] and
                        global_variable.fight_mob[Mob_enum.BAD_GUY][i]["y"] + global_variable.mob_attrib[Mob_enum.BAD_GUY]["animation"][0]["h"][0] > global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index]["y"] and
                        global_variable.fight_mob[Mob_enum.BAD_GUY][i]["x"] > global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index]["x"]):
                        global_variable.fight_mob[Mob_enum.BAD_GUY][i]["y"] = global_variable.fight_mob[Mob_enum.BAD_GUY][len(global_variable.fight_mob[Mob_enum.BAD_GUY])-1]["y"] 
                        global_variable.fight_mob[i].remove(global_variable.fight_mob[i][len(global_variable.fight_mob[i])]["y"])

                global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index]["x"]+=10
                if(global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index]["x"] > 256):
                    global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index] = global_variable.fight_mob[Mob_enum.PROJECTILE][len(global_variable.fight_mob[Mob_enum.PROJECTILE])-1]
                    global_variable.fight_mob[Mob_enum.PROJECTILE].remove(global_variable.fight_mob[Mob_enum.PROJECTILE][len(global_variable.fight_mob[Mob_enum.PROJECTILE])-1])
                    projectile_index-=1
                projectile_index+=1


            bad_projectile_index:int = 0
            while bad_projectile_index<len(global_variable.fight_mob[Mob_enum.PROJECTILE]):
                if(global_variable.fight_mob[Mob_enum.JOTARO][0]["y"]<global_variable.fight_mob[Mob_enum.PROJECTILE][bad_projectile_index]["y"] and
                   global_variable.fight_mob[Mob_enum.JOTARO][0]["y"] + global_variable.mob_attrib[Mob_enum.JOTARO]["animation"]["h"][0] > global_variable.fight_mob[Mob_enum.PROJECTILE][bad_projectile_index]["y"] and
                   global_variable.fight_mob[Mob_enum.JOTARO][0]["x"] > global_variable.fight_mob[Mob_enum.PROJECTILE][bad_projectile_index]["x"]):
                    global_variable.life -= 1

                print(len)

                global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index]["x"]-=10
                if(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index]["x"] <0):
                    global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index] = global_variable.fight_mob[Mob_enum.PROJECTILE][len(global_variable.fight_mob[Mob_enum.PROJECTILE])-1]
                    global_variable.fight_mob[Mob_enum.BAD_PROJECTILE].remove(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][len(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE])-1])
                    bad_projectile_index-=1
                bad_projectile_index+=1

                if global_variable.life <=0:
                    global_variable.state = Prog_state.GAME_OVER

        case Prog_state.KARAOKE:
            if pyxel.btnp(translate_char(global_variable.karaoke_string[global_variable.karaoke_index])):
                global_variable.karaoke_index += 1
                global_variable.karaoke_pose = global_variable.karaoke_pose ^ 1

            if global_variable.draw_loop_count%30 == 0:
                global_variable.enemy_karaoke_index += 1
                global_variable.enemy_karaoke_pose = global_variable.enemy_karaoke_pose ^ 1

            if global_variable.karaoke_index == len(global_variable.karaoke_string):
                global_variable.state = Prog_state.IN_GAME
                talk(global_variable.mob[global_variable.talking_png["i"]][global_variable.talking_png["j"]], global_variable.karaoke_return)

            if global_variable.enemy_karaoke_index == len(global_variable.karaoke_string):
                global_variable.state = Prog_state.GAME_OVER

    global_variable.draw_loop_count+=1



def draw():
    global state

    pyxel.bltm(0, 0, 0, global_variable.tilemap_x, global_variable.tilemap_y, 256, 224)

    match global_variable.state:
        case Prog_state.END:
            running = False

        case Prog_state.UI:
            state = render_ui(global_variable.ui_dict[0])

        case Prog_state.GAME_OVER:
            return

        case Prog_state.IN_GAME:
            global_variable.mob[Mob_enum.JOTARO][0]["animation_index"] = 0
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_Q):
                global_variable.mob[Mob_enum.JOTARO][0]["animation_index"] = 1


            for i in range(len(global_variable.mob)):
                for j in range(len(global_variable.mob[i])):
                    draw_mob(global_variable.mob[i][j], i)

        case Prog_state.FLIGHT_FIGHT:
            pyxel.cls(1)
            for i in range(len(global_variable.fight_mob)):
                for j in range(len(global_variable.fight_mob[i])):
                    draw_mob(global_variable.fight_mob[i][j], i)

        case Prog_state.KARAOKE:
            pyxel.cls(8)
            pyxel.blt(10, 20, 2, global_variable.karaoke_pose*50, 50, 50, 50)
            pyxel.blt(150, 20, 2, global_variable.enemy_karaoke_pose*50, 50, 50, 50)
            pyxel.text(10, 80, global_variable.karaoke_string[global_variable.karaoke_index].upper(), 0)
            pyxel.text(140, 80, global_variable.karaoke_string[global_variable.enemy_karaoke_index].upper(), 0)

pyxel.run(update, draw)
