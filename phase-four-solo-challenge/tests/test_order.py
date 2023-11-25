import pytest
from unittest.mock import Mock
from lib.order import *

def test_order_constructor_empty_order():
    new_order = Order({})
    assert new_order.dishes_ordered == {}
    assert new_order.order_placed == False

def test_order_constructor():
    dish_1 =  Mock(dish_name = "Curry", price = 5.50)
    dish_2 =  Mock(dish_name = "Rice", price = 3.75)
    dishes_ordered = {dish_1: 3, dish_2: 2}
    new_order = Order(dishes_ordered)

    assert new_order.dishes_ordered == dishes_ordered
    assert new_order.order_placed == False

def test_order_receipt_single_item():
    dish_1 =  Mock(dish_name = "Curry", price = 5.50)
    dishes_ordered = {dish_1: 1}
    new_order = Order(dishes_ordered)
    result = new_order.receipt()
    expected = [f"1 x Curry - {dish_1.price:.2f}", "Grand Total - 5.50"]
    assert result == expected

def test_order_receipt_multiple_items():
    dish_1 =  Mock(dish_name = "Curry", price = 5.50)
    dish_2 =  Mock(dish_name = "Pasta", price = 6.99)
    dish_3 =  Mock(dish_name = "Rice", price = 3.75)
    dishes_ordered = {dish_1: 3, dish_3: 2}
    new_order = Order(dishes_ordered)
    result = new_order.receipt()
    expected = [f"3 x Curry - {dish_1.price*3:.2f}", f"2 x Rice - {dish_3.price*2:.2f}", "Grand Total - 24.00"]
    assert result == expected

# def order_placed_text():
#     with pytest.raises(TypeError) as e:
#         item = Dish("Curry", "five")
#     error_message = str(e.value)
#     assert error_message == "Invalid price, must be a number!"

# # The Order constructor raises an error when the quantity of a dish is invalid.
# def test_order_constructor_invalid_dish_quantity():
#     with pytest.raises(TypeError) as e:
#         dish_1 = Mock(dish_name="Curry", price=5.50)
#         dishes_ordered = {dish_1: "three"}
#         new_order = Order(dishes_ordered)
#     error_message = str(e.value)
#     assert error_message == "Invalid quantity, must be a number!"