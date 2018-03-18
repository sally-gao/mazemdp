import maze
import re
import multiprocessing as mp
import AldousBroder

def divide_grid(grid):
    """Divides the length of a grid into 4 and returns a list of slice indices."""
    
    chunksize = int(len(grid)/4)
    chunk1 = (0, chunksize)
    chunk2 = (chunksize, chunksize*2)
    chunk3 = (chunksize*2, chunksize*3)
    chunk4 = (chunksize*3, len(grid))
    
    return [chunk1, chunk2, chunk3, chunk4]

def get_actions(chunkstart, chunkstop, grid):
    
    """Updates policy for a subsection of the grid with greedy actions.
    Input should be the first and last row of the subsection."""
    
    actions = ['up', 'down', 'left', 'right']
    
    new_actions = []
    
    for i in range(chunkstart, chunkstop):
        acts = []
        
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                a = '#'
            else:
                action_values = {a: grid[getattr(grid[i][j], a)[0]][getattr(grid[i][j], a)[1]].value for a in actions}
                a = max(action_values, key=action_values.get)
            acts.append(a)
            
        new_actions.append(acts)
    return new_actions

def get_values(chunkstart, chunkstop, gamma, grid, policy):
    
    """Gets updated values for a subsection of the grid.
    Input should be the first and last row of the subsection."""
    
    values = []
    
    for i in range(chunkstart, chunkstop):
        vals = []
        
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                v = '#'
            else:
                neighbor = getattr(grid[i][j], policy[i][j])
                v = grid[i][j].reward + gamma * grid[neighbor[0]][neighbor[1]].value
            vals.append(v)
            
        values.append(vals)
    return values

def parallel_pi(grid, gamma):
    
    """Performs parallelized policy iteration on a maze.
    Four processes will be run simultaneously during the value iteration
    and policy update portions of the code."""

    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]

    # Convert all walls to # in policy
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                policy[i][j] = '#'
    
    converged = False
    
    pool = mp.Pool(processes=4) # initialize pool for parallel programming
    
    while not converged:
        
        converged = True
        is_value_changed = True
        
    
        while is_value_changed:
            
            is_value_changed = False
    
            results = [pool.apply_async(get_values, args=(chunk[0], chunk[1], gamma, grid, policy)) for chunk in divide_grid(grid)]
            output = [p.get() for p in results]
            new_values = [row for chunk in output for row in chunk]
    
            # Update MDP state values in the grid
            for i in range(len(new_values)):
                for j in range(len(new_values[i])):
                    if new_values[i][j] == '#': continue
                    if new_values[i][j] != grid[i][j].value: # check for convergence
                        grid[i][j].value = new_values[i][j]
                        is_value_changed = True
        
        # Find new policy based on V(π)
        results = [pool.apply_async(get_actions, args=(chunk[0], chunk[1], grid)) for chunk in divide_grid(grid)]
        output = [p.get() for p in results]
        updated_actions = [row for chunk in output for row in chunk]
    
        # Update policy
        for i in range(len(updated_actions)):
            for j in range(len(updated_actions[i])):
                if updated_actions[i][j] == '#': continue
                if updated_actions[i][j] == policy[i][j]: continue
                policy[i][j] = updated_actions[i][j]
                converged = False
                
    pool.close()
    pool.join()

                    
    return(policy)

    
def prettify_policy(policy):
    policy_str = '\n'.join([''.join(row) for row in policy])
    policy_str = re.sub('up', '↑', policy_str)
    policy_str = re.sub('down', '↓', policy_str)
    policy_str = re.sub('right', '→', policy_str)
    policy_str = re.sub('left', '←', policy_str)
    return(policy_str)

if __name__ == '__main__':
    test_maze = AldousBroder.AldousBroder(3, 3).generate()
    test_mdp = AldousBroder.maze_to_mdp(test_maze)
    test_policy = parallel_pi(test_maze, .9)
    test_policy_str = prettify_policy(test_policy)

    print(test_maze)
    print(test_policy_str)
