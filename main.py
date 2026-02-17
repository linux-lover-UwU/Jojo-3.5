#!/bin/python

import json
import pyxel
import csv
from random import *
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

for i in range(len(global_variable.mob)):
    for j in range(len(global_variable.mob[i])):
            global_variable.mob[i][j]["x"] -= global_variable.tilemap_x
            global_variable.mob[i][j]["y"] -= global_variable.tilemap_y

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

            if pyxel.btn(pyxel.KEY_L):
                global_variable.save(global_variable.mob[Mob_enum.JOTARO][0]["x"], global_variable.mob[Mob_enum.JOTARO][0]["y"])

            if pyxel.btn(pyxel.KEY_E):

                jotaro_center_x = global_variable.mob[Mob_enum.JOTARO][0]["x"] + 4
                jotaro_center_y = global_variable.mob[Mob_enum.JOTARO][0]["y"] + 8
                for i in range(len(global_variable.mob[Mob_enum.BEAR])):
                    if(40 > global_variable.mob[Mob_enum.BEAR][i]["x"]+16 - jotaro_center_x > -40 and
                           40 > global_variable.mob[Mob_enum.BEAR][i]["y"]+16 - jotaro_center_y > -40):
                        global_variable.talking_png["i"] = Mob_enum.BEAR
                        global_variable.talking_png["j"] = i
                        global_variable.state = talk(global_variable.mob[Mob_enum.BEAR][i], 0)
                        if(global_variable.state != Prog_state.IN_GAME):
                            global_variable.update_global_variable()
                        elif global_variable.mod_arg == -1:
                            global_variable.mob[Mob_enum.BEAR][i] = global_variable.mob[Mob_enum.BEAR][len(global_variable.mob[Mob_enum.BEAR])-1]
                            global_variable.mob[Mob_enum.BEAR].remove(global_variable.mob[Mob_enum.BEAR][len(global_variable.mob[Mob_enum.BEAR])-1])
                            break

                for i in range(len(global_variable.mob[Mob_enum.PENGUIN])):
                    if(20 > global_variable.mob[Mob_enum.PENGUIN][i]["x"]+8 - jotaro_center_x > -20 and
                           20 > global_variable.mob[Mob_enum.PENGUIN][i]["y"]+8 - jotaro_center_y > -20):
                        global_variable.talking_png["i"] = Mob_enum.PENGUIN
                        global_variable.talking_png["j"] = i
                        global_variable.state = talk(global_variable.mob[Mob_enum.PENGUIN][i], 0)
                        if(global_variable.state != Prog_state.IN_GAME):
                            global_variable.update_global_variable()
                        elif global_variable.mod_arg == -1:
                            global_variable.mob[Mob_enum.PENGUIN][i] = global_variable.mob[Mob_enum.PENGUIN][len(global_variable.mob[Mob_enum.PENGUIN])-1]
                            global_variable.mob[Mob_enum.PENGUIN].remove(global_variable.mob[Mob_enum.PENGUIN][len(global_variable.mob[Mob_enum.PENGUIN])-1])
                            break



            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]-1, global_variable.mob[Mob_enum.JOTARO][0]["y"]) in global_variable.color_to_avoid or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]-1, global_variable.mob[Mob_enum.JOTARO][0]["y"]+16)in global_variable.color_to_avoid:
                global_variable.movement_x = 0
                global_variable.mob[Mob_enum.JOTARO][0]["x"] += 1
            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+9, global_variable.mob[Mob_enum.JOTARO][0]["y"]) in global_variable.color_to_avoid or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+9, global_variable.mob[Mob_enum.JOTARO][0]["y"]+16) in global_variable.color_to_avoid:
                global_variable.movement_x = 0
                global_variable.mob[Mob_enum.JOTARO][0]["x"] -= 1
            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"], global_variable.mob[Mob_enum.JOTARO][0]["y"]-1) in global_variable.color_to_avoid or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+8, global_variable.mob[Mob_enum.JOTARO][0]["y"]-1) in global_variable.color_to_avoid:
                global_variable.movement_y = 0
                global_variable.mob[Mob_enum.JOTARO][0]["y"] += 1
            if pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"], global_variable.mob[Mob_enum.JOTARO][0]["y"]+17) in global_variable.color_to_avoid or pyxel.pget(global_variable.mob[Mob_enum.JOTARO][0]["x"]+8, global_variable.mob[Mob_enum.JOTARO][0]["y"]+17) in global_variable.color_to_avoid:
                global_variable.movement_y = 0
                global_variable.mob[Mob_enum.JOTARO][0]["y"] -= 1

            global_variable.mob[Mob_enum.JOTARO][0]["x"]+=movement_x
            global_variable.mob[Mob_enum.JOTARO][0]["y"]+=movement_y

            if global_variable.mob[Mob_enum.JOTARO][0]["x"] > 200:
                for i in range(len(global_variable.mob)):
                    for j in range(len(global_variable.mob[i])):
                        global_variable.mob[i][j]["x"]-=1
                global_variable.tilemap_x += 1
            if global_variable.mob[Mob_enum.JOTARO][0]["y"] > 200:
                for i in range(len(global_variable.mob)):
                    for j in range(len(global_variable.mob[i])):
                        global_variable.mob[i][j]["y"]-=1
                global_variable.tilemap_y += 1
            if global_variable.mob[Mob_enum.JOTARO][0]["x"] < 50:
                for i in range(len(global_variable.mob)):
                    for j in range(len(global_variable.mob[i])):
                        global_variable.mob[i][j]["x"]+=1
                global_variable.tilemap_x -= 1
            if global_variable.mob[Mob_enum.JOTARO][0]["y"] < 50:
                for i in range(len(global_variable.mob)):
                    for j in range(len(global_variable.mob[i])):
                        global_variable.mob[i][j]["y"]+=1
                global_variable.tilemap_y -= 1

            if len(global_variable.mob[Mob_enum.BEAR]) == 0:
                global_variable.state = Prog_state.END

        case Prog_state.FLIGHT_FIGHT:
            if pyxel.btn(pyxel.KEY_Z):
                movement_y = -1
            if pyxel.btn(pyxel.KEY_Q):
                movement_x = -1
            if pyxel.btn(pyxel.KEY_S):
                movement_y = 1
            if pyxel.btn(pyxel.KEY_D):
                movement_x = 1

            if pyxel.btn(pyxel.KEY_O) and global_variable.draw_loop_count%4 == 0:
                global_variable.fight_mob[Mob_enum.PROJECTILE].append({"x":global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["x"]+16,"y":global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["y"]+8,"animation_start":0,"animation_index":0})

            for i in range(Mob_enum.BAD_GUY_1,len(global_variable.fight_mob)):
                j=0
                while j<len(global_variable.fight_mob[i]):
                    if global_variable.draw_loop_count%60 == 0:
                        global_variable.fight_mob[i][j]["direction"] = (randint(0,1)-0.5)*2
                    if global_variable.draw_loop_count%8 == 0:
                        global_variable.fight_mob[Mob_enum.BAD_PROJECTILE].append({"x":global_variable.fight_mob[i][j]["x"]-8,"y":global_variable.fight_mob[i][j]["y"]+8,"animation_start":0,"animation_index":0})

                    global_variable.fight_mob[i][j]["y"] += global_variable.fight_mob[i][j]["direction"]
                    if global_variable.fight_mob[i][j]["y"] < 0:
                        global_variable.fight_mob[i][j]["y"] = 0
                    if global_variable.fight_mob[i][j]["y"] > 210:
                        global_variable.fight_mob[i][j]["y"] = 210

                    k:int = 0
                    while k<len(global_variable.fight_mob[Mob_enum.PROJECTILE]) and j!=-1:
                        if global_variable.fight_mob[i][j]["x"] < global_variable.fight_mob[Mob_enum.PROJECTILE][k]["x"] < global_variable.fight_mob[i][j]["x"]+16 and global_variable.fight_mob[i][j]["y"] < global_variable.fight_mob[Mob_enum.PROJECTILE][k]["y"] < global_variable.fight_mob[i][j]["y"]+16:
                            global_variable.fight_mob[Mob_enum.PROJECTILE][k] = global_variable.fight_mob[Mob_enum.PROJECTILE][len(global_variable.fight_mob[Mob_enum.PROJECTILE])-1]
                            global_variable.fight_mob[Mob_enum.PROJECTILE].remove(global_variable.fight_mob[Mob_enum.PROJECTILE][k])
                            k-=1

                            global_variable.fight_mob[i][j] = global_variable.fight_mob[i][len(global_variable.fight_mob[i])-1]
                            global_variable.fight_mob[i].remove(global_variable.fight_mob[i][j])
                            j-=1

                            if i>Mob_enum.BAD_GUY_1:
                                global_variable.fight_mob[i-1].append({"x":220,"y":100,"animation_start":0,"animation_index":0, "direction":1})
                                global_variable.fight_mob[i-1].append({"x":220,"y":100,"animation_start":0,"animation_index":0, "direction":1})
                        k+=1
                    j+=1

            global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["x"] += movement_x
            global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["y"] += movement_y

            if global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["x"] > 150:
                global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["x"] = 150

            for i in range(len(global_variable.fight_mob[Mob_enum.PROJECTILE])):
                global_variable.fight_mob[Mob_enum.PROJECTILE][i]["x"] += 3

            for i in range(len(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE])):
                global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][i]["x"] -= 3

            projectile_index = 0
            while projectile_index<len(global_variable.fight_mob[Mob_enum.PROJECTILE]):
                if global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index]["x"]>256:
                    global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index] = global_variable.fight_mob[Mob_enum.PROJECTILE][len(global_variable.fight_mob[Mob_enum.PROJECTILE])-1]
                    global_variable.fight_mob[Mob_enum.PROJECTILE].remove(global_variable.fight_mob[Mob_enum.PROJECTILE][projectile_index])
                    projectile_index -= 1
                projectile_index += 1


            bad_projectile_index = 0
            while bad_projectile_index<len(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE]):
                if global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index]["x"]<0:
                    global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index] = global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][len(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE])-1]
                    global_variable.fight_mob[Mob_enum.BAD_PROJECTILE].remove(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index])
                    bad_projectile_index -= 1

                if global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["x"] < global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index]["x"] < global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["x"]+16 and global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["y"] < global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index]["y"] < global_variable.fight_mob[Mob_enum.JOTARO_FLIGHT][0]["y"]+16:
                    global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index] = global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][len(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE])-1]
                    global_variable.fight_mob[Mob_enum.BAD_PROJECTILE].remove(global_variable.fight_mob[Mob_enum.BAD_PROJECTILE][bad_projectile_index])
                    bad_projectile_index -= 1
                    global_variable.life -= 1

                bad_projectile_index += 1

            mob_count = 0
            for i in range(Mob_enum.BAD_GUY_1, len(global_variable.fight_mob)):
                for j in global_variable.fight_mob[i]:
                    mob_count+=1

            if mob_count == 0:
                global_variable.state = Prog_state.IN_GAME
                talk(global_variable.mob[global_variable.talking_png["i"]][global_variable.talking_png["j"]], global_variable.flight_return)
                if global_variable.mod_arg == -1:
                    global_variable.mob[global_variable.talking_png["i"]][global_variable.talking_png["j"]] = global_variable.mob[global_variable.talking_png["i"]][len(global_variable.mob[global_variable.talking_png["i"]])-1]
                    global_variable.mob[global_variable.talking_png["i"]].remove(global_variable.mob[global_variable.talking_png["i"]][global_variable.talking_png["j"]])


            print(mob_count)


            if global_variable.life <= 0:
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
                if global_variable.mod_arg == -1:
                    global_variable.mob[global_variable.talking_png["i"]][global_variable.talking_png["j"]] = global_variable.mob[global_variable.talking_png["i"]][len(global_variable.mob[global_variable.talking_png["i"]])-1]
                    global_variable.mob[global_variable.talking_png["i"]].remove(global_variable.mob[global_variable.talking_png["i"]][global_variable.talking_png["j"]])

            if global_variable.enemy_karaoke_index == len(global_variable.karaoke_string):
                global_variable.state = Prog_state.GAME_OVER

    global_variable.draw_loop_count+=1



def draw():
    global state

    pyxel.bltm(0, 0, 0, global_variable.tilemap_x, global_variable.tilemap_y, 256, 224)

    match global_variable.state:
        case Prog_state.END:
            while True:
                render_ui(global_variable.ui_dict[2])

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
            #pyxel.text(0,0,8,s)
            for i in range(Mob_enum.JOTARO_FLIGHT, len(global_variable.fight_mob)):
                for j in range(len(global_variable.fight_mob[i])):
                    draw_mob(global_variable.fight_mob[i][j], i)

        case Prog_state.KARAOKE:
            pyxel.cls(8)
            pyxel.blt(10, 20, 2, global_variable.karaoke_pose*50, 50, 50, 50)
            pyxel.blt(150, 20, 2, global_variable.enemy_karaoke_pose*50, 50, 50, 50)
            pyxel.text(10, 80, global_variable.karaoke_string[global_variable.karaoke_index].upper(), 0)
            pyxel.text(140, 80, global_variable.karaoke_string[global_variable.enemy_karaoke_index].upper(), 0)

pyxel.run(update, draw)
