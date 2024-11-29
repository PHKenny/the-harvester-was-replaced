from __builtins__ import *

def only_carrots_and_grass(current_x, current_y):
    if current_x < 5:
        return Entities.Grass
    return Entities.Carrots

def balanced_mode(current_x, current_y):
    if current_x % 2 == 0:
        if current_y % 2 == 0:
            return Entities.Grass
        return Entities.Tree
    
    if current_y % 2 == 0:
        return Entities.Tree
    return Entities.Carrots

def maze_mode(current_x, current_y):
    if current_x < 4:
        if current_y < 4:
            return Entities.Pumpkin
        return Entities.Carrots

    if current_x == 4:
        return Entities.Bush

    if current_x % 2 == 0:
        if current_y % 2 == 0:
            return Entities.Grass
        return Entities.Tree

    if current_y % 2 == 0:
        return Entities.Tree
    return Entities.Grass