"""
Program: Warehouse Control
Author: Andrew Corona
Functionality:
    - Register Products
        - id (auto generated)
        - title
        - category
        - price
        - stock
"""

#imports
from menu import clear, print_menu, print_header, print_product_info
from product import Product
import sys
import pickle

#global vars
catalog = []
next_id = 1

#functions

def serialize_data():
    try:
        writer = open('warehouse.data', 'wb') #wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data Serialized! **")
    except:
        print("** Error, data was not saved, use option [s] to manually save **")

def deserialize_data():
    global next_id

    try:
        reader = open('warehouse.data', 'rb') #rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        #you could do catalog instead of temp_list however it is more risky incase you have a bad file / info

        for prod in temp_list:
            catalog.append(prod)  #take all prod objects in temp list (which was filled by pickle.load(reader) and append to original catalog)

        #we need to get the last used id, [-1] is how you read objects in a array backwards
        last = catalog[-1]
        next_id = last.id + 1


        how_many = len(catalog)
        print(str(how_many) + " objects have been loaded")

    except:
        print("** Error: no data file found **")

def register_product():
    global next_id #have to do this because python is picky with global variables

    try:
        print_header("Register your new product")
        title = input('Please provide the Title: ')
        cat = input('Please provide the Category: ')
        stock = int(input('Please provide initial Stock: '))
        price = float(input('Please provide the Price: '))

        #validations
        if(len(title) <1):
            print("*Error: Title should not be empty")

        product = Product(next_id, title, cat, stock, price)
        next_id += 1
        catalog.append(product)

    except:
        print("** Error: make sure to enter only integers for stock and price")

def display_catalog():
    print_header("Current Catalog")
    for prod in catalog:
        print_product_info(prod)
        #HOMEWORK - DISPLAY CATEGORIES IN THEIR OWN SLOTS
 
def display_outofstock():
    print_header("Your current Out of Stock Products")
    for prod in catalog:
        if(prod.stock == 0):
            print_product_info(prod)

def display_totalstock():
    print_header("Your total stock worth")
    total_value = 0
    for prod in catalog:
        #better way of doing this is total_value += total_value + (prod.stock * prod.price)
        total_value = total_value + (prod.stock * prod.price)
    print("$" + str(total_value))

def display_cheapest():
    print_header("Cheapest item in stock")
    #instead of making a ceiling for the integer, just assign lowest_price to catalog[0], setting it to the first object
    lowest_price = sys.float_info.max
    lowest_item = ""
    for prod in catalog:
        if prod.price < lowest_price:
            lowest_price = prod.price
            lowest_item = prod.title
    print("The Cheapest item is: " + lowest_item)

def delete_product():
    print_header("Find Product ID:(#) in the list")
    display_catalog()
    selected_item = int(input("Enter ID for product to be deleted: "))

    found = False
    for prod in catalog:
        if (prod.id == selected_item):
            found = True
            catalog.remove(prod)
            print("Item deleted")

    if(not found):
        print("** Incorrect ID selected **")

def update_price():
    print_header("Find Product ID:(#) in the list")
    display_catalog()

    try:
        selected_item = int(input("Enter ID for product to be updated: "))
        
        found = False
        for prod in catalog:
            if (prod.id == selected_item):
                found = True
                new_price = float(input("Please input the new price for the product: "))
                prod.price = new_price
                print("Product Price updated")

        if(not found):
            print("** Incorrect ID selected **")

            return found
    except:
        print("** Unexpected Error **")
        return False

def update_stock():
    print_header("Find Product ID:(#) in the list")
    display_catalog()

    try:
        selected_item = int(input("Enter ID for product to be updated: "))

        found = False
        for prod in catalog:
            if (prod.id == selected_item):
                found = True
                new_stock = int(input("Please input the new stock for the product: "))
                prod.stock = new_stock
                print("Product Stock updated")

        if(not found):
            print("** Incorrect ID selected **")
    except:
        print("** Unexpected Error **")
        return False

def most_expensive_items():
    print_header("Top 3 most expensive products")
    prices = []
    for prod in catalog:
        prices.append(prod.price)
    prices.sort(reverse=True)
    print(prices[0])
    print(prices[1])
    print(prices[2])


#instructions

deserialize_data()
input("Press Enter to conitnue...")

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Please select an option: ')

    if(opc == '1'):
        register_product()
        serialize_data()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_outofstock()
    elif(opc == '4'):
        display_totalstock()
    elif(opc == '5'):
        display_cheapest()
    elif(opc == 's'):
        serialize_data()
    elif(opc == '6'):
        delete_product()
        serialize_data()
    elif(opc == '7'):
        if(update_price()):
            serialize_data()
    elif(opc == '8'):
        if(update_stock()):
            serialize_data()
    elif(opc == '9'):
        most_expensive_items()

    input('Press Enter to continue...')

print('Good Bye!')