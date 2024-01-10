"""
Start

Create variable called sentance and store the line in a single string.

#create a vaiable called new_sentance and Using replace() function remove
    "!" (exclamation mark) and add " " (blank space) and print the line.

Using upper() function convert all the letters in uppercase,
    reprint the new_sentance.

Using revese slicing method ([::-1]) reverse the whole line and then
    reprint the new_sentance.

End

"""

sentance = "The!quick!brown!fox!jumps!over!the!lazy!dog."
new_sentance = sentance.replace("!", " ")
print(new_sentance)
print(new_sentance.upper())
print(new_sentance[::-1])
