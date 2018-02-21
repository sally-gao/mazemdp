# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:21:58 2018

@author: Duncan
"""

from random import shuffle, randrange

def make_maze(w = 16, h = 16):
    """
    Creates a maze of specified size.
    Output is a list of lists, to be used as a matrix with coordinates.
    '#' = wall
    ' ' = empty space
    
    Adapted from http://rosettacode.org/wiki/Maze_generation#Python
    """
    h = int(h/2)
    w = int(w/2)
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["# "] * w + ['#'] for _ in range(h)] + [[]]
    hor = [["##"] * w + ['#'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "# "
            if yy == y: ver[y][max(x, xx)] = "  "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
        
    s = s.split('\n')
    s = [list(row) for row in s]
    del s[len(s)-1]
    del s[len(s)-1]
    
    return s
 
if __name__ == '__main__':
    print(make_maze())
    