#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as plt
import cv2

def get_contrast(img):
    contrast = 0
    for i in range(1, img.shape[0] - 1):
        line_inf = img[i-1, :]
        line = img[i, :]
        line_sup = img[i+1, :]
        for j in range(1, img.shape[1] - 1):
            contrast = contrast + abs(int(line[j+1]) - int(line[j]))
            contrast = contrast + abs(int(line[j]) - int(line[j-1]))
            contrast = contrast + abs(int(line[j]) - int(line_inf[j]))
            contrast = contrast + abs(int(line[j]) - int(line_sup[j]))
    return contrast

def main():
    nu = cv2.imread("cat.jpg")
    img = cv2.cvtColor(nu, cv2.COLOR_BGR2GRAY)
    random = randint(0, 501)
    if random % 2 == 0:
        random += 1
    blur = cv2.blur(img(random,random))
    cv2.imshow(blur)

    print(get_contrast(img))
    print(get_contrast(blur))
        
        

if __name__ == "__main__":
    main()