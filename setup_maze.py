# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:11:27 2018
@author: yhao
"""
#Adampted from; https://www.youtube.com/watch?v=-0q_miviUDs&list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP&index=2

##SETTING UP THE MAZE

#a window of 700x700
#Top Left Block: -288, 288
#Top Right Block: 288, 288
#Bottom Left Block: -288, -288
#Bottom Left Block: 288, -288

import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0) #Animation speed
        
#Create levels list
#levels = [""]

#Define first maze grid from our input
level_1= [
"XXXXXXXXXXXXXXXXXXXXX",
"X X         X   X   X",
"X X XXX XXXXX X X X X",
"X   X X       X X X X",
"X XXX XXXXXXXXX XXX X",
"X X   X       X   X X",
"X XXX X XXXXX XXX X X",
"X X   X     X   X X X",
"X X XXXXX XXX X X X X",
"X X   X   X   X X X X",
"X XXX X XXX XXXXXXX X",
"X   X     X       X X",
"XXX X XXXXXXXXX X X X",
"X X X X       X X   X",
"X X XXX XXXXX X XXXXX",
"X X   X X     X     X",
"X XXX X X XXXXXXXXX X",
"X   X X X   X       X",
"X XXX X XXX XXX XXX X",
"X       X       X   X",
"XXXXXXXXXXXXXXXXXXXXX"     
]       
 
#Add maze to mazes list:
#levels.append(level_1)

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x, y coordinate
            #Note the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
            
            #Check if it is an P (representing the player)
            if character == "P":
                pen.goto(screen_x, screen_y)
                               
#Create class instances
pen = Pen()

#Set up the maze
setup_maze(level_1)      


         
        
        
        
        
        
        
        
        
        
        
        
        
        