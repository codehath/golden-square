from lib.dish import *

class Menu():
    def __init__(self, all_dishes):
        self.all_dishes = all_dishes
    
    def display_menu(self):
        itemised_menu = []
        menu_item = 0
        for dish in self.all_dishes:
            menu_item += 1
            itemised_menu.append(f"{menu_item} - {dish.dish_name} - {dish.price:.2f}")
            print(itemised_menu[-1])
        return itemised_menu