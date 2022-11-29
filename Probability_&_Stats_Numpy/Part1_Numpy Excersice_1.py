#Task
"""
1. The most basic kind of broadcast is with a scalar, in which you can perform a binary
   operation (e.g., add, multiply, ...) on an array and a scalar, the effect is to perform that
   operation with the scalar for every element of the array. To try this out, create a vector
   1, 2, . . . , 10 by adding 1 to the result of the arange function.


"""
#Program

import numpy as np

def array_creation():
    arr=np.arange(10)
    broadcast=np.array(arr)+1
    print(broadcast)
        
array_creation()
























 