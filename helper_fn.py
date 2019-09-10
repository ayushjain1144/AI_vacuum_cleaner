#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
import random
import math
from bitstring import BitArray
import helper_ds

#constants


cost_move = 2
cost_clean = 1

num_nodes = 1



# Dirt Generator
# percentage of dirt = prob (from 0 to 1)


def dirt_generator(size, prob = 0.1):
    """Returns the initial state of the game state"""

    row = size
    col = size

    size = row * col
    floor = BitArray(size)
    floor.set(False)
    #floor = [[0 for x in range(col)] for x in range(row)]

    # sample is used to return unique random values
    for i in random.sample(range(0, size), (int)(size * prob)):

        #r = (int)(i / col)
        #c = (int)(i % col)

        try:
            floor[i] = 1
        except ValueError:
            print("Error, Exiting")

    return floor



def print_floor(list):
    """Prints the floor"""

    size = math.sqrt(len(list))
    print("Printing the current state of floor")
    row = size
    col = size
    for i, j in enumerate(list, 1):

        if j:
            print(1, end=" ")
        else:
            print(0, end= " ")

        if(i % col == 0):
            #print(i, col)
            print("\n", end="")


    #for i in range(row):
    #    for j in range(col):
    #        print(list[i][j], end=" ")

        #print('\n', end="")

# Goal Test
def GoalTest(cur_state, goal_state):
    """Returns True if the current state is the goal state, else False"""

    return cur_state.floor == goal_state.floor

    #and (cur_state.pos_x in [0, row -1] and cur_state.pos_y in [0, col - 1] )

# Successor functiion
# Action is passed as string

def nextState(cur_state, action):
    """Returns a new next state after applying action on current state"""

    floor = [index for index in cur_state.floor]
    new_state = helper_ds.State(floor, cur_state.pos_x, cur_state.pos_y)
    if action == "mr":
        new_state.right()

    elif action == "md":
        new_state.down()

    elif action == "ml":
        new_state.left()

    elif action == "mu":
        new_state.up()


    elif action == "sd":
        new_state.suck()

    elif action == "dn":
        new_state.do_nothing()

    else:
        print("Invalid action demanded, doing nothing :/ ")

    return new_state

# create Root Node functiion

def createRootNode(initial_state):
    """Returns the root node"""

    parent = None
    action = []
    path_cost = 0
    depth = 0
    root_node = helper_ds.Node(initial_state, parent, action, path_cost, depth)

    return root_node

def available_actions(cur_state):
    """Returns the applicable actions in a list"""

    size = math.sqrt(len(cur_state.floor))
    row = int(size)
    col = int(size)
    action_list = []

    if cur_state.floor[cur_state.pos_x * col + cur_state.pos_y] == 1:
        action_list.append("sd")
        return action_list

    if cur_state.pos_x != row - 1:
        action_list.append("md")

    if cur_state.pos_y != col - 1:
        action_list.append("mr")

    if cur_state.pos_y != 0 :
        action_list.append("ml")

    if cur_state.pos_x != 0:
        action_list.append("mu")




    return action_list

def action_cost(action):
    """Returns cost of taking a particular action"""

    if action == "mu" or action == "md" or action == "ml" or action == "mr":
        return cost_move
    elif action == "sd":
        return cost_clean
    else:
        return 0



def child_node(cur_node, action):
    """Returns child node"""

    global num_nodes
    num_nodes = num_nodes + 1

    child_state = nextState(cur_node.initial_state, action)
    cost = action_cost(action)
    child_node = helper_ds.Node(child_state, cur_node, action, cur_node.path_cost + cost, cur_node.depth + 1)

    #if num_nodes % 1000 == 0:
        #print(f"no. of nodes(MILLION): {num_nodes / 1000000}, depth: {cur_node.depth}")
    return child_node

def return_to_goal(cur_node):
    """Returns the final solution node"""

    size = math.sqrt(len(cur_node.initial_state.floor))
    row = int(size)
    col = int(size)

    if row - cur_node.initial_state.pos_x - 1 < cur_node.initial_state.pos_x:
        vert = "md"
        step_vert = row - cur_node.initial_state.pos_x - 1
    else:
        vert = "mu"
        step_vert = cur_node.initial_state.pos_x

    if col - cur_node.initial_state.pos_y - 1 < cur_node.initial_state.pos_y:
        hor = "mr"
        step_hor = col - cur_node.initial_state.pos_y - 1
    else:
        hor = "ml"
        step_hor = cur_node.initial_state.pos_y

    for i in range(step_vert):
        cur_node = child_node(cur_node, vert)

    for i in range(step_hor):
        cur_node = child_node(cur_node, hor)

    return cur_node




def sol_path(solution):
    """Returns the list of actions for reaching goal state"""

    sol_action = []

    while solution.parent:

        sol_action.append(solution.action)
        solution = solution.parent

    sol_action.reverse()
    #print(sol_action)
    return sol_action
