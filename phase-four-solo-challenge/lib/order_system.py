from datetime import datetime, timedelta
import json
from twilio.rest import Client

from lib.order import *
from lib.menu import *
from lib.dish import *

class OrderSystem():
    def __init__(self, menu):
        self.menu = menu

        # Read Twilio credentials from JSON file
        with open('twilio_credentials.json') as f:
            twilio_credentials = json.load(f)

        
        # Extract credentials
        account_sid = twilio_credentials["account_sid"]
        auth_token = twilio_credentials["auth_token"]
        self.twilio_phone_number = twilio_credentials["twilio_phone_number"]

        print(account_sid)
        print(auth_token)
        print(self.twilio_phone_number)


        # Create a Twilio client
        self.client = Client(account_sid, auth_token)

    def run(self):
        self.menu.display_menu()
        new_order = self.take_order()
        self.place_order(new_order)

    def take_order(self):
        order_finished = False
        order = {}

        while order_finished == False:
            print("What would you like to order?/n Enter x when you are done." )
            menu_item_input = input("Select Menu Item: ")
            quantity_input = input(f"How many would you like: ")
            
            if menu_item_input == "x" or quantity_input == "x":
                order_finished = True
            else:
                dish = self.menu.all_dishes[int(menu_item_input) - 1]
                order[dish] = int(quantity_input)

        customer_order = Order(order)
        
        return customer_order
    
    def order_placed_text(self):
        customer_phone_number = "+447453179983"
        current_time = datetime.now()
        delivery_time = current_time + timedelta(minutes=45)
        text = f"Thank you! Your order was placed and will be delivered before {delivery_time.strftime('%H:%M')}"

        # # Send an SMS
        # message = self.client.messages.create(
        #     to = customer_phone_number,
        #     from_= self.twilio_phone_number,
        #     body = text
        # )

        # SMS Text - For Testing to not waste Trial Allowance
        print(text)

        # print("Message SID:", message.sid)

    def place_order(self, order):
        order.receipt()
        self.order_placed_text()
        order.order_placed = True
