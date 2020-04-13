#!/usr/bin/env python3
import math
import numpy as np

def UTRIS(U,b):
    n = len(b)
    x = b
    for i in range ((n-1), (-1), (-1)):
        print(i)
        for j in range ((i+1),(n)):
            x[i] = x[i] - U[i][j]*x[j]
        x[i] = x[i]/U[i][i]
    return x

def TORT(A):
    m=len(A)
    n=len(A[1])
    p=min(m-1,n)
    beta = []
    for i in range(p):
        beta.append(0)
    U = []
    for i in range(m):
        zero=[]
        for j in range(n):
            zero.append(0)
        U.append(zero)
    for k in range(0,p):
        sum = 0
        tau = 0
        for i in range(k,m):
            sum = sum + A[i][k]*A[i][k]
        sum = math.sqrt(sum)

        tau = np.sign(A[k][k])*sum
        if tau == 0:
            beta[k] = 0
        else:
            U[k][k] = A[k][k] + tau

            for i in range(k+1, m):
                U[i][k] = A[i][k]    
            beta[k] = tau*U[k][k]
            A[k][k] = -tau
            for i in range(k+1,m):
                A[i][k] = 0
            for j in range(k+1,n):
                sum = 0
                for i in range(k,m):
                    sum = sum + U[i][k]*A[i][j]
                sigma = sum/beta[k]
                for i in range(k,m):
                    A[i][j] = A[i][j]-sigma*U[i][k]
    return [A, U, beta]

def main():
    M = [[7, 3],[4, 2],[1, 2]]
    b = [2, 2, 6]
    U=[[1,4,6],[0,2,5],[0, 0, 3]]
    [A,U,beta] = TORT(M)
    print(A)
    print(UTRIS(U,b))
if __name__=='__main__':
    main()
