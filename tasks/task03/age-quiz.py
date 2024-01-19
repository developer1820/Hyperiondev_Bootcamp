"""
Start

Ask customer to enter their age and store the value in int format in age variable.

Use if, elif, else conditional statement to evaluate below conditions.

If the customer's age is more than 100 then print statement "Sorry, you are dead".

If the customer's age is 65 or more than that then print statement "enjoy your retirement".

If the customer's age is 40 or more than that then print statement "you are over the hill".

If the customer's age is 21 then print statement "congrets on your 21st!!".

If the customer's age is less than 13 then print statement "You are qualify for the kiddie discount"..

Else print statement "age is but a number".

End

"""

#Ask customer to enter their age and store the value in int format in age variable.
age = int(input("Please enter your age:"))

#Use if, elif, else conditional statement to evaluate below conditions.
#If the customer's age is more than 100 then print statement "sorry, you are dead".
if age>100:
    print("Sorry, you are dead.")

#If the customer's age is 65 or more than that then print statement "enjoy your retirement".
elif age>=65:
    print("Enjoy your retirement!")

#If the customer's age is 40 or more than that then print statement "you are over the hill".
elif age>=40:
    print("You are over the hill.")

#If the customer's age is 21 then print statement "congrets on your 21st!".
elif age==21:
    print("Congrates on your 21st!")

#If the customer's age is less than 13 then print statement "You are qualify for the kiddie discount"..
elif age<13:
    print("Yor are qualify for the kiddie discount.")

#Else print statement "age is but a number".
else:
    print("Age is but a number.")