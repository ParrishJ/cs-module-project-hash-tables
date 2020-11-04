""" UNDERSTAND

We want to take a given string, and return the string with all duplicate words removed - without a trailing space

PLAN 

We'll create a dictionary to hold all instances of unique words in our given string. 
We'll then split the given string so that each word occupies an index in a list.
We'll also initialize an empty string to hold our final answer. We'll then loop through our words array and push any words that haven't already appeared to our dictionary.
We'll then use the keys from the dictionary to serve as a list of words that will appear in our final answer.
We'll use the length of the dictionary keys to serve as a benchmark for when to add a space between words in our final string.
We'll then loop through our dictionary keys, and append each word to our final string, incrementing a counter for each key.
If the counter is equal to our lengths of keys, we won't append an extra space with the word. If the counter is less than the length of keys, we will append an extra space with the word. 
""" 
def no_dups(s):
    # Your code here
    str_dictionary = {}
    s = s.split()
    ans_str = ""

    for word in s: 
        if word in str_dictionary:
            pass
        else:
            str_dictionary[word] = 1
    str_keys = str_dictionary.keys()
    
    key_len = len(str_keys)
    count = 1 
    for key in str_keys:
        
        print(key)
        if count != key_len:
            ans_str += (key + " ")
            count += 1
        else:
            ans_str += key
    return ans_str


if __name__ == "__main__":
    print(no_dups(""))
    print(len(no_dups("hello")))
    print(no_dups("hello hello"))
    print(len(no_dups("cats dogs fish cats dogs")))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))