"""
Start

create variable and assign its initial value 2.

Create for loop using range.

Write if else statement using condition.

Firt minus 2 from each variable and then add 2 to initial variable
    each time when code runs.

Print a pattern.

End
"""

# Create a variable and assign initial value to 2.
decrement_by = 2

# Create for loop, use if else statemnt draw a pattern by using condition.
for each in range(1, 10):
    if each > 5:
        print("*" * (each - decrement_by))
        decrement_by = decrement_by + 2
    else:
        print("*" * each)
