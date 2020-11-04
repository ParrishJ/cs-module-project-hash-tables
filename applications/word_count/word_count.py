""" UNDERSTAND

We need to split the string up, remove any special characters listed in the readme, then push those strings to a dictionary as a key where the value is the number of occurances of those strings

PLAN

First, we'll remove all special characters from the strings, leaving spaces. We'll do this by creating a new string and pushing characters from the old string that fit this criteria to the new string.
Then, we'll split the strings into a list.
Next, we'll loop through the list and push the strings to the dictionary as a key if they don't already exist or will increment the value for the correct key if the key already exists """

def word_count(s):
    # Your code here
    newStr = ""
    strDict = {}
    for char in s:

        if char.isalnum() == True or char.isspace() == True or char == "'": 
            newStr = newStr + char
    newStr = newStr.lower()
    strArr = newStr.split()

    if newStr == None:
        return strDict
    
    for word in strArr:
        if word in strDict:
            strDict[word] += 1
        else:
            strDict[word] = 1
    
    return strDict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))