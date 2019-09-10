#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
import helper_fn
import helper_ds
import bfs
import iterative_deepening
import time

size = 3

time_G3_bfs = open("G3_bfs.txt", "w")
for i in range(17):

    goal_floor = helper_fn.dirt_generator(size, 0)
    helper_fn.print_floor(goal_floor)
    goal_state = helper_ds.State(goal_floor, 0, 0)

    new_floor = helper_fn.dirt_generator(size, 0.1)
    new_state = helper_ds.State(new_floor, 0, 0)
    start_time = time.time()

    solution = bfs.breadth_first_search(new_state, goal_state)

    time_taken = time.time() - start_time
    print(f"Total time taken: {time_taken}")
    time_G3_bfs.write(f"Total time taken: {time_taken}")
    size = size + 1

time_G3_bfs.close()
