# Lets create a shopping cart program


# It takes the product and quantity from the user
product = input("Select a Product:")
quantity = int(input(f"How many {product}s would you like?"))
currency = input("What currency are you paying with? use a symbol:")

# It already has a price to each item
price = 12.53

# Calculates total
total = price * quantity

# display total to user and round to nearest 1 decimal place (round() method)
print(f"Your total is {currency}{round(total, 1)}")

