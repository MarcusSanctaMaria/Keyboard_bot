import sys
import random
from random import randint
# Constants
LOW = 1  # LOW equals 1
HIGH = 2  # HIGH equals 2
PH_LOW = 7
PH_HIGH = 10
# List of random names
names = ["Mark", "Pheobe", "Ochre", "Jill", "Johnson",
         "Vector", "Kiara", "Louis", "Jodi", "Lily"]

# List of keyboard switches to choose from
keyboard_names = ['Blue Switch', 'Red Switch', 'Brown Switch',
                  'Clear Switch', 'Black Switch', 'Green Switch',
                  'White Switch', 'Silver Switch', 'Grey Switch',
                  'Navy Switch', 'Jade Switch', 'Gold Switch']

# Lists of keyboard prices
keyboard_prices = [79.99, 74.99, 74.99, 84.99, 89.99, 79.99,
                   84.99, 79.99, 84.99, 89.99, 89.99, 89.99]

# List to store ordered keyboards
order_list = []

# List to store keyboard prices
order_cost = []

# Customer detail dictionary
customer_details = {}

# A function that validtes inputs to check if they are blank
def not_blank(question): # Defines the function with the name not_blank
    valid = False 
    while not valid:
        response = input(question)
        if response != "":  # Checks if the input is blank
            return response.title()
        else:
            print ("This cannot be blank")  

def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters.")
        else: 
            return response.title()
# Validtes inputs to check if they are an integer.
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print (f"Please enter a number between {low} and {high}")
        except ValueError:
            print ("That is not a valid number")
            print (f"Please enter a number between {low} and {high}")

def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return str(num)
            else:
                print("NZ Phone numbers must have between 7 and 10 digits.")
        except ValueError:
            print("Please enter a number.")

# Welcome message with random name
def welcome():
    """
Purpose: To generate a random name from the list and print
         out a welcome message
Parameters: None
Returns: None

    """

    num = randint(0, 9)
    name = (names[num])
    print("** Welcome to Karlos' Kool Keyboards **")
    print("** My name is", name, "**")
    print("** I will be here to help you order your new Kool Keyboard **")


# Menu for Click and Collect or delivery
def order_type():
    del_click = ""
    question = (f"Enter a number between, {LOW} and {HIGH} ")
    print ("Is your order for Click and Collect or delivery?")
    print (" For Click and Collect enter 1.")
    print (" For delivery enter 2.")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Click and Collect")
        del_click = "Click and Collect"
        clickcollect_info()

    else:
        print ("Delivery")
        delivery_info()
        del_click = "delivery"
    return del_click



# Click and collect  information-name and phone number
def clickcollect_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details["phone"] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])
    print(customer_details)


# Delivery information  - name, address and phone number

def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details["phone"] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details["house"] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details["street"] = check_string(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details["suburb"] = check_string(question)
    print (customer_details['suburb'])

# Keyboard menu
def menu():
    number_keyboard = 12

    for count in range(number_keyboard):
        print("{} {} ${:.2f}" .format(count+1, keyboard_names[count],
                                      keyboard_prices[count]))

# Choose total number of keyboards-max 5
# Keyboard ordering-from menu-print each keyboard ordered with cost
def order_keyboard():
    # Ask for total number of keyboards for order
    num_keyboards = 0
    NUM_LOW = 1
    NUM_HIGH = 5
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("How many keyboards do you want to order? ")
    num_keyboards = val_int(NUM_LOW, NUM_HIGH, question)
    # Choose keyboard from menu
    for item in range(num_keyboards):
        while num_keyboards > 0:
            print("Please choose the keyboard you would like to"
                  " order by entering the corresponding number on the menu")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            keyboard_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            keyboard_ordered = keyboard_ordered - 1
            order_list.append(keyboard_names[keyboard_ordered])
            order_cost.append(keyboard_prices[keyboard_ordered])
            print("{} ${:.2f}" .format(keyboard_names[keyboard_ordered],
                  keyboard_prices[keyboard_ordered]))
            num_keyboards = num_keyboards - 1



# Print order out-including if order is delivering or Click and Collect and names
# and price of each keyboard-total cost including any delivery charge
def print_order(del_click):
    total_cost = sum(order_cost)
    print("Your Details:")
    if del_click == "Click and Collect":
        print("Your order is for Click and Collect.")
        print(f"Customer Name: {customer_details['name']}"
              "\nCustomer Phone Number: {customer_details['phone']}")
        print ("Thank you for shopping with Karlos' Kool Keyboards."
               "We will send you a text on when your new"
               "keyboard is ready to be collected.")
    elif del_click == "delivery":
        total_cost = total_cost + 9
        print(f"Customer Name: {customer_details['name']}"
              "\nCustomer Phone Number: {customer_details['phone']}"
              "\nCustomer Address: {customer_details['house'] }"
              "{customer_details['street']} {customer_details['suburb']} ")
    print()
    print("Your Order Details:")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}" .format(item, order_cost[count]))
        count = count+1
    print("Your order is for Delivery. A $9.00 delivery will be applied.")
    print()
    print("Total Order Cost:")
    print(f"${total_cost:.2f}")
    print("Thank you for shopping with Karlos' Kool Keyboards! The keyboard will be with you soon.")


# Ability to cancel or proceed with order
def confirm_cancel():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print("Please confrim your order.")
    print("For confirm please enter 1")
    print("For cancel enter 2")

    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print("Order Confirmed.")
        print("Your order has been sent to our company")
        print("Your brand new keyboard will be with you shortly.")
        new_exit()

    elif confirm == 2:
        print("Your Order has been Cancelled.")
        print("Your can restart your order or exit the BOT.")
        new_exit()

# Option for new order or to exit 
def new_exit():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print("Do you want to start another order or exit?")
    print("To start another order, please enter 1")
    print("To exit the BOT, please enter 2")
    order_exit = val_int(LOW, HIGH, question)

    if order_exit == 1:
        print("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()

    elif order_exit == 2:
        print("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()


# Main function 
def main():
    
    """
    Purpose:To run all functions
    Parameters: None 
    Returns: None

    """
    welcome()
    del_click = order_type()
    menu()
    order_keyboard()
    print_order(del_click)
    confirm_cancel()

main()