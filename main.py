# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



resturant = "Foodie Doodie"
# Using a nested dictionary for the menu
menu = {
    "sku1": {
        "name": "Hamburger",
        "price": 6.51
    },
    "sku2": {
        "name": "Cheeseburger",
        "price": 7.75
    },
    "sku3": {
        "name": "Milkshake",
        "price": 5.99
    },
    "sku4": {
        "name": "Fries",
        "price": 2.39
    },
    "sku5": {
        "name": "Sub",
        "price": 5.87
    },
    "sku6": {
        "name": "Ice Cream",
        "price": 1.55
    },
    "sku7": {
        "name": "Fountain Drink",
        "price": 3.45
    },
    "sku8": {
        "name": "Cookie",
        "price": 3.15
    },
    "sku9": {
        "name": "Brownie",
        "price": 2.46
    },
    "sku10": {
        "name": "Sauce",
        "price": 0.75
    }
}
app_actions = {
    "1": "Add a new menu item to cart",
    "2": "Remove an item from the cart",
    "3": "Modify a cart item's quantity",
    "4": "View cart",
    "5": "Checkout",
    "6": "Exit"
}

SALES_TAX_RATE = 0.07
cart = {}
def display_menu():
    print("****Menu****")
    for sku in menu:
        sku_no=sku[-1]
        product_name=menu[sku]['name']
        product_price=menu[sku]['price']
        print(f'{sku_no}: {product_name} for {product_price}')
display_menu()
def add_to_cart(sku,quants):
    if sku in menu:
        if sku in cart:
            cart[sku]+=quants
        else:
            cart[sku]=quants
            print(f'Added {quants} of {menu[sku]['name']} to the cart.')
    else:
        print("SKU not found")
def remove_from_cart(sku):
    if sku in cart:
        cart.pop(sku)
        print(f'removed {menu[sku]['name']} from the cart')
    else:
        print('Sku not in the cart')
def modify_cart(sku,quants):
    if sku in cart:
        if quants>0:
            cart[sku]=quants
            print(f'Modified {menu[sku]['name']} quantity to {quants} in the cart')
        else:
            remove_from_cart(sku)
    else:
        print("Product doesn't exist in cart")
def view_cart():
    print("****CART****")
    subtotal=0
    for sku in cart:
        if sku in menu:
            quantity=cart[sku]
            subtotal+=quantity*menu[sku]['price']
            print(f"{quantity} x {menu[sku]['name']}")
    print(f"Total: {(subtotal*SALES_TAX_RATE)+subtotal}")
def checkout():
    print("***CHECKOUT***")
    view_cart()
    print("order was submitted")


def get_sku_and_quantity(sku_prompt, quantity_prompt=None):
    item_sku = input(sku_prompt+" ")
    # String concatenate "sku" to the beginning of the entered SKU number
    item_sku = "sku" + item_sku
    # If the quantity prompt is provided, we should get input from the user
    if quantity_prompt:
        # Use the quantity prompt to get input from the user
        quantity = input(quantity_prompt+" ")
        # If the user typed a non-digit value, default quantity to 1
        if not quantity.isdigit():
            quantity = 1
        quantity = int(quantity)

        return item_sku, quantity
    # Quantity prompt is None meaning we do not need to get input for quantity
    else:
        return item_sku
def order_loop():
    print(f"welcome to {resturant}")
    running=True
    print("Ordering actions")
    while running:
        for action in app_actions:
            print(f"({action}) {app_actions[action]}")

        action=int(input("input action \n"))
        if action==1:
            display_menu()
            sku,quantity=get_sku_and_quantity("Please enter the sku number you want to order: ","Please enter the "
                                                                                                "quantity")
            add_to_cart(sku,quantity)
        elif action==2:
            display_menu()
            sku,quantity=get_sku_and_quantity("Please enter the sku number you want to remove: ")
            remove_from_cart(sku)
        elif action==3:
            display_menu()
            sku,quantity=get_sku_and_quantity("Please enter the sku number you want to modify: ","Please enter the quantity")
            modify_cart(sku,quantity)
        elif action==4:
            view_cart()
        elif action==5:
            checkout()
        elif action==6:
            running=False
        else:
            print("Please enter a valid prompt")

order_loop()
