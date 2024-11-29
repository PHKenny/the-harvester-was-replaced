from __builtins__ import *

def wait_harvest():
    if not get_entity_type():
        return True

    while not can_harvest():
        pass

    return True

def confirm_plant(entity):
    if get_entity_type() != entity:
        plant(entity)
        return confirm_plant(entity)
    return True

def fill_water():
    while num_items(Items.Water_Tank) > 0 and get_water() < 0.7:
        use_item(Items.Water_Tank)

def trade_up():
    while num_items(Items.Carrot_Seed) < 8:
          if not trade(Items.Carrot_Seed):
              break

    while num_items(Items.Pumpkin_Seed) < 8:
        if not trade(Items.Pumpkin_Seed):
            break
    
    # while num_items(Items.Sunflower_Seed) < 8:
    #     if not trade(Items.Sunflower_Seed):
    #         break

    while num_items(Items.Fertilizer) < 16:
        if not trade(Items.Fertilizer):
            break

    while (num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)) < 150:
        trade(Items.Empty_Tank)