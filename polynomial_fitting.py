#!/usr/bin/env python3

import numpy as np
from ml_functions import TORT, UTRIS

def CMMP(A, b):
    [A, U, beta] = TORT(A)
    m = len(A)
    n = len(A[1])
    for k in range (0, n):
        sum = 0
    
        for i in range (k, m):
            sum = sum + U[i][k] * b[i]
    
        sigma = sum/beta[k]
    
        for i in range (k, m):
            b[i] = b[i] - sigma * U[i][k]

    for r in range (m-n):
        del A[-1]
        del b[-1]
    x = UTRIS(A, b)
    return x


def polyfit(x,y):
    A = []
    sol = []
    for i in x:
        v = [1, i, i*i, i**3, i**4]
        A.append(v)
    sol = CMMP(A, y)
    return sol
    

def main():
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 0.5, 0.33, 0.25, 0.2, 0.16]
    
    z = polyfit(x,y)
    print(z)

if __name__=='__main__':
    main()