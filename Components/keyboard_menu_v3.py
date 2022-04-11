# List of keyboard names
keyboard_names = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch', 
                  'Black Switch', 'Green Switch', 'White Switch']

# List of keyboard prices
keyboard_prices = [79.99, 74.99, 74.99, 84.99, 89.99, 79.99, 84.99]

def menu():
    number_keyboard = 7

    for count in range (number_keyboard):
        print("{} {} ${:.2f}" .format(count+1,keyboard_names[count],keyboard_prices[count]))

menu()