#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
from helper_fn import *
from helper_ds import *
from bfs import *
#from test import *
from iterative_deepening import *
import config

goal_floor = dirt_generator(0)
print_floor(goal_floor)
goal_state = State(goal_floor, 0, 0)

store_av_six = open("average_6.py", 'w')

cost_T1 = 0
cost_T2 = 0
for i in range(10):


    floor = dirt_generator()

    state = State(floor, 0, 0)

    print_floor(floor)
    #test_bfs(state)
    solution = breadth_first_search(state, goal_state)

    cost_T1 = cost_T1 + solution.path_cost

    solution = iterative_deepening_search(state, goal_state)

    cost_T2 = cost_T2 + solution.path_cost

    store_av_six.write(f"cost_T1: {cost_T1}, cost_T2: {cost_T2}")

config.R12_T1 = cost_T1 / 10
config.R12_T2 = cost_T2 / 10

print(f"R12_T1: {config.R12_T1}, R12_T2: {config.R12_T2}")

store_av_six.write(f"R12_T1: {config.R12_T1}, R12_T2: {config.R12_T2}")
store_av_six.close()
