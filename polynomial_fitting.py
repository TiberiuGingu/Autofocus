#!/usr/bin/env python3

import numpy as np
from ml_functions import TORT, UTRIS

def CMMP(A, b):
    [A, U, beta] = TORT(A)
    m = len(A[:, 1])
    n = len(A[1, :])

    for k in range (0, n):
        sum = 0
    
        for i in range (k, m+1):
            sum = sum + U[i][k] * b[i]
    
        sigma = sum/beta[k]
    
        for i in range (k, m+1):
            b[i] = b[i] - sigma * U[i][k]

    x = UTRIS(A, b)
    return x


def polyfit(x,y):
    A = []
    sol = []
    for i in x:
        v = [i**4, i**3, i*i, i, 1]
        A.append(v)
    sol = CMMP(A, y)
    return sol
    

def main():
    x = [1, 2, 3]
    y = [1, 2, 3]
    M = polyfit(x,y)
    print(M)

if __name__=='__main__':
    main()