from lib.dish import *

def test_constructor():
    item = Dish("Curry", 5.50)
    assert item.name == "Curry"
    assert item.price == 5.5