keyboard_names = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch', 
                  'Black Switch', 'Green Switch', 'White Switch']

keyboard_prices = [80.00, 75.00, 75.00, 85.00, 90.00, 80.00, 85.00]

number_keyboard = 7

#print("How many keyboards would you like to order? ")
#num_keyboard = int(input())

for count in range (number_keyboard):
    print(count,keyboard_names[count],keyboard_prices[count])