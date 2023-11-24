import pytest
from lib.dish import *

def test_constructor():
    item = Dish("Curry", 5.50)
    assert item.dish_name == "Curry"
    assert item.price == 5.5

def test_price_not_number():
    with pytest.raises(TypeError) as e:
        item = Dish("Curry", "five")
    error_message = str(e.value)
    assert error_message == "Invalid price, must be a number!"