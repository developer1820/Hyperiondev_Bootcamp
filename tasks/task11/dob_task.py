"""
Create a txt file, write names and dobs(date of births).
Write a programme to read values from txt file.
Create 3 empty list to store values later in programme.
Using for loop and nested for loop remove individual value and add
it in a list.
"""

names_dobs_list = []
names_list = []
dobs_list = []

with open("DOB.txt", "r") as file:
    record_list = file.read().split("-")
    for line in record_list:
        for word in line.strip().split("\n"):
            names_dobs_list.append(word)

"""
Use for loop to find length of a list. And using if else statement
seperate names, dobs and add it in a appropriate lists.
"""

for index_num in range(len(names_dobs_list)):
    if index_num % 2 == 0:
        names_list.append(names_dobs_list[index_num])
    else:
        dobs_list.append(names_dobs_list[index_num])

"""
Use for loop to print individual values (name, dob) in Name and Birthdate.
"""

print('\033[1m' + "Name" + '\033[0m')
for name in names_list:
    print(name)

print()

print('\033[1m' + "Birthdate" + '\033[0m')
for dob in dobs_list:
    print(dob)
