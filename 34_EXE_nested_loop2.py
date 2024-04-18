# Create a Rectangle
# we create a nested loop for dsiplay a rectangle grid

# collect user input for rows, columns and shape symbol
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
shape = input("Enter a shape to use: ")

for char in range(rows):                # iterate over each character in rows
    for chars in range(columns):        # nest iteration of each column caharcter
        print(f"{shape}",  end='')      # print shape horizontally
    print()                             # move to next line after each iteration