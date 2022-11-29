#Task
"""
2. Now, create a 10 × 10 matrix A in which A[i][j] = i + j. You’ll be able to do this using
   the vector you just created, and adding it to a reshaped version of itself.
"""
#Program


import numpy as np

def matrix_creation():
    arr=np.arange(10)
    arr1=np.arange(1,100,10)
    A=[]
    for i in np.nditer(arr):
        for j in np.nditer(arr1):
            val=i+j
            A.append(val)
    A=np.array(A).reshape(10,10)
    print(A)

matrix_creation()

