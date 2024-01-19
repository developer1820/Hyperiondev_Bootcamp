"""
Write a input function asking user how many students are registering.
Using for loop iterate each student and enter their registeration number.
print registration number in txt file following dotted line.

"""

user_input = int(input("How many students are registering?:"))

for student in range(user_input):
    id_number_input = input("Please enter next student id number:")

    with open("reg_form.txt", "a") as file:
        file.write("\n")
        file.write(id_number_input)
        file.write("\n")
        file.write("_ _" * 7)
        file.write("\n")
