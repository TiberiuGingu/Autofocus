#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
from random import randint

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

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def main():
    #citire si afisare imagine originala
    image = cv2.imread('poza.png')
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = rgb2gray(image)
    plt.subplot(121)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.title('Original')

    #afisare imagine blurata
    random = randint(1, 100)
    if random % 2 == 0:
        random += 1
    plt.subplot(122)
    blur = cv2.GaussianBlur(img,(random,random),0)
    plt.imshow(blur)
    plt.xticks([]), plt.yticks([])
    plt.title('Blurat')

    plt.show()

    #afisare contrast
    print(get_contrast(img))
    print(get_contrast(blur))
if __name__ == "__main__":
    main()