#!/usr/bin/env python3

import cv2
from PIL import Image
from PIL import ImageFilter
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
    x=[]
    y=[]

    #citire si afisare imagine originala
    OrgImage = Image.open("poza.png")
    OrgImage.show()
    image = cv2.imread("poza.png")
    img = rgb2gray(image)
    
    # plt.subplot(121)
    # plt.imshow(img, cmap=cm.gray, vmin=0, vmax=255)
    # plt.xticks([]), plt.yticks([])
    # plt.title('Original')

    #imagine blurata random
    boxImage = OrgImage.filter(ImageFilter.BoxBlur(40))
    boxImage.show()

    #training vector
    for i in range (10):
        random = randint(1,80)
        x.append(random)
        boxImage = OrgImage.filter(ImageFilter.BoxBlur(20.34))
        boxImage.show()
        boxImage.save(".\\auxiliar.png")
        blur = cv2.imread("auxiliar.png")
        bl = rgb2gray(blur)

    # plt.subplot(122)
    # blur = cv2.GaussianBlur(img,(random,random),0)
    # plt.imshow(blur, cmap=cm.gray, vmin=0, vmax=255)
    # plt.xticks([]), plt.yticks([])
    # plt.title('Blurat')
    # plt.show()

    #afisare contrast
    print(get_contrast(img))
    print(get_contrast(bl))

if __name__ == "__main__":
    main()