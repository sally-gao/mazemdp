# mazemdp
Exploring MDP solving algorithms with mazes!

Sally Gao, Duncan Rule, Yi Hao

****

## Research question(s):
Our central research pursuit is to compare the speed of different techniques for Markov
Decision Processes (MDPs) in the context of solving mazes. Faster solving times are desirable
in situations where many states are possible. In addition to value iteration and policy iteration,
one technique that may improve performance is policy iteration with parallel processing. The
calculation of V<sub>π</sub>(s) and π(s) within each iteration can be parallelized because these values can
be derived individually.

We will simulate randomized maze environments of varying sizes that are populated with a
variety of obstacles. We will then compare computation times of (A) value iteration, (B) policy
iteration and (C) policy iteration with parallel processing with varying maze sizes.
We expect that:

   1. Value iteration will always be the slowest performer
   2. Given smaller problem sizes, non-parallel policy iteration will perform the best due to the
   fixed overhead associated with parallel processing, but with larger problems, the
   performance of policy iteration with parallel processing will exceed that of non-parallel
   policy iteration.


Our specific research question is: How does the computation time grow for each MDP-solving
technique as the size of our problem becomes larger?

## Description of data to be used:
Our data will be in the form of randomly generated maze environments, constructed with an
adapted version of the Depth First maze generation algorithm<sup>[1](http://rosettacode.org/wiki/Maze_generation#Python)</sup>. The algorithm will output a grid
of a user-specified size, with each state occupied by either a wall, an empty space, or an
obstacle (if time allows, we will add randomly placed hostile agents). This output will then be
automatically translated into an object oriented implementation of MDP-focused gridworld: each
open space in the maze will have reward and value attributes, as well as attributes linking to
neighboring spaces. If time allows, we will also provide a Flask-based web application allowing
a user to create a valid maze environment of their own, which will be processed in the same
way.

## Planned methodology:
Here are the specific steps we will follow:

  1. For each randomly generated maze, compute the time it takes to “solve” the maze using
  (A) value iteration, (B) policy iteration and (C) policy iteration with parallel processing.
  2. Repeat using varying maze sizes. For instance, we may use 10x10 grids 100 times,
  25x25 grids 100 times, 50x50 grids 100 times, 100x100 grids 100 times, and so on.
  3. Plot the average solving time against grid size for all three methods to compare
  computation times.
  4. (Extra) Develop a web interface that allows the user to define a limited set of maze
  parameters and show the computed solution visually.
  
If we have time, we will also investigate solving VERY large mazes using approximation
algorithms for MDPs <sup>[2](https://arxiv.org/abs/1710.09988)</sup>. If we have even more time, we will investigate using ε-MDPs to handle
dynamic environments (for instance, the presence of a moving hostile agent in the maze).
