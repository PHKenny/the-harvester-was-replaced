from __builtins__ import *
from actions import *
from maze import *
from move import *

while True:
    trade_up()

    x = get_pos_x()
    y = get_pos_y()

    desired_entity = Entities.Grass
    ## Only Carrots and Grass
    # if x < 5:
    #     desired_entity = Entities.Grass
    # else:
    #     desired_entity = Entities.Carrots

    ## Balanced
    # if x % 2 == 0:
    #     if y % 2 == 0:
    #         desired_entity = Entities.Grass
    #     else:
    #         desired_entity = Entities.Tree
    # else:
    #     if y % 2 == 0:
    #         desired_entity = Entities.Tree
    #     else:
    #         desired_entity = Entities.Carrots
    
    ## Maze
    # if x < 4:
    #     if y < 4:
    #         desired_entity = Entities.Pumpkin
    #     else:
    #         desired_entity = Entities.Carrots
    # else:
    #     # if y < 2:
    #     #     desired_entity = Entities.Bush
    #     # else:
    #     if x % 2 == 0:
    #         if y % 2 == 0:
    #             desired_entity = Entities.Grass
    #         else:
    #             desired_entity = Entities.Tree
    #     else:
    #         if y % 2 == 0:
    #             desired_entity = Entities.Tree
    #         else:
    #             desired_entity = Entities.Grass

    if desired_entity != Entities.Carrots and desired_entity != Entities.Pumpkin and desired_entity != Entities.Sunflower:
        if get_ground_type() == Grounds.Soil:
            till()
    else:
        if get_ground_type() != Grounds.Soil:
            till()
    
    if desired_entity == Entities.Bush:
        use_item(Items.Fertilizer)
        do_a_flip()

        if get_entity_type() == Entities.Hedge:
            solve_maze()
            print('Maze solved')
            move_x(0)
            move_y(0)
            continue

    if wait_harvest():
        if get_entity_type() != None:
            harvest()

        plant(desired_entity)

    fill_water()
    move(North)

    if y == get_world_size() - 1:
        move(East)