from lib.order import *
from lib.menu import *
from lib.dish import *
from lib.order_system import *

# def test_order_system_integration_make_order():
#     system = OrderSystem()
#     dish_1 =  Dish(dish_name = "Curry", price = 5.50)
#     dish_2 =  Dish(dish_name = "Pasta", price = 6.99)
#     dish_3 =  Dish(dish_name = "Rice", price = 3.75)
#     dish_4 =  Dish(dish_name = "Noodle", price = 5.50)
#     dish_5 =  Dish(dish_name = "Sirloin Steak", price = 37)
#     dish_6 =  Dish(dish_name = "Chicken Fajitas", price = 9.20)

#     menu_items = [dish_1, dish_2, dish_3, dish_4, dish_5, dish_6]

#     the_menu = Menu(menu_items)
#     the_menu.display_menu()

#     system.run()

def test_run():
    dish_1 =  Dish("Curry", 5.50)
    dish_2 =  Dish("Pasta", 6.99)
    dish_3 =  Dish("Rice", 3.75)
    dish_4 =  Dish("Noodle", 5.50)
    dish_5 =  Dish("Sirloin Steak", 37)
    dish_6 =  Dish("Chicken Fajitas", 9.20)

    menu_items = [dish_1, dish_2, dish_3, dish_4, dish_5, dish_6]

    the_menu = Menu(menu_items)

    system = OrderSystem(the_menu)
    system.run()

# def order_placed_text():
#     expected = "Thank you! Your order was placed and will be delivered before 18:52"
