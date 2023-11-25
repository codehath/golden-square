from lib.dish import *

class Order:

    def __init__(self, dishes_ordered):
        self.dishes_ordered = dishes_ordered
        self.order_placed = False

    def receipt(self):
        itemised_receipt = []
        grand_total = 0
        for item, quantity in self.dishes_ordered.items():
            dish_total = item.price*quantity
            grand_total += dish_total

            itemised_receipt.append(f"{quantity} x {item.dish_name} - {dish_total:.2f}")
            print(itemised_receipt[-1])
        
        itemised_receipt.append(f"Grand Total - {grand_total:.2f}")
        print(f"Grand Total - {grand_total:.2f}")
        
        return itemised_receipt