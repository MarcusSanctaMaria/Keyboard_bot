#Keyboard bot program
#Bugs - phone number input allows letters
#     - Name input allows numbers
#Known bugs
# Final printout is not printing customer details correctly
#

import sys
import random
from random import randint



# List of random names
names = ["Mark", "Pheobe", "Ochre", "Jill", "Johnson", 
         "Vector", "Kiara", "Louis", "Jodi", "Lily"]

# List of keyboards
keyboard_names = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch', 'Black Switch', 'Green Switch', 
                    'White Switch', 'Silver Switch', 'Grey Switch', 'Navy Switch', 'Jade Switch', 'Gold Switch']

#lists of keyboard prices
keyboard_prices = [79.99, 74.99, 74.99, 84.99, 89.99, 79.99, 84.99, 79.99, 84.99, 89.99, 89.99, 89.99]

# List to store ordered keyboards
order_list = []

# List to store keyboard prices
order_cost = []

#Customer detail dictionary 
customer_details = {}

#Validtes inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid: 
        response = input (question)
        if response != "":
            return response.title() 
        else:
            print ("This cannot be blank")

#Validtes inputs to check if they are an integer.
def val_int(LOW, HIGH, question):
    while True:
        try:
            num = int(input(question))
            if num >= 1 and num <= 2:
                return num
            else: 
                print("Please enter a number between", LOW, "and " , HIGH )
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter a number between", LOW, "and " , HIGH )





# Welcome message with random name
def welcome():
    """
Purpose: To generate a random name from the list and print out a welcome message 
Parameters: None 
Returns: None

    """
    
    
    num = randint(0,9)
    name = (names[num])
    print("** Welcome to Karlos' Kool Keyboards **")
    print("** My name is", name ,"**")
    print("** I will be here to help you order your new Kool Keyboard **")


# Menu for pickup or delivery 
def order_type():
    del_pick = ""
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between, {LOW} and {HIGH} ")
    print ("Is your order for pickup or delivery?")
    print (" For pickup enter 1.")
    print (" For delivery enter 2.")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Pickup")
        del_pick = "pickup"
        pickup_info()
        

    else:
        print ("Delivery")
        delivery_info()
        del_pick = "delivery"
    return del_pick



# Pick up information - name and phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    #print (customer_details ['name'])

    question = ("Please enter your phone number ")
    customer_details["phone"] = not_blank(question )
    #print (customer_details ['phone'])
    print(customer_details)


# Delivery information  - name, address and phone number

def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details ['name'])

    question = ("Please enter your phone number ")
    customer_details["phone"] = not_blank(question )
    print (customer_details ['phone'])

    question = ("Please enter your house number ")
    customer_details["house"] = not_blank(question )
    print (customer_details ['house'])

    question = ("Please enter your street name ")
    customer_details["street"] = not_blank(question )
    print (customer_details ['street'])

    question = ("Please enter your suburb ")
    customer_details["suburb"] = not_blank(question )
    print (customer_details ['suburb'])
 

# Keyboard menu
def menu():
    number_keyboard = 12

    for count in range (number_keyboard):
        print("{} {} ${:.2f}" .format(count+1,keyboard_names[count],keyboard_prices[count]))



# Choose total number of keyboards - max 5 
# Keyboard ordering - from menu - print each keyboard ordered with cost 
def order_keyboard():
    # Ask for total number of keyboards for order
    num_keyboards = 0

    while True:
        try:
            num_keyboards = int(input("How many keyboards do you want to order? "))
            if num_keyboards >= 1 and num_keyboards <= 5:
                break
            else:
                print("Your order must be between 1 and 5 keyboards.")
        except ValueError:
            print("That is not a valid number.")
            print("Please choose a number between 1 and 5.")

    # Choose keyboard from menu
    for item in range(num_keyboards):
        while num_keyboards > 0:
            while True:
                try:
                    keyboard_ordered = int(input("Please choose your keyboards by entering the number from the menu. "))
                    if keyboard_ordered >= 1 and keyboard_ordered <= 12:
                        break
                    else:
                        print("Your keyboard order must be between 1 and 12 keyboards.")
                except ValueError:
                    print("That is not a valid number.")
                    print("Please choose a number between 1 and 12.")
            keyboard_ordered = keyboard_ordered-1
            order_list.append(keyboard_names[keyboard_ordered])
            order_cost.append(keyboard_prices[keyboard_ordered])
            print("{} ${:.2f}" .format(keyboard_names[keyboard_ordered],keyboard_prices[keyboard_ordered]))
            num_keyboards = num_keyboards-1


# Print order out - including if order is delivering or pick up and names and price of each keyboard - total cost including any delivery charge 
def print_order(del_pick):
    total_cost = sum(order_cost)
    print("Your Details:")
    if del_pick == "pickup":
        print("Your order is for Pickup.")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']}")
        print ("Thank you for shopping with Karlos' Kool Keyboards. We will send you a text on when your new keyboard is ready to be picked up.")
    elif del_pick == "delivery":
        print("Your order is for Delivery. A $9.00 delivery will be applied.")
        total_cost = total_cost + 9
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']} \nCustomer Address: {customer_details['house'] } {customer_details['street']} {customer_details['suburb']} ")
    print()
    print("Your Order Details:")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}" .format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost:")
    print(f"${total_cost:.2f}")
    print("Thank you for shopping with Karlos' Kool Keyboards! The keyboard will be sent to you soon.")


# Ability to cancel or proceed with order
def confirm_cancel():
    print("Please confrim your order.")
    print("For confirm please enter 1")
    print("For cancel enter 2")
    while True:
        try:
            Confirm = int(input("Please enter a number "))
            if Confirm >= 1 and Confirm <= 2:
                if Confirm == 1:
                    print("Order Confirmed.")
                    print("Your order has been sent to our company")
                    print("Your brand new keyboard will be with you shortly.")
                    new_exit()
                    break

                elif Confirm == 2:
                    print("Your Order has been Cancelled.")
                    print("Your can restart your order or exit the BOT.")
                    new_exit()
                    break
            else:
                print("The number must be 1 or 2")   
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


# Option for new order or to exit 
def new_exit():
    print("Do you want to start another order or exit?")
    print("To start another order, please enter 1")
    print("To exit the BOT, please enter 2")
    while True:
        try:
            order_exit = int(input("Please enter a number "))
            if order_exit >= 1 and order_exit <= 2:
                if order_exit == 1:
                    print("New Order")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main()
                    break

                elif order_exit == 2:
                    print("Exit")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    sys.exit
                    break
            else:
                print("The number must be 1 or 2")   
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")



# Main function 
def main():
    
    """
    Purpose:To run all functions
    Parameters: None 
    Returns: None

    """
    welcome()
    del_pick = order_type()
    menu()
    order_keyboard()
    print_order(del_pick)
    confirm_cancel()

main()