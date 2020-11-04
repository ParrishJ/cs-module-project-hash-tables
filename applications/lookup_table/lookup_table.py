import random
import math
# Your code here

""" UNDERSTAND

We need to cache combinations of x,y that have already been run so that this function runs faster

PLAN

Initialize a cache with an empty dictionary 
If x,y combination already in cache, just do a lookup
Else, store x,y values in cashe as tuple, run function and return value 

"""

""" def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v """

""" def cache_builder():
    cache = {}
    def computation(x, y):
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653

        return v

    for x in range(2, 14):
        for y in range(3, 6):
            cache[(x, y)] = computation(x, y)
    
    return cache

cache = cache_builder() """

cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    def computation(x, y):
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653

        return v

    if (x, y) in cache:
        return cache[(x, y)]
    else:
        cache[(x, y)] = computation(x, y)
        return cache[(x, y)]
    
    
    

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')



