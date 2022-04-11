# List of keyboard names
keyboard_names = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch', 
                  'Black Switch', 'Green Switch', 'White Switch']

# List of keyboard prices
keyboard_prices = [79.99, 74.99, 74.99, 84.99, 89.99, 79.99, 84.99]

# List to store ordered keyboards
order_list = []
# List to store keyboard prices
order_cost = []

# List to store order cost

def menu():
    number_keyboard = 7

    for count in range (number_keyboard):
        print("{} {} ${:.2f}" .format(count+1,keyboard_names[count],keyboard_prices[count]))

menu()

# Ask for total number of keyboards for order
num_keyboards = 0

num_keyboards = int(input("How many keyboards do you want to order? "))

print(num_keyboards)

# Choose keyboard from menu
print("Please choose your keyboards by entering the number from the menu.")
for item in range(num_keyboards):
    while num_keyboards > 0:
        keyboard_ordered = int(input())
        order_list.append(keyboard_names[keyboard_ordered])
        order_cost.append(keyboard_prices[keyboard_ordered])
        print("{} ${:.2f}" .format(keyboard_names[keyboard_ordered],keyboard_prices[keyboard_ordered]))
        num_keyboards = num_keyboards-1

print(order_list)
print(order_cost)


# Countdown until all keyboards are ordered





# Print Order