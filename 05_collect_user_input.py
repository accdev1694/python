# Collecting user input

# lets send a user some prompt to collect their name and age
user_name = input("What is your name?")
user_age = input("How old are you?")

# print this information back to the user
print(f"Your name is {user_name}, and you are {user_age} years old")

# lets increment the age
# first, convert the age into an integer

user_age = input("How old are you again?")
user_age = int(user_age) + 1
print(f"Your name is still {user_name}, but you are now {user_age} years old")
