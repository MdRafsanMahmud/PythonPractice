# Create a variable called 'price' as a string with the value '19.99'.
price = '19.99'

# Convert 'price' to a float and store it in a new variable called 'price_float'.
price_float = float(price)

# Create a variable called 'quantity' as an integer with a value 5.
quantity = 5

# Calculate the total cost by multiplying 'price_float' and 'quantity', and store it in a variable called 'total_cost'.
total_cost = price_float * quantity

# Convert 'total_cost' to an integer (round down) and store it in a variable called 'total_cost_int'.
total_cost_int = int(total_cost)

# Print out 'price', 'price_float', 'quantity', 'total_cost', 'total_cost_int' along with their types.
print(f"Price: {price}","\nType:",type(price))
print(f"Price as float: {price_float}","\nType:",type(price_float))
print(f"Quantity: {quantity}","\nType:",type(quantity))
print(f"Total cost: {total_cost}","\nType:",type(total_cost))
print(f"Total cost as int: {total_cost_int}","\nType:",type(total_cost_int))

