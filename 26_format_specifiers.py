# They are usd in f-strings to format a string based on the 
# values that are used in them

# it follows a {value:flag} pair format


# lets create some variables of student gps's
gpa = 2.3345
quantity = 1000000

# 01:---> Set Decimal Places <---
# lets print out GPA and set it to 2 decimal places(:.2f)
print(f"Dan's GPA is #{gpa:.2f}")           # returns (#2.33)

# 02: ---> Allocate Output Spaces <---
# lets print out GPA and allocate 10 spaces to display the output(:10)
print(f"Joy's GPA is #{gpa:10}")            # returns (#    2.3345)

# 03:---> Add Padding <---
# lets add 0s as padding to the 10 spaces allocated to GPA(:010)
print(f"Joy's GPA is {gpa:010}")           # returns (#00002.3345) 

# 04: ---> Justify Left <---
# lets justify the output left and push the spaces right
print(f"Joy's GPA is {gpa:<10}")           # returns(2.3345    )
 
# 05: ---> Justify Center <---
# lets justify the output center and push the spaces left and right
print(f"Joy's GPA is {gpa:^10}")           # returns(  2.3345  )

# 06: ---> Justify Right <---
# lets justify the output right and push the spaces left
print(f"Joy's GPA is {gpa:>10}")           # returns(    2.3345)

# 07: ---> Display Positive values <---
# display a plus sign for positive values. same works for  negatives
print(f"Joy's GPA is {gpa:+}")             # returns(+2.3345)
# you could also use a space to display positive numbers
print(f"Joy's GPA is {gpa: }")             # returns( 2.3345)

# 08: ---> Thousand Seperator <---
# lets format every 3 integers with and comma to signigy thousands
print(f"the quantity is {quantity:,}")      # returns(1,000,000)

# 09: ---> Mix flags <---
# lets mix decimal places with comma seperators
print(f"the quantity is {quantity:,.2f}")      # returns(1,000,000.00)

