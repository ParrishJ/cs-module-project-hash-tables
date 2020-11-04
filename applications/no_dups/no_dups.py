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
    print(len(str_keys))
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