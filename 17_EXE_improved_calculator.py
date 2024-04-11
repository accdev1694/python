# Lets create a very simple calculator program

# collect user input to select an operator
operator = input("select an operator (+ - * /)")

# collect user input to select numbers
number_one = float(input("select the first number"))
number_two = float(input("select the second number"))
    
# calculations
addition = number_one + number_two
subtraction = number_one - number_two
multiplication = number_one * number_two
division = number_one / number_two

# conditionals    
if operator == "+":
    print(f"the sum of {number_one} and {number_two} is: {round(addition, 2)}")
    
elif operator == "-":
    print(f"the difference between {number_two} and {number_one} is: {round(subtraction, 2)}")
    
elif operator == "*":
    print(f"the product of {number_one} and {number_two} is: {round(multiplication, 2)}")
    
elif operator == "/":
    print(f"the quotient of {number_one} and {number_two} is: {round(division, 2)}")
    
else:
    print("A valid operator has not been selected")
    
    

    