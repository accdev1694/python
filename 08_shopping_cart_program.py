# Lets create a shopping cart program


# It takes the product and quantity from the user
product = input("Select a Product:")
quantity = int(input(f"How many {product}s would you like?"))
currency = input("What currency are you paying with? use a symbol:")

# It already has a price to each item
price = 12.5

# Calculates total
total = price * quantity

# display total to user
print(f"Your total is {currency}{total}")
