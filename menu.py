import os
import datetime

def print_menu():
    print("-" * 50)
    print(" Welcome to Warehouse PyControl  [" + get_date_time() + "]")
    print("-" * 50)

    print('[1] - Add Product to Catalog')
    print('[2] - Display Catalog')
    print('[3] - Display Out of Stock Products')
    print('[4] - Total Stock Value')
    print('[5] - Cheapest Product')
    print('[6] - Delete Product')
    print('[7] - Update Product Price')
    print('[8] - Update Product Stock')
    print('[9] - Display Top 3 Expensive Products')

    print('[s] - Save')
    print('[x] - Exit')

def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%x %H:%M")

def clear():      
    return os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    clear()
    print('-' * 76)
    print(text)
    print('-' * 76)

def print_product_info(prod):
    print(
            "| " +
            str(prod.id).rjust(3) + " | " + 
            prod.title.ljust(25) + " | " + 
            prod.category.ljust(12) + " | " + 
            str(prod.stock).rjust(7) + " | $" + 
            str(prod.price).rjust(12) + " |"
            )