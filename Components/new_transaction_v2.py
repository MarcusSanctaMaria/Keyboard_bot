import sys

# List to store ordered keyboards
order_list = []

# List to store keyboard prices
order_cost = []

#Customer detail dictionary 
customer_details = {}

def main():
    print("Start Again.")

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
