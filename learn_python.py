# printing messages to the terminal or output window
print('hello') # add your message inside parenthesis, and inside quotes
print('welcome')

# varriables and data types
# a variable is a reusable container that represents some form of data

# STRINGS

#get user input, remove white spaces from start and end and capitalize
name = input('what is your name?').strip().title()

#remove white spaces from your string
# name = name.strip() 

# capitalize the first word in string
# name = name.capitalize()

# capitalize every word in string
# name = name.title()

#remove white spaces from start of string and capitalize
# name = name.strip().title()

#split string into first and last name
first, last = name.split(" ")


#output greeting of first name to console
print(f'my name {first}')
