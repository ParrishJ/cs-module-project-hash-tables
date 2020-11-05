import random

""" 
UNDERSTAND

A markov chains are sequences of words that appear to look gramatically correct but are in fact nonsensical.
We can generate a markov chain by creating a dictionary of words where the values of the dictionary are the words
that follow the keys in the dictionary as they appear in the original text.

We can use this dictionary and some helper methods to create our markov chain

PLAN

We'll split the words that we read from the document into an array. We'll then push all unique words as keys to our dictionary.
(we may have to account for punctuation in our words.) We'll then reitterate through our words list, adding the word after each word
to its corresponding place in the dictionary as a value. 

We'll then create three helper functions: pick_start(), pick_next(), and is_end().

pick_start() will randomly return a key from our dictionary. It will verify
that the key starts with either an uppercase letter or a quotation mark followed by an uppercase letter.
If the key does not meet this criteria, the key will be swapped out for another key.

pick_next() will take a string in and will do a lookup on our dictionary using that string, and will 
randomly select a value from that entry as the next word in our final sentence. If there is no value
for that entry in the dictionary, the function will return an empty string.

is_end() will take in a string and will check to see if it meets the criteria for being a stop word (that
it ends in ., ?, or !, or ends in a quotation mark immediately preceeded by one of these characters)


Using these three helper methods, we'll then combine them to create our sentences. We'll start by using pick_start()
to get our starting word and will then use a while loop to continue using pick_next() to add to our sentence until
we have reached a stop word which will be determined using is_end().
"""

# Read in all the words in one go
with open("applications\markov\input.txt") as f:
    word_dict = {}
    words = f.read()
    word_list = words.split()
    start_word = ""
    
    # TODO: analyze which words can follow other words
    # Your code here
    
    for word in word_list:

        if word in word_dict:
            pass
        else:
            """ word_dict[word] = "" """
            word_dict[word] = []

    for i in range(len(word_list) - 1):

        """ word_dict[word_list[i]] += ((word_list[i + 1]) + " ") """
        word_dict[word_list[i]].append(word_list[i + 1])

    def pick_start():
        start_word = random.choice(list(word_dict.keys()))
        if start_word[0].isupper():
            return start_word
        if start_word[0] == '"' and start_word[1].isupper():
            return start_word
        else:
            return pick_start()
    
    def pick_next(prev_str):
        next_str = ""
        if len(prev_str) == 0:
            return next_str
        
        next_str_list = word_dict[prev_str]
        
        if len(next_str_list) == 0:
            return next_str
        else:
            next_str = random.choice(next_str_list)
            return next_str


    def is_end(end_str):
        if len(end_str) == 0:
            return False
        if len(end_str) == 1 and end_str[0].islower():
            return False
        elif len(end_str) == 1 and end_str[0].isupper():
            return False
        elif end_str[-1] == "." or end_str[-1] == "?" or end_str[-1] == "!":
            return True
        elif len(end_str) > 1 and end_str[-2] == "." or end_str[-2] == "?" or end_str[-2] == "!" and end_str[-1] == '"':
            return True
        else:
            return False

    
    def return_markov():
        final_str = pick_start()
        continue_concat = True
        next_str = final_str
        while continue_concat == True:
            next_str = pick_next(next_str)
            
            if len(next_str) == 0:
                final_str = final_str
            else:
                final_str += (' '  + next_str )
            
            if is_end(next_str) == True:
                continue_concat = False
        return final_str
    

    # TODO: construct 5 random sentences
    # Your code here

    print(return_markov()) 
    print(return_markov())
    print(return_markov())
    print(return_markov())
    print(return_markov())
    

    

    
    





