# variables

# a variable is a container for storing values or data, it is reusable

number = 40            
# number is the variable name

print(number) 

# there are 3 ways of printing variables along with some text as follows:

# 01: string concatination
print("we have " + str(number) + " oranges left *")     
# str type casting of the number variable
# meaning convert the number to a string before concatinating it   

# 02: seperate argumnets
print("we have", number, "oranges left **") 
# seperate each argument with a comma

# 03: f strings or format strings
print(f"we have {number} oranges left ***")
# uses an f before the quotes and wraps the variables in curly braces

