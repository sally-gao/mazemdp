import maze
import re

"""
Duncan Rule, Sally Gao, Yi Hao
"""


def value_iteration(grid, gamma):
    """
    Performs value iteration on a given grid of MDPState objects.
    """

    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]
    actions = ['up', 'down', 'left', 'right']

    is_value_changed = True
    
    iterations = 0
    
    # iterate values until convergence
    while is_value_changed:
        is_value_changed = False
        for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] != '#':
                        q = []
                        for a in actions:
                            neighbor = getattr(grid[i][j], a) # Get coordinates of neighboring cell
                            q.append(grid[i][j].reward + gamma * grid[neighbor[0]][neighbor[1]].value)
                        v = max(q)
                        
                        if v != grid[i][j].value:
                            is_value_changed = True
                            grid[i][j].value = v
                            
        iterations += 1
                            
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
    
def prettify_policy(policy):
    policy_str = '\n'.join([''.join(row) for row in policy])
    policy_str = re.sub('up', '↑', policy_str)
    policy_str = re.sub('down', '↓', policy_str)
    policy_str = re.sub('right', '→', policy_str)
    policy_str = re.sub('left', '←', policy_str)
    return(policy_str)

if __name__ == '__main__':
    test_maze = maze.Maze(w=20, h=20)
    test_policy = value_iteration(test_maze.grid, .9)
    test_policy_str = prettify_policy(test_policy)

    print(test_maze)
    print(test_policy_str)
                    