'''
Author: Alex Pitts
Date: 2/7/21
Class: CS 362

Description: This program simply calculates the 
volume of a cube with the function "volume_of_cube()"
'''

def volume_of_cube(length, width, hight):

    #convert inputs to ints
    length = int(length)
    width = int(width)
    hight = int(hight)
    
    #if a negative num is detected, calculate error value and return it
    if(length<1 or width<1 or hight<1):
        error = 0
        if(length<1):
            error += -1
        if(width<1):
            error += -2
        if(hight<1):
            error += -4
        return error
    
    #calculate errors if no negative values were entered
    volume = length*width*hight
    return volume
