# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:44:09 2018

@author: Duncan
"""

import maze
import gradienthelper
import turtle
import random
from time import sleep

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("A Maze Game")
wn.setup(700,700)
#wn.exitonclick()

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("black")
        self.speed(0) #Animation speed

def value_iteration(grid, gamma):
    
    setup_maze(grid)

    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]
    actions = ['up', 'down', 'left', 'right']
    
    sleep(2)

    is_value_changed = True
    while is_value_changed:
        is_value_changed = False
        for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] != '#':
                        q = []
                        for a in actions:
                            neighbor = getattr(grid[i][j], a)
                            q.append(grid[i][j].reward + gamma * grid[neighbor[0]][neighbor[1]].value)
                        v = max(q)
                        
                        if v != grid[i][j].value:
                            is_value_changed = True
                            grid[i][j].value = v
                            
        animate_values(grid)
    turtle.done()
                            
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '#':
                # Dictionary comprehension to get value associated with each action
                action_values = {a: grid[getattr(grid[i][j], a)[0]][getattr(grid[i][j], a)[1]].value for a in actions}
                policy[i][j] = max(action_values, key=action_values.get)
                # Compare to previous policy
            else:
                policy[i][j] = '#'
                
    return(policy)
    
def setup_maze(level):
    wn.tracer(0,0)
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x, y coordinate
            #Note the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #Check if it is an X (representing a wall)
            if character == "#":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                
    wn.update()
                
    #pen.color('red')
    #pen.goto(-264, 264)
    #pen.stamp()
    
def animate_values(grid):
    
    wn.tracer(0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            
            character = grid[y][x]
            
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            pen.goto(screen_x, screen_y)
            
            if character == '#':
                pen.color('black')
                pen.stamp()
            
            else:
                pen.color(gradient_dict.get(int(round(character.value/5.)*5), '#008080'))
                pen.stamp()
                
    wn.update()
            
pen = Pen()

gradient = gradienthelper.linear_gradient('#FFFFFF', '#008080', 22)
col_list = range(-10, 102, 5)
gradient_dict = {col_list[i]: gradient.get('hex')[i] for i in range(len(gradient.get('hex')))}

if __name__ == '__main__':
    random.seed(1)
    test_maze = maze.Maze(w=10, h=10)
    test_policy = value_iteration(test_maze.grid, .9)
    
    
    
    values = [[state.value for state in row if state != '#'] for row in test_maze.grid]
    values = sum(values, [])
    

    print(min(values))
    print(max(values))
    #print(gradient_dict)

    #print(test_maze)
    #print(test_policy_str)