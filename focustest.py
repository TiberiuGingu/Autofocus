#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from random import randint
from ml_functions import TORT, UTRIS
from polynomial_fitting import CMMP, polyfit

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
    plt.imshow(img, cmap=cm.gray, vmin=0, vmax=255)
    plt.xticks([]), plt.yticks([])
    plt.title('Original')

    #training
    for i in range (6):
        random = randint(1, 100)
    if random % 2 == 0:
        random += 1

    #afisare imagine blurata
    random = randint(1, 100)
    print(random)
    if random % 2 == 0:
        random += 1
    plt.subplot(122)
    blur = cv2.GaussianBlur(img,(random,random),0)
    plt.imshow(blur, cmap=cm.gray, vmin=0, vmax=255)
    plt.xticks([]), plt.yticks([])
    plt.title('Blurat')

    plt.show()

    #afisare contrast
    print(get_contrast(img))
    print(get_contrast(blur))
if __name__ == "__main__":
    main()