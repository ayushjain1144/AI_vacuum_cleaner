# AI_vacuum_cleaner
This repository contains the code for making an artificially intelligent vacuum cleaner, made using uninformed earch algorithms.

# Problem Description
A 10 by 10 tiled floor is cleaned by an intelligent vacuum cleaner. The vacuum cleaner has two
sensors to perceive the position and dirt of the tile. The actuator actions are MR, ML, MU and MD
respectively for movements in right, left, up, and down directions. The fifth action is 'Suck the dirt' (S)
and the sixth action is 'Do nothing'(N). The action ‘Do nothing’ is meant to indicate the vacuum
cleaner resting action. While the vacuum cleaner can move in the any one of the four directions one
step at a time, its cost is 2 units per step. The dirt is cleaned by the vacuum cleaner by its actuator
brush which sucks the dirt completely from the tile at the cost of 1 unit. The vacuum cleaner cleans the
floor and can rest at any one corner of the room.


Remember that the environment is partially observable and the intelligent agent is able to receive the
percepts from all its 8 neighbors

The PEAS descriptions of the vacuum cleaner agent are as follows
* Performance (P):
* Environment (E):
* Actuator (A):
* Sensors (S):
* Path cost

Room having 10x10 tiles with dirt on randomly selected tiles,
also has 4 resting places for the vacuum cleaner
Wheels and cleaning brush implemented through Graphics
Position and Dirt sensors (percepts can be simulated using a 2D array)

# MODULES

* Dirt Generator
The amount of dirt is fixed and is same for each tile. Randomly select the tiles to introduce the
dirt within. Dirt generator introduces dirt by taking as input the value ‘p’ where ‘p’ is the
percentage of tiles to get the dirt. The dirt generator returns the initial state of the room.
* Function GoalTest (state initialState, goal goalstate) function: Write a function that takes as
input initial and goal states. The function returns true or false depending on whether the goal is
met or not.
* Function nextState (state s, action A): This function takes as input a state s and applies action
A. It returns a new next state.
* Function createRootNode (state initialState): This function creates the root node of the
search tree for input initial state and returns the node address to be preserved for all tree
traversals.
* Uninformed Search technique
Implemented the following techniques to obtain action path given an initial room state.
* Breadth first search (T1)
* Iterative Deepening Search (T2)

# Analysis Module
Produced the following analyses and display the resultant values/path etc. on the GUI.

(a) T1 based analysis
i.
Compute the number of nodes generated till the problem is solved or the memory
cannot be allocated further. [R1]
ii.
Compute the amount of memory allocated to one node. [R2]
iii. Compute the maximum growth of the auxiliary stack or queue (appropriately) used
with the search tree. [R3]
iv.
Produce the action path in text and in graphics both. For graphics, use RED color to
show the path obtained using T1. [G1]
v.
Compute total cost to clean the room. [R4]
vi.
Compute the total time to compute the path. [R5]
(b) T2 based analysis
i.
Compute the number of nodes generated till the problem is solved or the memory
cannot be allocated further. [R6]
ii.
Compute the amount of memory allocated to one node. [R7]
iii. Compute the maximum growth of the auxiliary stack or queue (appropriately) used
with the search tree. [R8]
iv.
Produce the action path in text and in graphics both. For graphics, use RED color to
show the path obtained using T2. [G2]
v.
Compute total cost to clean the room. [R9]
vi.
Compute the total time to compute the path. [R10]
(c) Comparative analysis
i.
Compare the memory used in T1 and T2. [R11]
ii.
Run both the techniques 10 times each with randomly generated initial state of the
room. Compute average cost of the path obtained using T1 and T2 respectively.
[R12]
iii. Plot a graph with two curves displaying the time taken to compute the path by T1
(RED) and T2 (BLUE) against the room size varying from 3 x 3 to 20 x 20 in step
size of 1 in each direction. [G3]
iv.
Similarly plot a curve displaying the time taken to compute the path using T2
against the level of dirt in the room varying from 10% to 100% in step size of 5%.
[G4]

# Driver

Option 1: Display the room environment
Option 2: Find the path (action sequence) and path cost using T1
Option 3: Find the path (action sequence) and path cost using T2
Option 4: Show all results and graphs in the GUI.

Option 1 uses the dirt generator and displays the room environment graphically.
Options 2 and 3 use the appropriate functions and display the result on the console.
Option 4 uses all functions and computes the path using T1 and T2 both and displays all results on the
GUI as specified earlier.

# Dependencies:

* pyqt5
* matplotlib
* python 3.7

# Running Instruction
```javascript
python run.py
```

# Video Demonstration

Please visit this link:
```javascript
https://youtu.be/69iJ83ausyU
```
