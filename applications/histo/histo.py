# Your code here
"""
UNDERSTAND

We'll create a dicionary of words and their frequency as they appear in a text file we will read in to the program.
We can then make a historgram comprised of hash marks using this dictionary as a reference.

PLAN:

We'll first read in this file, and itterate over the text, pushing each character of text to a new string if it is alphanumeric or 
a space.

We'll then convert the string to lowercase and split the individual strings into an array.

We'll then itterate over this list to create a dictionary of words and their frequency as they appear in the original list

We can then use this dictionary as a reference to print a number of hash marks. After building the dictionary, we will sort it with its keys in descending order, and alphabetically when there are two entries with keys that are equal.

We'll also want to sort the list by length of keys so that we can find the longest word, find its length, and add two so we have a value from which we can subtract the length of keys from 
each entry to format the output in a justified way.

With all of this in place, all we have to do is loop through our sorted dictionary, and print the key, correct number of spaces, and correct number of hash marks on each line. 




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

        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1],) + x[:1])

        longest_sort = sorted(word_dict.items(), key=lambda x: len(x[0]), reverse=True)

        spaces = len(longest_sort[0][0]) + 2 

        

        for entry in sorted_words:
            print(entry[0] + ((spaces - len(entry[0])) * " ") + (entry[1] * "#")   )


        
        
histogram()
