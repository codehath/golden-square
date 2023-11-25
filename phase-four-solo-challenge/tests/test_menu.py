import pytest
from unittest.mock import Mock
from lib.menu import *

def test_menu_constructor():
    item_1 =  Mock(dish_name = "Curry", price = 5.50)
    item_2 =  Mock(dish_name = "Pasta", price = 6.99)
    item_3 =  Mock(dish_name = "Rice", price = 3.75)
    new_menu = Menu([item_1, item_2, item_3])

    assert new_menu.all_dishes == [item_1, item_2, item_3]

def test_menu_display_menu():
    item_1 =  Mock(dish_name = "Curry", price = 5.50)
    item_2 =  Mock(dish_name = "Pasta", price = 6.99)
    item_3 =  Mock(dish_name = "Rice", price = 3.75)
    new_menu = Menu([item_1, item_2, item_3])
    
    expected = ["1 - Curry - 5.50", "2 - Pasta - 6.99", "3 - Rice - 3.75"]
    result = new_menu.display_menu()

    assert result == expected