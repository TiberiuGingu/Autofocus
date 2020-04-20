#!/usr/bin/env python3

import cv2
from PIL import Image
from PIL import ImageFilter
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from random import randint
from ml_functions import TORT, UTRIS, evalpoly
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
    x=[]
    y=[]

    #citire si afisare imagine originala
    OrgImage = Image.open("poza2.jpg")
    OrgImage.show()
    image = cv2.imread("poza2.jpg")
    img = rgb2gray(image)


    # #imagine blurata random
    # boxImage = OrgImage.filter(ImageFilter.BoxBlur(80))
    # boxImage.save(".\\auxiliar.jpg")
    # blur = cv2.imread("auxiliar.jpg")
    # bl = rgb2gray(blur)
    # print(get_contrast(bl))
    # boxImage.show()
    # boxImage = OrgImage.filter(ImageFilter.BoxBlur(90))
    # boxImage.save(".\\auxiliar.jpg")
    # blur = cv2.imread("auxiliar.jpg")
    # bl = rgb2gray(blur)
    # print(get_contrast(bl))
    # boxImage.show()


    #training vector
    for i in range (100):
        random = randint(1,80)
        #x.append(random)
        x.append(i)
        boxImage = OrgImage.filter(ImageFilter.BoxBlur(i))
        boxImage.save(".\\auxiliar.jpg")
        blur = cv2.imread("auxiliar.jpg")
        bl = rgb2gray(blur)
        y.append(get_contrast(bl))


    coef = polyfit(x, y)
    y_contrast = []
    x_contrast = []
    for i in range (100):
        x_contrast.append(i)
        y_contrast.append(evalpoly(coef, i))

    plt.plot(x_contrast, y_contrast)
    plt.show()


    #afisare contrast
    print(get_contrast(img))
    print(get_contrast(bl))

if __name__ == "__main__":
    main()