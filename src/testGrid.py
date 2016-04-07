# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:57:32 2016

@author: planat
"""

# http://matplotlib.org/users/image_tutorial.html


import matplotlib.pyplot as plt
import numpy as np
import random

SPACE_Y = 100
SPACE_X = 100
FIRE_SIZE = 20
NB_FIRE = 2
FIRE_HOTTEST_TEMP = 0.8
FIRE_LOWEST_TEMP = 0.2

fire_x = [30,60]
fire_y = [30,60]

# initialize space with zero
game_field = np.zeros((taille_x,taille_y))

# loop accross al the fires
for id in range(0,NB_FIRE):   
    y_ref = fire_y[id]
    x_ref = fire_x[id]
    for index in range(1,FIRE_SIZE):
        x = x_ref + index
        terrain[x,]
    



A = np.random.rand(5, 5)
plt.figure(1)
plt.imshow(A)
#plt.grid(True)
