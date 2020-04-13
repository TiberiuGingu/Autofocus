#!/usr/bin/env python3

def UTRIS(U,b):
    n = len(b)
    x = b
    for i in range ((n-1), (-1), (-1)):
        for j in range ((i+1),(n)):
            x[i] = x[i] - U[i][j]*x[j]
        x[i] = x[i]/U[i][i]
    return x

def TORT(A):

    return A, U, beta

def main():
    U = [[7, 3, 2],[0, 2, 1],[0, 0, 4]]
    b = [2, 2, 6]
    x=UTRIS(U,b)
    print(x)
if __name__=='__main__':
    main()
