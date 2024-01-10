# Task - 2

"""
Start

Give a variable name (Full_Name) and ask customer to enter their full name.

Give a variable name (Age) and ask customer to enter their age.

Give a variable name (House_number) and ask customer to enter their
    house number.

Give a variable name (Street_name) and ask customer to enter their street name.

Then print all the above details creating a string in single line.

End

"""
# Give a variable name (Full_Name) and ask customer to enter their full name.
full_name = input("Please enter your full name:")

# Give a variable name (Age) and ask customer to enter their age.
age = int(input("Please enter your age:"))

# Give a variable name (House_number) and ask customer to
# enter their house number.
house_number = int(input("Please enter your house number:"))

# Give a variable name (Street_name) and ask customer to enter
# their street name.
street_name = input("please enter your street name:")

# Then print all the above details creating a string in single line.
print("Hello my name is {} and I am {} years old. My House Number is {} "
      "and my Street Name is {}.".format(full_name, age, house_number,
                                         street_name))
