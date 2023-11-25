from unittest.mock import Mock, patch
from lib.order_system import *


# Mock the menu object
dish_1 =  Mock(dish_name = "Curry", price = 5.50)
dish_2 =  Mock(dish_name = "Pasta", price = 6.99)
dish_3 =  Mock(dish_name = "Rice", price = 3.75)
dish_4 =  Mock(dish_name = "Noodle", price = 5.50)
dish_5 =  Mock(dish_name = "Sirloin Steak", price = 37)
dish_6 =  Mock(dish_name = "Chicken Fajitas", price = 9.20)
menu_items = [dish_1, dish_2, dish_3, dish_4, dish_5, dish_6]
# menu_mock = Mock(spec = Menu)
menu_mock = Mock(all_dishes = menu_items)

client_mock = Mock()

# order_mock = Mock(spec=Order)


# # To Mock constructor, may need to mock twilio client
# def test_order_system_constructor():
#     dish_1 =  Dish("Curry", 5.50)
#     dish_2 =  Dish("Rice", 3.75)

#     menu_items = [dish_1, dish_2]
#     the_menu = Mock(all_dishes = menu_items)
#     system = OrderSystem(the_menu)

#     assert system.menu == the_menu


@patch('builtins.input', side_effect=['1', '2', 'x']) # Mock input
def test_take_order(mock_input):
    # Instantiate OrderSystem with Menu mock
    system = OrderSystem(menu_mock)    

    # Call the take_order method
    order = system.take_order()

    # Assert that the order is correct
    expected = {menu_mock.all_dishes[0]: 2}
    actual = order.dishes_ordered
    assert actual == expected





# import io
# import sys

# def test_take_order():
#     # Create an instance of the OrderSystem class
#     order_system = OrderSystem(menu_mock)

#     # Create a mock input string to simulate user input
#     # mock_input = "1\n2\nx\n"
#     mock_input = ['1', '2', 'x', 'x']
#     # mock_input = ['1', '\n','2' ,'\n' , 'x','\n' ,'x','\n']

#     # Patch the input() function to return the mock input string
#     with patch('builtins.input', side_effect=mock_input):
#         # Redirect stdout to a StringIO object to capture the output
#         captured_output = io.StringIO()
#         sys.stdout = captured_output

#         # Call the take_order function
#         order = order_system.take_order()

#         # Restore stdout
#         sys.stdout = sys.__stdout__

#         # Assert the output and the order object
#         # assert captured_output.getvalue() == "What would you like to order?\nEnter x when you are done.\nSelect Menu Item: How many would you like: "
#         assert captured_output.getvalue().strip() == "What would you like to order?\nEnter x when you are done.\nSelect Menu Item: How many would you like: "

#         # expected_output = "What would you like to order?\n Enter x when you are done.\nSelect Menu Item: How many would you like: "
#         # assert captured_output.getvalue().strip() == expected_output
        
#         # assert order == Order({menu.all_dishes[0]: 2})
#         assert True == False