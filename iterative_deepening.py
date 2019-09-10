#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
from helper_fn import *
from helper_ds import *

def recursive_dls(node, goal_state, limit):
    """Returns a solution, a failure or cutoff"""


    if GoalTest(node.initial_state, goal_state):
        return node
    elif limit == 0:
        #print("Limit is 0, returning")
        return "cutoff"

    else:

        cutoff_occurred = False
        action_list = available_actions(node.initial_state)
        for action in action_list:

            child = child_node(node, action)
            result = recursive_dls(child, goal_state, limit - 1)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result
        if cutoff_occurred:
            child.parent = None
            return "cutoff"
        else:
            child.parent = None
            return "failure"


def depth_limited_search(initial_state, goal_state, limit):
    """returns solution or failure or cutoff"""

    return recursive_dls(createRootNode(initial_state), goal_state, limit)

def iterative_deepening_search(initial_state, goal_state):

    print("Starting IDFS")
    depth = 0
    while True:

        result = depth_limited_search(initial_state, goal_state, depth)
        if result != "cutoff":
            return return_to_goal(result)

        depth = depth + 1
