# Autofocus

Autofocus simulates the process through which a camera focuses an image by gradually changing the focal distance to an optimal value. In our case the focal distance is represented by the blur level, because we do not dispose of three dimensional images.

## How does it work?

The picture is blurred with a certain level introduced from the keyboard.

Then a training process is needed to determine the function between the contrast and blur level .The image is blurred with different levels and the contrasts are calculated, to obtain a data set. The minimum of this function is used to find the optimal blur level for which the image is in focus. 


## How to run the program

In order to run the program on a certain photo you have to type the path to ```focustest.py``` and the name of the photo with space in between them like in this example: ```./Autofocus/focustest.py <photo_name>```.

After running the previous commands close the original picture which will show up on your screen, then follow the instructions that appear in the terminal.

The Autofocus repository contains a bunch of sample pictures to showcase the functionality. However, if you want to test it on another picture, you will have to save it in the same folder as the ```focustest.py``` executable.

### WARNING
The pictures must have a reasonable contrast which means they shouldn't be completely white or black.

## Requirements

Assuming that you have already installed python3, you will also need to install some libraries by typing the following command: ```pip install <library name>```, in the console.

The name of the libraries are: 
- PILLOW 
- matplotlib
- numpy
- opencv

