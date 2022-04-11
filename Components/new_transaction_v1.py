print("Do you want to start another order or exit?")
print("To start another order, please enter 1")
print("To exit the BOT, please enter 2")
while True:
    try:
        Confirm = int(input("Please enter a number "))
        if Confirm >= 1 and Confirm <= 2:
            if Confirm == 1:
                print("New Order")
                break

            elif Confirm == 2:
                print("Exit")
                break
        else:
            print("The number must be 1 or 2")   
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")