# List of keyboard names
keyboard_names = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch', 
                  'Black Switch', 'Green Switch', 'White Switch']

# List of keyboard prices
keyboard_prices = [79.99, 74.99, 74.99, 84.99, 89.99, 79.99, 84.99]

# List to store ordered keyboards
order_list = ['Blue Switch', 'Red Switch', 'Brown Switch', 'Clear Switch']
# List to store keyboard prices
order_cost = [79.99, 74.99, 74.99, 84.99]

customer_details = {'name': 'Marcus', 'phone': '14245235325', 'house': '54', 'street': 'Harvey', 'suburb': 'Flat Bush'}

#print("\n", customer_details['name'],"\n", customer_details['phone'],"\n", customer_details['house'],"\n", customer_details['street'],"\n", customer_details['suburb'])

print("\n Customer Name: {} \n Customer Phone:{}\n Customer House Number:{}\n Customer Street Name:{}\n Customer Suburb:{} ".format(customer_details['name'], 
    customer_details['phone'],customer_details['house'],customer_details['street'],customer_details['suburb']))

count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}" .format(item, order_cost[count]))
    count = count+1