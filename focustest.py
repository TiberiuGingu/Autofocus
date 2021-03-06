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
import sys
import time
from progress_bar import printProgressBar

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

    #alegere poza
    
    if len (sys.argv) != 2 :
        print ("Wrong number of arguments taken from console! (expected 1 argument but recieved:" , len(sys.argv) - 1, ")")
        sys.exit (1)

    else:
        photo_name = sys.argv[1]

    #identificare extensie poza
    extension = photo_name.split('.')[-1]

    if extension != 'png' and extension != 'jpg':
        print("File must be .png or .jpg. Choose another file:")
        photo_name = input()
        extension = photo_name.split('.')[-1]   

    #citire si afisare imagine originala
    OrgImage = Image.open(photo_name)
    OrgImage.show()
    image = cv2.imread(photo_name)
    img = rgb2gray(image)

    print("Blur level ( in range (1, 100) ):")
    nivel_blur = float(input())

    while nivel_blur < 1:
        print("Blur must be over 1 :")
        nivel_blur = float(input())
        
    #training
    
    if nivel_blur < 5:
        printProgressBar(0, 20, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i in range (20):
            x.append(i)
            boxImage = OrgImage.filter(ImageFilter.BoxBlur(i))
            boxImage.save(".\\auxiliar." + extension)
            blur = cv2.imread("auxiliar."+ extension)
            bl = rgb2gray(blur)
            y.append(get_contrast(bl))
            printProgressBar(i + 1, 20, prefix = 'Progress:', suffix = 'Complete', length = 50)
    else:
        printProgressBar(0, math.ceil((nivel_blur+10)/2), prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i in range (math.ceil((nivel_blur+10)/2)):
            x.append(2*i)
            boxImage = OrgImage.filter(ImageFilter.BoxBlur(2*i))
            boxImage.save(".\\auxiliar." + extension)
            blur = cv2.imread("auxiliar." + extension)
            bl = rgb2gray(blur)
            y.append(get_contrast(bl))
            printProgressBar(i + 1, math.ceil((nivel_blur+10)/2), prefix = 'Progress:', suffix = 'Complete', length = 50)

    # determinarea polinomului care aproximeaza functia
    coef = polyfit(x, y)
    y_contrast = []
    x_contrast = []
    for i in range (math.ceil((nivel_blur+10)/2)):
        x_contrast.append(2*i)
        y_contrast.append(evalpoly(coef, 2*i))

    # aflare minim
    for i in range(len(coef)):
        coef[i] = (-1)*coef[i]

    x_min, y_min, val_min = gold( 0, 20, coef, 2 )
    
    if nivel_blur > 20:
        k = math.ceil((nivel_blur/20)-1)
        for i in range(1,k):
            x_aux, y_aux, val_aux = gold( 20*i, 20*(i+1), coef, 1 )
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
    boxImage.save(".\\auxiliar." + extension)
    blur = cv2.imread("auxiliar." + extension)
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
    plt.title('Imagine')
    plt.xticks([]), plt.yticks([])
    plt.savefig('results.png')
    print('Open result.png and press enter to continue')
    input()

    for i in val_min:
        plt.figure()
        plt.subplot(121)
        plt.plot(x_contrast, y_contrast)
        plt.plot(i,evalpoly(coef,i),'r*')
        plt.grid(True)
        plt.title('Grafic')
        boxImage = OrgImage.filter(ImageFilter.BoxBlur(i))
        boxImage.save(".\\auxiliar." + extension)
        blur = cv2.imread("auxiliar." + extension)
        plt.subplot(122)
        plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
        plt.title('Imagine')
        plt.xticks([]), plt.yticks([])
        plt.savefig('results.png')
        input()


if __name__ == "__main__":
    main()