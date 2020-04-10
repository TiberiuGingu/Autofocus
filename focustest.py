#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    #citire si afisare imagine originala
    img = cv2.imread('ofamerica.png')
    plt.subplot(121)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.title('Unid Eium')

    #afisare imagine blurata
    plt.subplot(122)
    blur = cv2.GaussianBlur(img,(101,101),0)
    plt.imshow(blur)
    plt.xticks([]), plt.yticks([])
    plt.title('Unid Eium Blurat')

    plt.show()

    
    print ("Autofocus2")
    print ("test")
if __name__ == "__main__":
    main()