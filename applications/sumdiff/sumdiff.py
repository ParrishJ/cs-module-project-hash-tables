"""
UNDESTAND
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)

We need to find all of the possible combinations that satisfy the condition above and print the functions and values of those combinations. 

PLAN

First, we'll construct a hash table with the keys being each value in q, and the values being the output of f(x) for each value of q.

Next we'll use recursion along with a helper function to generate two additional dictionaries: one for all possibilities on the left 
hand side of the equality, one for all possibilities for all possible values on the right hand side of the equality.

By using a dictionary, we can ensure that each possibility is found in each dictionary only once by performing a check on the entry 
before it is entered into the dictionary.

The recursive function will loop over our helper function a number of time equal to the length of a list generated from the dictionary of 
computed values.

Once the recursive function has generated our two new dictionaries, I will create an additional function to create lists from these values.
These lists contain both the original number (before they were calculated using f(x)) as well as their computed value.

Using these lists, I can make the comparison specified in the readme (f(a) + f(b) = f(c) - f(d)) and can push any pair of "left" / "right" 
combinations that fit this description to a new list.

I will then use this new list to generate the strings specified in the readme as the list has all the information I will need. 


"""

#q = set(range(1, 10))
#q = set(range(1, 200))

q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

# Your code here

def find_combinations():
    possibilities = []
    computed_dict = {}
    total_possibilities_left = {}
    total_possibilities_right = {}

    for value in q:
        computed_dict[value] = f(value)
    possibility_list = list(computed_dict.items())
    
    def helper(n, curr_possibilities):
        
        if n == 0:
            possibilities.append(curr_possibilities)

            left_keys = (curr_possibilities[0][0], curr_possibilities[1][0])
            left_vals = (curr_possibilities[0][1], curr_possibilities[1][1])
            right_keys = (curr_possibilities[2][0], curr_possibilities[3][0])
            right_vals = (curr_possibilities[2][1], curr_possibilities[3][1])
            
            if left_keys not in total_possibilities_left:
                total_possibilities_left[left_keys] = left_vals
            if right_keys not in total_possibilities_right:
                total_possibilities_right[right_keys] = right_vals

            return
        
        for i in range(len(possibility_list)):
            new_possibility = [possibility_list[i]]
            helper(n - 1, curr_possibilities + new_possibility)
    helper(4, [])
    
    return total_possibilities_left, total_possibilities_right

    
final_posibilities_left = list(find_combinations()[0].items())
final_posibilities_right = list(find_combinations()[1].items())

def find_final(total_left, total_right):
    final_combination = []
    
    for i in range(len(total_left)):
        for j in range(len(total_right)):
            if (total_left[i][1][0] + total_left[i][1][1]) == (total_right[j][1][0] - total_right[j][1][1]):
                final_combination.append([total_left[i], total_right[j]])
    
    
    for possibility in final_combination:
        print(f'f({possibility[0][0][0]}) + f({possibility[0][0][1]}) = f({possibility[1][0][0]}) - f({possibility[1][0][1]})' + '    ' + f'{possibility[0][1][0]}' + ' + ' + f'{possibility[0][1][1]}' + ' = ' + f'{possibility[1][1][0]}' + ' - ' f'{possibility[1][1][1]}')

find_final(final_posibilities_left, final_posibilities_right)