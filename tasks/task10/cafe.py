"""
Create a list of available items in the cafe.
Create 2 dictionaries one for stock of items and
second one for price of each item.
Using for loop find out total price for the stock available in the cafe
and print answer.

"""

menu = ["Chocolates", "Sandwiches", "Cookies", "Cake slice", "Water bottle"]
stock = {
        "Chocolates": 100,
        "Sandwiches": 30,
        "Cookies": 50,
        "Cake slice": 20,
        "Water bottle": 50
        }

price = {
        "Chocolates": 1.50,
        "Sandwiches": 4.10,
        "Cookies": 2.0,
        "Cake slice": 3.0,
        "Water bottle": 1.0
        }

total_stock_value_of_cafe = 0

for item in menu:
    total_stock_of_each_item = stock[item]
    each_item_value = price[item]
    total_price_for_each_item = total_stock_of_each_item * each_item_value
    total_stock_value_of_cafe += total_price_for_each_item

print("Cafe's total stock value is: £{}".format(total_stock_value_of_cafe))
