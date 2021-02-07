'''
Author: Alex Pitts
Date: 2/7/21
Class: CS 362

Description: This program simply calculates the 
volume of a cube with the function "volume_of_cube()"
'''

def volume_of_cube(edge):

    #convert inputs to ints
    edge = int(edge)
    
    
    #if a negative num is detected, calculate error value and return it
    if(edge<1):
        return -1
    
    #calculate errors if no negative values were entered
    volume = edge**3
    return volume
