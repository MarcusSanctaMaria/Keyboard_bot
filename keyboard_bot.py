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

# Validates input so it is not blank
# Takes question as the parameter inside the bracket
# Returns the response in title class if input is valid
def not_blank(question): # Defines the code as a not_blank function with question as parameter
    """
    Purpose: To make sure that the input is not left blank
    Parameters: None
    Returns: None
    """
    valid = False # Makes it so valid can be used for false
    while not valid: # While not false
        response = input(question) # Asks for user input using a string
        if response != "":  # Checks if the input is not blank, hense !=
            return response.title() # Returns the response in title class
        else: # Triggers if the input is blank
            print ("This cannot be blank")  # Prints the error message

# Validates input as letters
# Takes question as the parameter inside the bracket
# Returns the response in title class if input is valid
def check_string(question): # Defines the code as a check_string function with question as parameter
    """
    Purpose: To make sure that the input is set as an alphabetical character
    Parameters: None
    Returns: None
    """
    while True: # Creates a while loop
        response = input(question) # Asks for user for string input with question as parameter
        x = response.isalpha() # Checks that input is a letter by setting x to True
        if x == False: # If x is false, not a letter, this triggers
            print("Input must only contain letters.") # Prints error message
        else: # Triggers if x is True
            return response.title() # Returns response in title class

# Validates input as integers
# Takes question as parameter
def val_int(low, high, question): # Defines code as a val_int function with low, high, question as parameter
    """
    Purpose: To make sure that the input is set as an integer
    Parameters: None
    Returns: None
    """
    while True: # Creates a while loop
        try: # Triggers while the function is true
            num = int(input(question)) # Creates an integer input for the question (question is a parameter)
            if num >= low and num <= high: # Triggers if the input is greater to or equal to low (1) and less than or equal to high (2)
                return num # Returns and accepts input
            else: # Triggers if input is not within or equal to low and high
                print (f"Please enter a number between {low} and {high}") # Asks for the input again
        except ValueError: # Triggers if input is invalid (int() creates an invalid input when it is not an integer)
            print ("That is not a valid number") # Prints error message
            print (f"Please enter a number between {low} and {high}") # Asks for the input again

# Validates input as an NZ number
# Takes question as a parameter
def check_phone(question, PH_LOW, PH_HIGH): # Defines code as a check_phone function with question, PH_LOW, PH_HIGH as parameter
    """
    Purpose: To make sure that the phone number that is input is an integer and is valid to be an NZ number (between 7 and 10 digits)
    Parameters: None
    Returns: None
    """
    while True: # Creates a while loop
        try: # Triggers while the function is true
            num = int(input(question)) # Creates an integer input for the question (question is a parameter)
            test_num = num # Makes input equal the test_num variable
            count = 0 # Creates the variable count and sets it to 0
            while test_num > 0: # Creates a loop while the test_num variable is 0
                test_num = test_num//10 # Divides the variable test_num by 10
                count = count + 1 # Adds 1 to the variable count
            if count >= PH_LOW and count <= PH_HIGH: # Triggers if the count is greater than PH_LOW and less than or equal to PH_HIGH
                return str(num) # Returns and accepts input
            else: # Triggers if input is not above
                print("NZ Phone numbers must have between 7 and 10 digits.") # Prints error message
        except ValueError: # Triggers if input is invalid (int() creates an invalid input when it is not an integer)
            print("Please enter a number.") # Prints error message

# Welcome message with random name
def welcome(): # Defines code as a welcome function
    """
    Purpose: To generate a random name from the list and print
             out a welcome message
    Parameters: None
    Returns: None
    """
    num = randint(0, 9) # Chooses a random number between or equal to 0 and 9
    name = (names[num]) # Name will be chosen from list with the corresponding number taken from the randint above
    print("** Welcome to Karlos' Kool Keyboards **") # Prints a welcome message with asterisks
    print("** My name is", name, "**") # Continues welcome message using the random name chosen above
    print("** I will be here to help you order your new Kool Keyboard **") # Finishes welcome message


# Order type function. User chooses between Click & Collect and Delivery
def order_type(): # Defines the code as an order_type function
    '''
    Purpose: To create a menu for the user to choose between Click and Collect and Delivery
    Parameter: none
    Return: Returns if del_click is valid
    '''
    del_click = "" # Sets the variable del_click as blank
    question = (f"Enter a number between, {LOW} and {HIGH} ") # Sets the question variable to ask users to choose between the LOW (1) and HIGH (2)
    print ("Is your order for Click and Collect or delivery?") # Prints message
    print (" For Click and Collect enter 1.") # Prints message to indicate that Click and Collect is 1
    print (" For Delivery enter 2.") # Prints message to indicate that Delivery is 2
    delivery = val_int(LOW, HIGH, question) # Sets delivery to use the val_int fucntion to make sure that the user can only enter integers.  Uses LOW, HIGH and question as parameters
    if delivery == 1: # Triggers if the input is 1
        print ("Click and Collect") # Prints Click and Collect to let the user know they chose Click and Collect
        del_click = "Click and Collect" # Sets del_click as Click and Collect
        clickcollect_info() # Selects the clickcollect_info function
    elif delivery == 2: # Triggers if input is 2 
        print ("Delivery") # Prints Delivery to let the user know they chose Delivery
        delivery_info() # Selects the delivery_info function
        del_click = "delivery" # Sets del_click as delivery
    return del_click # Returns and accepts input



# Click and collect information - name and phone number
def clickcollect_info(): # Defines the code as a clickcollect_info function
    """
    Purpose: To collect the users information when the user chooses Click and Collect
    Parameters: None
    Returns: None
    """
    question = ("Please enter your name ") # Sets question to ask the user for their name
    customer_details['name'] = check_string(question) # Takes input from above and adds input to customer_details list as name. Then it validates inputs as letters
    print (customer_details['name']) # Prints out the customer's name

    question = ("Please enter your phone number ") # Sets question to ask the user for their phone number
    customer_details["phone"] = check_phone(question, PH_LOW, PH_HIGH)  # Takes input from above and adds input to customer_details list as phone. Then it validates input as a valid NZ number.  Uses question, PH_LOW and PH_HIGH as parameters
    print (customer_details['phone']) # Prints out customer's phone number

# Delivery information - name, phone number and address
def delivery_info(): # Defines the code as a delivery_info function
    """
    Purpose: To collect the users information when the user chooses Delivery
    Parameters: None
    Returns: None
    """
    question = ("Please enter your name ") # Sets question to ask the user for their name
    customer_details['name'] = check_string(question) # Takes input from above and adds input to customer_details list as name. Then it validates inputs as letters
    print (customer_details['name']) # Prints out the customer's name

    question = ("Please enter your phone number ") # Sets question to ask the user for their phone number
    customer_details["phone"] = check_phone(question, PH_LOW, PH_HIGH)  # Takes input from above and adds input to customer_details list as phone. Then it validates input as a valid NZ number
    print (customer_details['phone']) # Prints out customer's phone number

    question = ("Please enter your house number ") # Sets question to ask the user for their house number
    customer_details["house"] = not_blank(question) # Takes input from above and adds input to customer_details list as house. Then it validates input as not blank
    print (customer_details['house']) # Prints out customer's house number

    question = ("Please enter your street name ") # Sets question to ask the user for their street name
    customer_details["street"] = check_string(question) # Takes input from above and adds input to customer_details list as street. Then it validates inputs as letters
    print (customer_details['street']) # Prints out customer's street name

    question = ("Please enter your suburb ") # Sets question to ask the user for their suburb
    customer_details["suburb"] = check_string(question) # Takes input from above and adds input to customer_details list as suburb. Then it validates inputs as letters
    print (customer_details['suburb']) # Prints out customer's suburb

# Keyboard menu
def menu(): # Defines the code as a menu function
    """
    Purpose: To print out the keyboard menu
    Parameters: None
    Returns: None
    """
    number_keyboard = 12 # Sets number_keyboard variable to 12 because there are 12 items on the menu
    for count in range(number_keyboard): # For items within the range of 1 and 12
        print("{} {} ${:.2f}" .format(count+1, keyboard_names[count], # Prints out each item in the keyboard_names list with prices from keyboard_prices list. Each item is formatted
                                      keyboard_prices[count]))

# Keyboard ordering
def order_keyboard(): # Defines code as an order_keyboard function
    """
    Purpose: To ask the user how many keyboards they want to order with a maximum of 5
    Parameters: None
    Returns: None
    """
    # Ask for total number of keyboards for order
    num_keyboards = 0 # Sets num_keyboards (number of keyboards to be ordered) variable to 0
    NUM_LOW = 1 # Sets constant as 1
    NUM_HIGH = 5 # Sets constant as 5
    MENU_LOW = 1 # Sets constant as 1
    MENU_HIGH = 12 # Sets constant as 12
    question = (f"Please enter a number between {NUM_LOW} and {NUM_HIGH} ") # Sets the question variable to ask users to choose between the LOW (1) and HIGH (5)
    print("How many keyboards do you want to order? You can only order a maxiumum of 5.") # ASks the user how many keyboards they want to order
    num_keyboards = val_int(NUM_LOW, NUM_HIGH, question) # Sets num_keyboards to use the val_int fucntion to make sure that the user can only enter integers. Uses NUM_LOW, NUM_HIGH and question as parameters
    # Choose keyboard from menu
    for item in range(num_keyboards): # For keyboard(s) between 1 and 12 (num_keyboard corresponding to the number of the keyboard in the menu)
        while num_keyboards > 0: # Creates while loop that continues while the input (num_keyboards) is greater than 0
            print("Please choose the keyboard you would like to"
                  " order by entering the corresponding number on the menu.") # Prints the question asking users to choose which keyboard they want to order
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")  # Sets the question variable to ask users to choose between the LOW (1) and HIGH (12)
            keyboard_ordered = val_int(MENU_LOW, MENU_HIGH, question)  # Sets keyboard_ordered to use the val_int fucntion to make sure that the user can only enter integers. Uses MENU_LOW, MENU_HIGH and question as parameters
            keyboard_ordered = keyboard_ordered - 1 # Subtracts 1 from the keyboard_ordered variable to go down the list
            order_list.append(keyboard_names[keyboard_ordered]) # Adds keyboard_names corresponding to the keyboard_ordered number to the order_list
            order_cost.append(keyboard_prices[keyboard_ordered]) # Adds keyboard_prices corresponding to the keyboard_ordered number to the order_list
            print("{} ${:.2f}" .format(keyboard_names[keyboard_ordered],
                  keyboard_prices[keyboard_ordered])) # Prints out keyboard ordered with price
            num_keyboards = num_keyboards - 1 # Subtracts 1 from the num_keyboards variable to go down the list

# Prints out order
def print_order(del_click): # Defines function as a print_order function
    """
    Purpose: To print out the order. The order includes the customer details, order type, name and total order price.
    Parameters: del_click
    Returns: None
    """
    total_cost = sum(order_cost) # Sets the variable total_cost as the sum of numbers in the order_cost list
    print("Your Details:") # Prints message
    if del_click == "Click and Collect": # Triggers if the del_click is set to Click and Collect which was chosen at the beginning of program
        print("Your order is for Click and Collect.") # Prints message to indicate the order type
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']}")  # Prints out all of the customer's details (name and phone number)
    elif del_click == "delivery": # Triggers if the del_click is set to Delivery which was chosen at the beginning of program
        total_cost = total_cost + 9 # Adds the delivery cost of $9 to the total cost
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']} \nCustomer Address: {customer_details['house'] } {customer_details['street']} {customer_details['suburb']} ")
        # Prints out all of the customer's details (name, phone number and address)
        print("Your order is for Delivery. A $9.00 delivery will be applied.")
    print() # Prints out a blank space
    print("Your Order Details:") # Prints message
    count = 0 # Sets the count variable to 0
    for item in order_list: # Triggers loop for each of the items in the order_list list
        print("Ordered: {} Cost: ${:.2f}" .format(item, order_cost[count])) # Prints out the keyboard ordered with the cost next to it
        count = count+1 # Adds 1 to count 
    print() # Prints an empty line
    print("Total Order Cost:") # Prints message
    print(f"${total_cost:.2f}") # Prints total cost with proper formatting
    print("Thank you for shopping with Karlos' Kool Keyboards! The keyboard will be with you soon.") # Prints message


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