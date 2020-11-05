"""

UNDERSTAND

We need to decrypt the text by analyzing the freqency of the appearance of all characters in the text
We can then work backwards to use these frequencies to decrypt the characters in the text. 


PLAN 

We'll read the text in, itterate over the text, and find the frequency of each character by storing unique characters in a hash table and incrementing the values in the hash table.

We'll then order the dictionary in descending order based on the keys.

We'll also use the provided information in the readme to make a tuple of the 
list of characters with the most frequently occuring characters listed first. 

We'll also construct another dictionary that will hold the encrypted char as the key and the decrpyted char as the value.

We'll then loop through the sorted dictionary and compare it to the provided information to populate our answer_dict.

Lastly, we'll loop through the original string, and for each character, we will look up the the character in the 
answer dictionary to find the correct character and then push that character to a new string. 

"""

# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

def crack_caesar(): 
    with open("applications\crack_caesar\ciphertext.txt") as f:
        char_dict = {}
        answer_dict = {}
        ans_string = ""

        char_frequencies = ('E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z')


        text = f.read()

        for char in text:
            if char.isspace() == False and char.isalpha() == True and char != "â":
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1

        sorted_dict = sorted(char_dict.items(), key=lambda x: (-x[1],) + x[:1])
       
        print(len(sorted_dict))
        
        for i in range(len(sorted_dict)):
            answer_dict[sorted_dict[i][0]] = char_frequencies[i]


        for char in text:
            if char.isspace() == True:
                ans_string += " "
            if char.isalpha() == False or char == "â":
                ans_string += char 
            else:
                ans_string += answer_dict[char]


        print(ans_string)

crack_caesar()