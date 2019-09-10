#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
from helper_fn import *
from helper_ds import *
from bfs import *
from iterative_deepening import *
import sys
import time

row = 7
col = 7

goal_state_floor = dirt_generator(5, 0)
goal_state = State(goal_state_floor, 0, 0)



list = dirt_generator(5, 1)
cur_state = State(list, 4, 5)

print("printing state")


print("Checking for goal state")

if GoalTest(cur_state, goal_state):
    print("Yes, we got the goal")
else:
    print("No, not the goal state")



"""testing for nextstate func"""

print_floor(cur_state.floor)
print(f"Initial state: {cur_state.pos_x}, {cur_state.pos_y}" )
print("state after going left")
new_state = nextState(cur_state, "move_left")
print_floor(cur_state.floor)
print(f"Next state state: {new_state.pos_x}, {new_state.pos_y}" )


"""testing createRootNode """


node = createRootNode(cur_state)
list1 = dirt_generator(5, 0.1)
cur_state1 = State(list, 0, 0)
print("size of node: ")
print(sys.getsizeof(node))





"""testing available_actions"""

dirty_floor = dirt_generator(5)
cur_state = State(dirty_floor, 0, 3)
print_floor(dirty_floor)
action_list = available_actions(cur_state)
print(action_list)


"""testing action_cost """

print("\n\n")

print("testing action cost function")

cost = action_cost("ml")
print(cost)

"""testing return child node"""
print("\n\n\n\n")
cur_state = State(dirty_floor, 3, 2)
cur_node = createRootNode(cur_state)
child_node = child_node(cur_node, "ml")
print_floor(cur_node.initial_state.floor)
print("\n\n")
print_floor(child_node.initial_state.floor)
print("size of node: ")
print(sys.getsizeof(node))
print(child_node.action)

"""testing state equality"""
print("testing state equality")
cur_state = State(dirt_generator(5, 1), 2, 1)
other_state = nextState(cur_state, "sd")
print_floor(cur_state.floor)
print("\n")
print_floor(other_state.floor)
print(cur_state == other_state)

"""testing bfs search"""
def test_bfs(new_state):

    print("\n\nStarting testing bfs search\n\n")


    print_floor(new_state.floor)

    solution = breadth_first_search(new_state, goal_state)

    print(solution.path_cost)
    print_floor(solution.initial_state.floor)
    print("\n\n")
    print_floor(new_state.floor)
    print("\n\n")

    print(f"This is the solution path: {sol_path(solution)}")

"""testing IDS"""
def test_idfs(new_state):

    global num_nodes

    start_time = time.time()
    print("\n\n Starting testing IDFS\n\n")

    print_floor(new_state.floor)

    solution = iterative_deepening_search(new_state, goal_state)

    print_floor(solution.initial_state.floor)
    print("\n\n")
    print_floor(new_state.floor)

    print(f"This is the solution path: ")
    for action in sol_path(solution):
        print(f"{action} to ", end="")
    print("goal")

    print("\n\n\n")

    print(f"Total num_nodes: {num_nodes}")

    print(f"Total cost: {solution.path_cost}")

    time_taken = time.time() - start_time
    print(f"Total time taken: {time_taken}")

"""testing return_to_goal fn"""

s1 = State(dirt_generator(5), 2, 3)
n1 = createRootNode(s1)

c1 = return_to_goal(n1)
print(c1.initial_state.pos_x, c1.initial_state.pos_y, c1.path_cost)

new_state = State(dirt_generator(5, 0.1), 0, 0)
test_bfs(new_state)
#test_idfs(new_state)
