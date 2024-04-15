# the indexing operator [] helps us assess characters in a string
# to access the first character in a string [0]

num = "1234567890"
print(num[0])           # prints 1
print(num[1])           # prints 2
print(num[-1])          # prints last character 0
print(num[2:5])         # prints between indexes 2 and 5; excluding the end index

# by the way:
print(num[0:4])
print(num[:4])
# both output the same thing(first 4 digits excluding index 4)

# to print the last 4 digits:
print(num[6:])

# to print digit before last:
print(num[-2])
# and work your way backwards

# Steps
# prints every nth character of our string
print(num[::3])     # prints every 3rd character

