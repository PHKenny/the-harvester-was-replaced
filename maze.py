from __builtins__ import *

def solve_maze():
    current_direction = West
    x1 = get_pos_x()
    y1 = get_pos_y()

    while True:
        move(current_direction)
        
        x2 = get_pos_x()
        y2 = get_pos_y()
        
        if x1 == x2 and y1 == y2:
            if current_direction == West:
                current_direction = North
            elif current_direction == North:
                current_direction = East
            elif current_direction == East:
                current_direction = South
            elif current_direction == South:
                current_direction = West
        else:
            x1 = get_pos_x()
            y1 = get_pos_y()
            
            if current_direction == West:
                current_direction = South
            elif current_direction == North:
                current_direction = West
            elif current_direction == East:
                current_direction = North
            elif current_direction == South:
                current_direction = East
        
        if get_entity_type() == Entities.Treasure:
            harvest()
            break