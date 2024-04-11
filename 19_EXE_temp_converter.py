# We will create a program that converts temperature from centigrade to farenheight, and vice versa

# lets collect user units input
unit_from = input("What unit are you converting from? (C or F): ").capitalize()
unit_to = input("What unit are you converting to: (C or F): ").capitalize()

# collect temperature data
temp = float(input("Type your temperature: "))

# conditionals
if unit_from == "C":
    result = temp * 32
    print(f"Your Temperature is: {round(result, 1)}{unit_to}")
    
elif unit_from == "F":
    result = temp / 32
    print(f"Your Temperature is: {round(result, 1)}{unit_to}")
    
else:
    print(f"{unit_from} is invalid! Type in a valid unit")