from unittest.mock import Mock
from lib.order_system import *

def test_order_system_constructor():
    dish_1 =  Dish("Curry", 5.50)
    dish_2 =  Dish("Rice", 3.75)

    menu_items = [dish_1, dish_2]

    the_menu = Mock(all_dishes = menu_items)

    system = OrderSystem(the_menu)