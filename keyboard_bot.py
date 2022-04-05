#Keyboard bot program
#Bugs - phone number input allows letters
#     - Name input allows numbers
#Known bugs
# Final printout is not printing customer details correctly
#

import sys
import random
from random import randint



#list of random names
names = ["Mark", "Pheobe", "Ochre", "Jill", "Johnson", "Vector", "Kiara", "Louis", "Jodi", "Lily"]

#Customer detail dictionary 
customer_details = {}


#lists of keyboards

#lists of keyboard prices


#list to store ordered keyboards


#list to store keyboards prices 


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
                print("Please enter a number between", LOW, "and" , HIGH)
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter a number between", LOW, "and" , HIGH)





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
    question = (f"Enter a number between, {LOW} and {HIGH}")
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




# Choose total number of Pizzas - max 5 
# Keyboard ordering - from menu - print each pizza ordered with cost 





# Print order out - including if order is delivering or pick up and names and price of each pizza - total cost including any delivery charge 




# Ability to cancel or proceed with order



# Option for new order or to exit 




# Main function 
def main():
    
    """
    Purpose:To run all functions
    Parameters: None 
    Returns: None

    """
    welcome()
    del_pick = order_type()


main()