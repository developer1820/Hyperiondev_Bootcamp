"""
Start

Create 2 variable and assign its value to zero and create an empty list.

Create while loop and ask user to enter number,
 until user enter -1 and end the while loop.

Create for loop.
Add all the numbers enter by user, excluding -1 and divide by how many
    times numbers been enteres.

Print answer.

End

"""

# Create 2 variable and assign its value to zero and create an empty list

num_count = 0
user_entered_numbers = []
total_num = 0

# Create while loop and ask user enters number untill user enters -1,
#   add numbers to list.
while True:
    num_by_user = int(input("please enter number:"))
    if num_by_user == -1:
        break

    num_count = num_count + 1
    user_entered_numbers.append(num_by_user)

# Create for loop add all numbers and divide by its count of number.
for num in user_entered_numbers:
    total_num += num
print("The average of your numbers is: {:.2f}".format(total_num/num_count))
