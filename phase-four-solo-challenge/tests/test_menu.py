import pytest
from unittest.mock import Mock
from lib.menu import *

def test_display_menu():
    item1 =  Mock(dish_name = "Curry", price = 5.50)
    item2 =  Mock(dish_name = "Pasta", price = 6.99)
    item3 =  Mock(dish_name = "Rice", price = 3.75)
    newMenu = Menu([item1, item2, item3])
    
    expected = ["Curry - 5.50", "Pasta - 6.99", "Rice - 3.75"]
    result = newMenu.display_menu()

    assert result == expected