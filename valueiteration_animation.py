import gradienthelper
import turtle
import random
from time import sleep
import AldousBroder

"""
Duncan Rule, Sally Gao, Yi Hao
"""

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
        self.speed(0)
        self.ht()
        #Animation speed

def value_iteration(grid, gamma):
    
    setup_maze(grid)
    
    iterations = 0

    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]
    actions = ['up', 'down', 'left', 'right']
    
    pen.color('black')
    pen.goto(-297, -50)
    pen.write('Iterations: {}'.format(iterations), font=('Arial', 20, 'normal'))
    
    sleep(1)

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
                            
        iterations += 1
        animate_values(grid, iterations)
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
                
    pen.color('red')
    pen.shape('square')
    pen.goto(-264, 264)
    pen.stamp()
                
    wn.update()
                
    #pen.color('red')
    #pen.goto(-264, 264)
    #pen.stamp()
    
def animate_values(grid, iterations):
    
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
                
    pen.color('white')
    pen.goto(-288, -34)
    pen.stamp()
    pen.goto(-268, -34)
    pen.stamp()
    pen.goto(-248, -34)
    pen.stamp()
    pen.goto(-228, -34)
    pen.stamp()
    pen.goto(-208, -34)
    pen.stamp()
    pen.goto(-188, -34)
    pen.stamp()
    pen.goto(-168, -34)
    pen.stamp()
    pen.goto(-148, -34)
    pen.stamp()
    pen.goto(-128, -34)
    pen.stamp()
    
    pen.color('red')
    pen.shape('square')
    pen.goto(-264, 264)
    pen.stamp()
    
    pen.color('black')
    pen.goto(-297, -50)
    pen.write('Iterations: {}'.format(iterations), font=('Arial', 20, 'normal'))
                
    wn.update()
            
pen = Pen()

gradient = gradienthelper.linear_gradient('#FFFFFF', '#008080', 22)
col_list = range(-10, 102, 5)
gradient_dict = {col_list[i]: gradient.get('hex')[i] for i in range(len(gradient.get('hex')))}

if __name__ == '__main__':
    random.seed(103)
    test = AldousBroder.AldousBroder(6, 6).generate()
    setup_maze(test)
    #print(test)
    #test_mdp = AldousBroder.maze_to_mdp(test)
    #test_policy = value_iteration(test_mdp, .9)
    
    
    
    #values = [[state.value for state in row if state != '#'] for row in test_maze.grid]
    #values = sum(values, [])
    
    #setup_maze(test)
    #turtle.done()
    #print(min(values))
    #print(max(values))
    #print(gradient_dict)

    #print(test_maze)
    #print(test_policy_str)