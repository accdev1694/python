# Compound Interest Calculator
# we create a calculator program for generating the 
# total amount from an investment over a period of time - A = P*(1+r/n)^(nt)

principal = 0           # initial investment
rate = 0                # interest rate
time = 0                # time in years

# collect the principal amount from user (must not be negative) and convert to float
principal = float(input("what is your principal? "))
while principal < 0:
    print("principal cannot be less than 0")    
    break

# collect the rate from user (must not be negative) and convert to float
rate = float(input("what is your rate? "))
while rate < 0:
    print("your rate cannot be a negative number")
    break

# collect the principal amount from user (must not be negative) and convert to integer
time = int(input("how many years? "))
while time < 0:
    print("cannot be less than 1 year")
    break

amount = principal * pow((1 + rate / 100), time)                        # A = P*(1+r/n)^t

print((f"your compound Interest over {time}yrs is £{amount:.2f}"))      # round to 2 decimal places