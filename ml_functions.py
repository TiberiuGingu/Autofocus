#!/usr/bin/env python3
import math
import numpy as np

def UTRIS(U,b):
    n = len(b)
    x = b
    for i in range ((n-1), (-1), (-1)):
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

def evalpoly(v,x):
    y = 0
    y = y+v[0]
    for r in range(1,len(v)):
        y = y + v[r]*(x**r)
    return y

def gold( a, b, v, eps ):
    val = []
    alfa = (math.sqrt(5)-1)/2
    n = 1
    lam = a + (1-alfa)*(b-a)
    miu = a + alfa*(b-a)
    while abs(b-a) > eps:
        if evalpoly(v,lam) < evalpoly(v,miu):
            b = miu
            miu = lam
            lam = a + (1- alfa)*(b-a)
            val.append(miu)
        else:
            a = lam
            lam = miu
            miu = a + alfa*(b-a)
            val.append(lam)
        n = n+1
    ext = (a+b)/2
    return ext, evalpoly(v, ext), val
