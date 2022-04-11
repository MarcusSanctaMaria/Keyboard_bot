# List of keyboard names
keyboard_names = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch', 
                  'Black Switch', 'Green Switch', 'White Switch']

# List of keyboard prices
keyboard_prices = [79.99, 74.99, 74.99, 84.99, 89.99, 79.99, 84.99]

# List to store ordered keyboards
order_list = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch']
# List to store keyboard prices
order_cost = [79.99, 74.99, 74.99, 84.99]

count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}" .format(item, order_cost[count]))
    count = count+1