#!/usr/bin/env python3

import cv2
from PIL import Image, ImageFilter
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from random import randint
from ml_functions import TORT, UTRIS, evalpoly, gold
from polynomial_fitting import CMMP, polyfit
import math

# functie pentru calcularea contrastului
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

    print("Nivel de blur ( cuprins intre 0 si 100 ):")
    nivel_blur = int(input())

    #training
    for i in range (nivel_blur+10):
        x.append(i)
        boxImage = OrgImage.filter(ImageFilter.BoxBlur(i))
        boxImage.save(".\\auxiliar.jpg")
        blur = cv2.imread("auxiliar.jpg")
        bl = rgb2gray(blur)
        y.append(get_contrast(bl))

    # determinarea polinomului care aproximeaza functia
    coef = polyfit(x, y)
    y_contrast = []
    x_contrast = []
    for i in range (nivel_blur+10):
        x_contrast.append(i)
        y_contrast.append(evalpoly(coef, i))

    # aflare minim
    for i in range(len(coef)):
        coef[i] = (-1)*coef[i]

    x_min, y_min, val_min = gold( 0, 20, coef, 2 )
    
    if nivel_blur > 20:
        k = math.ceil((nivel_blur/20)-1)
        for i in range(1,k):
            x_aux, y_aux, val_aux = gold( 20*i, 20*(i+1), coef, 2 )
            if x_min < x_aux:
                val_min = [val_aux[0]] + val_min
            else:
                val_min = [val_min[0]] + val_aux  
            if y_min > y_aux :
                x_min = x_aux
                y_min = y_aux
                val_min = val_aux

    y_min = (-1)*y_min
    for i in range(len(coef)):
        coef[i] = (-1)*coef[i]

    # afisarea rezultatelor
    plt.figure()
    plt.subplot(121)
    plt.plot(x_contrast, y_contrast)
    plt.plot(nivel_blur,evalpoly(coef,nivel_blur),'r*')
    plt.grid(True)
    plt.title('Grafic')
    boxImage = OrgImage.filter(ImageFilter.BoxBlur(nivel_blur))
    boxImage.save(".\\auxiliar.jpg")
    blur = cv2.imread("auxiliar.jpg")
    plt.subplot(122),plt.imshow(blur),plt.title('Imagine')
    plt.xticks([]), plt.yticks([])
    plt.show()
    input()

    for i in val_min:
        plt.figure()
        plt.subplot(121)
        plt.plot(x_contrast, y_contrast)
        plt.plot(i,evalpoly(coef,i),'r*')
        plt.grid(True)
        plt.title('Grafic')
        boxImage = OrgImage.filter(ImageFilter.BoxBlur(i))
        boxImage.save(".\\auxiliar.jpg")
        blur = cv2.imread("auxiliar.jpg")
        plt.subplot(122),plt.imshow(blur),plt.title('Imagine')
        plt.xticks([]), plt.yticks([])
        plt.show()
        input()


if __name__ == "__main__":
    main()