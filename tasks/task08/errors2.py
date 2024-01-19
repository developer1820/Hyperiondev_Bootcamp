# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program,
#   look at the error messages, and find and fix the errors.

"""
Name 'Lion' is not define, value should be in single or double quote,
    add quote to name Lion, its syntax error.
"""
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

"""
Formatted string missing, add formatted string, its a logical error.
And variable is on wrong place so change variable, for eg, animal_type comes
    instead of number_of_teeth, its a logical error.
"""

full_spec = f"This is a {animal}. It is a {animal_type} and \
    it has {number_of_teeth} teeth."

"""
Parentheses missing, add parenthesis, its a syntax error.
"""
print(full_spec)
