# Your code here
"""
UNDERSTAND

We'll create a dicionary of words and their frequency as they appear in a text file we will read in to the program.
We can then make a historgram comprised of hash marks using this dictionary as a reference

PLAN:

We'll first read in this file, and itterate over the text, pushing each character of text to a new string if it is alphanumeric or 
a space.

We'll then convert the string to lowercase and split the individual strings into an array.


We'll then itterate over this list to create a dictionary of words and their frequency as they appear in the original list

We can then use this dictionary as a reference to print a number of hash. After building the dictionary, we will sort it with its keys in descending order, and alphabetically when there are two entries with keys that are equal.


"""

def histogram():
    with open("applications/histo/robin.txt") as f:
        newStr = ""
        word_dict = {}
        words = f.read()

        for char in words:
            if char.isalnum() == True or char.isspace() == True:
                newStr += char

        newStr = newStr.lower()
        str_list = newStr.split()

        for word in str_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        word_dict = sorted(word_dict.items(), key=lambda x: (-x[1],) + x[:1])

        print(word_dict)
        
histogram()
