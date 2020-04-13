#!/usr/bin/env python3

import numpy as np

def polyfit(x,y):
    A = []
    for i in x:
        v = [i**4, i**3, i*i, i, 1]
        A.append(v)
    return A
    

def main():
    x = [1, 2, 3]
    y = [1, 2, 3]
    M = polyfit(x,y)
    print(M)

if __name__=='__main__':
    main()