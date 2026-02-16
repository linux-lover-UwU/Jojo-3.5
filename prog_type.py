from enum import *
import pyxel

class Prog_state(IntEnum):
    UI = 0
    IN_GAME = 1
    END = 2
    GAME_OVER = 3
    FLIGHT_FIGHT = 4
    KARAOKE = 5

def translate_char(char:str):
    match char:
        case "a":
            return pyxel.KEY_A
        case "b":
            return pyxel.KEY_B
        case "c":
            return pyxel.KEY_C
        case "d":
            return pyxel.KEY_D
        case "e":
            return pyxel.KEY_E
        case "f":
            return pyxel.KEY_F
        case "g":
            return pyxel.KEY_G
        case "h":
            return pyxel.KEY_H
        case "i":
            return pyxel.KEY_I
        case "j":
            return pyxel.KEY_J
        case "k":
            return pyxel.KEY_K
        case "l":
            return pyxel.KEY_L
        case "m":
            return pyxel.KEY_M
        case "n":
            return pyxel.KEY_N
        case "o":
            return pyxel.KEY_O
        case "p":
            return pyxel.KEY_P
        case "q":
            return pyxel.KEY_Q
        case "r":
            return pyxel.KEY_R
        case "s":
            return pyxel.KEY_S
        case "t":
            return pyxel.KEY_T
        case "u":
            return pyxel.KEY_U
        case "v":
            return pyxel.KEY_V
        case "w":
            return pyxel.KEY_W
        case "x":
            return pyxel.KEY_X
        case "y":
            return pyxel.KEY_Y
        case "z":
            return pyxel.KEY_Z
