from __builtins__ import *

def move_x(target_x):
    while get_pos_x() != target_x:
        move(West)

def move_y(target_y):
    while get_pos_y() != target_y:
        move(South)