
#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
from helper_ds import *
from helper_fn import *
from collections import deque



def breadth_first_search(initial_state, goal_state):
    """Returns a solution or failure"""

    hash_table = [[] for _ in range(10000)]

    print("Starting BFS")

    root_node = createRootNode(initial_state)

    if GoalTest(root_node.initial_state, goal_state):
        print("Solution found!! Yipee!!")
        return return_to_goal(root_node)

    frontier = deque([root_node])
    explored = []

    i = 0
    while True:

        try:
            if not frontier:
                print("frontier empty")
                return False

            node = frontier.popleft()
            explored.append(node.initial_state)



            action_list = available_actions(node.initial_state)
            #print(action_list)

            for action in action_list:
                child = child_node(node, action)
                if(not child):
                    print("no more memory")
                    return False

                #it first explores hash, if hash matches, then it has to ensure it is genuine match and not a collision.
                #Otherwise we might not be able to reach optimal solution

                if (child.initial_state in explored or child in frontier):
                    pass

                else:

                    if GoalTest(child.initial_state, goal_state):
                        print("Solution found!! Yipee!!")
                        return return_to_goal(child)
                    frontier.append(child)


        except MemoryError as error:

            log_exception(error)
            print("Memory exhausted")
            return False
