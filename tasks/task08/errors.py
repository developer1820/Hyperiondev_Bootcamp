"""
This example program is meant to demonstrate errors.
There are some errors in this program. Run the program,
    look at the error messages, and find and fix the errors.
"""

# Parentheses () is  missing, add parentheses, its a syntax error.

print("Welcome to the error program")

"""
Unexpected indentation and parentheses was missing,
    remove indentation and add parentheses,
its a syntax error.
"""

print("\n")


# Variables declaring the user's age, casting the str to an int,
#   and printing the result

"""
Unexpected indentation and two assignment operator(==). only one asignment
operator needed and remove indentation, its a syntax error.
And whole string can not be converted into an integer so remove
"years old", its a runtime error.
"""

age_Str = "24"

"""
Unexpected indentation, remove indentation, its a syntax error.
"""

age = int(age_Str)

"""
Unexpected indentation, remove leading space, its a syntax error.
you can not concatenate string with int so use formatted string to add age
into string, it's a runtime error.
"""

print(f"I'm {age} years old.")

# Variables declaring additional years and printing the total years of age

"""
Unexpected indentation, remove space, its a syntax error.
"""

years_from_now = "3"

"""
Unexpected indentation, remove space, its a syntax error.
years_from_now is string so not able to add to age which is int type,
    therefore, converting years_from_now into int and adding both.
it's a runtime error.
"""

total_years = age + int(years_from_now)

"""
Missing parentheses, add parentheses, its a syntax error. wrong variable
"answer_years" instead we need "total_years", so its a logical error.
And we can not concatenate int to str so using formatted string
we can solve a problem, its a runtime error.
"""

print(f"The total number of years: {total_years}")

# Variable to calculate the total amount of months
# from the total amount of years and printing the result

"""
Variable was not defined, its a spelling mistake , "total" variable
    is replaced by "total_years", its a runtime error.
"""

total_months = total_years * 12

"""
Missing parentheses, add parentheses, its a syntax error.
6 month is not been added so we need to add 6 month into
    total month to get correct answer, its a logical error.
"""

total_months += 6
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

# HINT, 330 months is the correct answers
