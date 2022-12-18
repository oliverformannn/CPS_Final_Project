#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:28:43 2022

@author: oliverforman
"""
import numpy as np
import matplotlib.pyplot as plt
import random

# Assumptions that are being made: takeoff and descent angle will be 45 degrees; 
# the place will turn at 90 degrees when in air; the flight will cruise at an 
# altitude of 11km in the air; the plane will travel at 1km/min when at cruising
# altitude forward; there will also be a 2km warning zone and a 1km danger zone 
# that will surrounding the plane alerting the pilot if any aircraft is at risk of 
# collision and will then alter the plane's course

#theta = 45 #degrees
#takeoff = 1 # km/min
#descent = 1 #km/min


# starting point for the plane will be considered (0,0,0)
# +y will be considered forward, the -x being left, and the +x being right
# will be adjusted during sim to make sure these values eventually reach the desired
# final destination
x = 0
y = 0
z = 0
time = 0

# variable h is to track whether the aircraft took a right or a left, and v will show if it moved up or down to make
# sure that the plane reaches its correct destination 
# -1 will represent left or down and 1 will be right or up
h = 0
v = 0


# this is for the other aircraft in the air that will remain stationary for simulation purposes
a = -2
b = 100
c = 9

# Used to generate a random point for the foreign aircraft to be for verification
#a = random.randint(-10,10)
#b = random.randint(11,250)
#c = random.randint(9,13)

#print(a)
#print(b)
#print(c)

# This is to initalize the foreign aircraft to be able to be plotted with the movement of the aircraft
# to visually see that the aircraft in question is avoiding this one
X = [a]
Y = [b]
Z = [c]

# User will now input the plane's final destination
# z_final can be conisdered 0 since the plane will be landing
#x_final = int(input("Enter the x coordinate location for the destination: "))
x_final = 0
y_final = int(input("Enter the distance to your destination: "))


# the total distance that the plane will have to move
total_path = np.sqrt((x_final**2 + y_final**2))

# initializing arrays that will be used to graph the movement of the plane
arrayx = np.zeros(y_final + 50)
arrayy = np.zeros(y_final + 50)
arrayz = np.zeros(y_final + 50)
#print(arrayy)

# 14 is the average speed in the air at cruise is 14km/min
# the -20 comes from accounting for time needed for takeoff and descent
#air_time = (total_path/14) - 20 

# Filling in the 0th array element for all the arrays
arrayx[0] = 0
arrayy[0] = 0
arrayz[0] = 0


i = 1 # initializes i at 1 because the 0th array element is already filled in above
# the while statement to ensure that the plane is not moving or making adjustments to its course
# after it already traveled the distance it was meant to 
while i < y_final:
    # this is for takeoff
    while z < 11:
        y = y + 1 # 1 is the horizontal distance traveled every minute
        arrayy[i] = y # storing value of y in array for the ith element
        
        z = z + 1 # updating the vertical coordinate so that it reaches 11 km 
        arrayz[i] = z # storing value of z in array for the ith element
        
        time = time + 1 # incrementing time each time to track how long the flight it
        i = i + 1
        

    while y < (total_path - 11):
        
        # the following movement of the plane only occurs when another aircraft is in the warning zone
        # of 2km from the aircraft. This will cause more drastic movements of 1km/min to occur in either
        # the horizontal direction, vertical, or both
        if (abs(a - x) <= 2) & (abs(b - y) <= 2) & (abs(c-z) <= 2):
            # displays to the user that there is another aircraft in its warning zone
            s1 = '\nWarning!'
            print(s1)
         
            # the foreign aircraft is within the 2km warning zone to the aircrafts left
            if (a - x) <= 0: 
                x = x + 1 # updating x to move to the right
                h = h + 1 # tracking that x moved to the right
                
                y = y # y doesn't change as it cannot move forward
                z = z
                
                arrayx[i] = x # storing value of x in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                arrayz[i] = z # storing value of z in array for the ith element
               
            # the foreign aircraft is within the 2km warning zone to the aircrafts right    
            if (a - x) > 0:
                x = x - 1  # updating x to move to the left
                h = h - 1  # updating x to move to the left
                
                y = y  # y doesn't change as it cannot move forward
                z = z
                
                arrayx[i] = x # storing value of x in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                arrayz[i] = z # storing value of z in array for the ith element
                
            # the foreign aircraft is within the 2km warning zone underneath aircraft    
            if (c - z) <= 0:
                z = z + 1 # updating z to move to the up
                v = v + 1 # tracking that z moved up
                y = y # y doesn't change as it cannot move forward
                
                arrayz[i] = z # storing value of z in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                
            # the foreign aircraft is within the 2km warning zone above aircraft        
            if (c - z) > 0:
                z = z - 1 # updating z to move to the down
                v = v - 1  # tracking that z moved down
                y = y # y doesn't change as it cannot move forward
                
                arrayz[i] = z # storing value of z in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                
            i = i + 1
            time = time + 1 # incrementing time each time to track how long the flight it
       
        
        # the following movement of the plane only occurs when another aircraft is in the danger zone
        # of 1km from the aircraft. This will cause more drastic movements of 3km/min to occur in either
        # the horizontal direction, vertical, or both
        if (abs(a - x) <= 1) & (abs(b - y) <= 1) & (abs(c-z) <= 1):
            # displays to the user that there is another aircraft  within the danger zone
            s2 = '\nDanger!'
            print(s2)
            
            # the foreign aircraft is within the 1km danger zone to the aircrafts left
            if (a - x) <= 0:
                x = x + 2 # updating x to move to the right
                h = h + 1 # tracking that x moved right
                y = y
                
                arrayx[i] = x # storing value of x in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                arrayz[i] = z # storing value of z in array for the ith element
            
            # the foreign aircraft is within the 1km danger zone to the aircrafts right
            if (a - x) > 0:
                x = x - 2 # updating x to move to the left
                h = h - 1 # tracking that x moved left
                y = y
                
                arrayx[i] = x # storing value of x in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                arrayz[i] = z # storing value of z in array for the ith element
             
            # the foreign aircraft is within the 1km danger zone underneath the aircraft 
            if (c - z) <= 0:
                z = z + 1 # updating z to move to the up
                v = v + 1 # tracking that z moved up
                y = y
                
                arrayz[i] = z # storing value of z in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                
             # the foreign aircraft is within the 1km danger zone above the aircraft     
            if (c - z) > 0:
                z = z - 1 # updating z to move to the down
                v = v - 1 # tracking that z moved down
                y = y
                
                arrayz[i] = z # storing value of z in array for the ith element
                arrayy[i] = y # storing value of y in array for the ith element
                
            i = i + 1
            time = time + 1 # incrementing time each time to track how long the flight it
            #print(arrayx)
 
        
        else:
                
                # if after the accumulation of all the right or left turns is positive and when the aircraft
                # is not in the warning or danger zone
                if h >= 1:
                    x = x - 1 # the aircraft turns left in order to get back to original path
                    h = h - 1 # will update h until h = 0 so that system knows aircraft is back on original path
                    y = y # y should not change at this time
                    
                    arrayx[i] = x # storing value of x in array for the ith element
                    arrayy[i] = y # storing value of y in array for the ith element
                    arrayz[i] = z # storing value of z in array for the ith element
                    
                    time = time + 1 # incrementing time each time to track how long the flight it
                    i = i + 1
                    #print(arrayy)      
                
                # if after the accumulation of all the right or left turns is negative and when the aircraft
                # is not in the warning or danger zone
                if h <= -1:
                    x = x + 1 # the aircraft turns right in order to get back to original path
                    h = h + 1 # will update h until h = 0 so that system knows aircraft is back on original path
                    y = y # y should not change at this time
                    
                    arrayx[i] = x # storing value of x in array for the ith element
                    arrayy[i] = y # storing value of y in array for the ith element
                    
                    time = time + 1 # incrementing time each time to track how long the flight it
                    i = i + 1
                #print(arrayx)    
                    
                # if after the accumulation of all the up or down movements is negative and when the aircraft
                # is not in the warning or danger zone
                if v >= 1:
                    z = z - 1 # the aircraft moves down in order to get back to original path
                    v = v - 1 # will update v until v = 0 so that system knows aircraft is back on original path
                    y = y
                    
                    arrayz[i] = z # storing value of z in array for the ith element
                    arrayy[i] = y # storing value of y in array for the ith element
                    
                    time = time + 1 # incrementing time each time to track how long the flight it
                    i = i + 1
                    
            
                if v <= -1:
                    z = z + 1 # the aircraft moves up in order to get back to original path
                    v = v - 1 # will update v until v = 0 so that system knows aircraft is back on original path
                    y = y
                    
                    arrayz[i] = z # storing value of z in array for the ith element
                    arrayy[i] = y # storing value of y in array for the ith element
                    
                    time = time + 1 # incrementing time each time to track how long the flight it
                    i = i + 1
                    
                else:
                   y = y + 1
                   z = z
                   arrayy[i] = y # storing value of y in array for the ith element
                   arrayz[i] = z # storing value of z in array for the ith element
                   
                   time = time + 1 # incrementing time each time to track how long the flight it
                   i = i + 1
                    
    #print(arrayz)
    # this is the descent of the plane      
    while z >= 1:
        y = y + 1 #1.1 is the horizontal distance traveled every minute
        arrayy[i] = y # storing value of y in array for the ith element
        
        z = z - 1 # updating the vertical coordinate so that it reaches 11 km in 10 min
        arrayz[i] = z # storing value of z in array for the ith element
        
        time = time + 1
        i = i + 1

# This if statement is used to check that the plane actually made it to its destination 
# as well as its destination being the correct location.       
if (x - x_final == 0) & (y - y_final == 0) & (z == 0):
        # displays that the aircraft arrived to its destination safely
        s3 = '\nArrived at your destination!'
        print(s3)
        
        # displays to the user how long the flight took with the flight path changes if taken
        string = '\nThe time in minutes needed to complete your trip was: '
        print(string)
        print(time)
        
# the following below is to plot the movemenet of the aircraft that is using this system
# It shows that for an aircraft that is within its vicinitiy during flight will cause
# the plane to alter its course in order to avoid being in the wanring zone of the system.
# This occurs for both the horizontal and vertical directions
plt.figure()
plt.plot(arrayx,arrayy)
plt.grid()
plt.plot(X, Y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
plt.legend
plt.xlabel('Horizontal Movement (km)')
plt.ylabel('Distance Traveled Toward Destination (km)')
plt.title("Plot of Aircraft's Horizontal Avoidance")
plt.show()


plt.figure()
plt.plot(arrayy,arrayz)
plt.grid()
plt.plot(Y, Z, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
plt.ylabel('Vertical Movement (km)')
plt.xlabel('Distance Traveled Toward Destination (km)')
plt.title("Plot of Aircraft's Vertical Avoidance")
plt.show()



       
    