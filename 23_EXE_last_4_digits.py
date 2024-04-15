# lets create a program to extract the last 4 digits of a debit card

# collect number from user
card_num = input("type in your debit card number")

# extract the last 4 digits and print
last_four = card_num[-4:]
print(f"the last four digits of your card number is ****-****-****-{last_four}")
