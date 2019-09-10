#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
from helper_fn import *
from helper_ds import *
from bfs import *
from iterative_deepening import *
import time

goal_floor = dirt_generator(0)
print_floor(goal_floor)
goal_state = State(goal_floor, 0, 0)

time_G4 = open("G4.txt", 'w')

p = 0.1
increment = 0.05

for _ in range(18):

    new_floor = dirt_generator(p)
    new_state = State(new_floor, 0, 0)
    start_time = time.time()

    solution = iterative_deepening_search(new_state, goal_state)

    time_taken = time.time() - start_time
    print(f"Total time taken: {time_taken}")
    time_G4.write(f"Total time taken: {time_taken}")
    p = p + increment

time_G4.close()
