#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount 
        self.total = 0
        self.items = []
        self.item_prices = []

    def add_item(self, title, price, quantity = 1):
        i = 0 
        while(i < quantity):
            self.total = self.total + price 
            self.items.append(title)
            self.item_prices.append(price)

    def apply_discount(self):
        if (self.discount == 0): 
            print("There is no discount to apply.")
        
        else: 
            disc = self.discount/100
            self.total = int(self.total-(self.total*disc))
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.items.pop()
        void_cost = self.item_prices.pop()
        self.total = self.total-void_cost



# testRegister = CashRegister()
# testRegister.add_item("beans", 5)
# testRegister.add_item("eggs", 5)
# testRegister.add_item("cheese", 5)
# testRegister.add_item("milk", 5)

# print(testRegister.items)
# print(testRegister.total)

