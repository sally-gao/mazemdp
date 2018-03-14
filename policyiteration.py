# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:07:18 2018

@author: Duncan
"""

import maze
import re

def policy_iteration(grid, gamma):
    is_policy_changed = True
    
    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]
    actions = ['up', 'down', 'left', 'right']
    
    # Policy iteration
    while is_policy_changed:
        is_policy_changed = False
        #print(policy)
        # Policy evaluation
        # Transition probabilities not shown due to deterministic setting
        is_value_changed = True
        while is_value_changed:
            is_value_changed = False
            # Run value iteration for each state
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '#':
                        policy[i][j] = '#'
                    else:
                        neighbor = getattr(grid[i][j], policy[i][j])
                        v = grid[i][j].reward + gamma * grid[neighbor[0]][neighbor[1]].value
                        # Compare to previous iteration
                        if v != grid[i][j].value:
                            is_value_changed = True
                            grid[i][j].value = v
                                
        # Once values have converged for the policy, update policy with greedy actions
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '#':
                    # Dictionary comprehension to get value associated with each action
                    action_values = {a: grid[getattr(grid[i][j], a)[0]][getattr(grid[i][j], a)[1]].value for a in actions}
                    best_action = max(action_values, key=action_values.get)
                    # Compare to previous policy
                    if best_action != policy[i][j]:
                        is_policy_changed = True
                        policy[i][j] = best_action
                    
    return(policy)
    
def prettify_policy(policy):
    policy_str = '\n'.join([''.join(row) for row in policy])
    policy_str = re.sub('up', '↑', policy_str)
    policy_str = re.sub('down', '↓', policy_str)
    policy_str = re.sub('right', '→', policy_str)
    policy_str = re.sub('left', '←', policy_str)
    return(policy_str)

if __name__ == '__main__':
    test_maze = maze.Maze(w=20, h=20)
    test_grid = maze.maze_to_mdp(test_maze)
    test_policy = policy_iteration(test_grid, .9)
    test_policy_str = prettify_policy(test_policy)

    print(test_maze)
    print(test_policy_str)
