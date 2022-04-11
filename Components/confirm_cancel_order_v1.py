print("Please confrim your order.")
print("For confirm please enter 1")
print("For cancel enter 2")
while True:
    try:
        Confirm = int(input("Please enter a number "))
        if Confirm >= 1 and Confirm <= 2:
            if Confirm == 1:
                print("Order Confirmed.")
                break

            elif Confirm == 2:
                print("Order Cancelled.")
                break
        else:
            print("The number must be 1 or 2")   
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")