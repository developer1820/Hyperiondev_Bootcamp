"""
Create a string. Use split mehod to create a list of words.
Using for loop find length of words.
In nested loop Using range(), create range of length.
Now Use if else conditional statement to print every even character in
string to upper case and print every odd character in lower case.
          for eg. 'Hyperiondev' becomes 'HyPeRiOnDeV'
"""

sentence = "My name is Aarti Kacha, i am a Student at HyperionDev \
and i am excited to learn Python."
list_of_words = sentence.split()
result = ""

for word in list_of_words:
    length_of_word = len(word)
    for char in range(length_of_word):
        if char % 2 == 0:
            result = result + word[char].upper()
        else:
            result = result + word[char].lower()
    result = result + " "
print(result)

"""
Using same string above, create for loop and find range of length of words.
Using if else conditional statement print every alternative words
to upper case follow by lower case. for eg. 'my name' becomes 'MY name'.
"""
new_sentence = ""

for i in range(len(list_of_words)):
    if i % 2 == 0:
        new_sentence = new_sentence + list_of_words[i].upper()
    else:
        new_sentence = new_sentence + list_of_words[i].lower()
    new_sentence = new_sentence + " "
print(new_sentence)
