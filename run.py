#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
import helper_fn
import helper_ds
import bfs
#from test import *
import iterative_deepening
#import config
from gui import *
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dirt_gui import *
#from global_var import row, col


print("Hello human! Welcome to smart AI Vacuum Cleaner")
print("I am here to clean your room")
print("\n\nBefore you expect too much out of me, there are limitations to my capabilities")
print("\nIDFS\tdirt = 0.1, floor_size: works till 7, but best for size 5")
print("\nBFS\tdirt = 0.1, floor_size: works till 6, but best for size 5")
print("\n\nDisclaimer: There is a tradeoff in dirt and size")
print("\n\nYou can go upto dirt: 0.25 in floor of size 5")
print("A lot depends on your luck i.e. how far the dirt is from origin")
print("\nBest of Luck")
print("\n But before you need to tell me the size of the floor: ", end="")
while(True):
    try:
        size = int(input())
        break
    except Exception:
        print("You need to enter integer values: ", end="")


print("Thank you")
print("\nPlease enter the dirt percentage(from 0 to 1, eg: 0.1): ", end="")
p = float(input())

while(p > 1 or p < 0):
    print("You wanna mess up with me...Now enter value betweem 0 and 1: ",end="")
    p = float(input())
print("Thank You")    
print("\nChoose among the following actions to proceed: ")
print("\tOption 1: Display room environment")
print("\tOption 2: Find the path (action sequence) and path cost using T1")
print("\tOption 3: Find the path (action sequence) and path cost using T2")
print("\tOption 4: Show all results and graph in the GUI")
print("\tOption 5: Bye Bye")
option = input()

row = size
col = size

goal_floor = helper_fn.dirt_generator(size, 0)
#print_floor(goal_floor)
goal_state = helper_ds.State(goal_floor, 0, 0)


floor = helper_fn.dirt_generator(size, p)
state = helper_ds.State(floor, 0, 0)

sol_bfs = None
sol_idfs = None
action_path_bfs = None
action_path_idfs = None

while option != "5":

    if option == "1":
        helper_fn.print_floor(floor)
        print(f"x coordinate of vacuum cleaner: {state.pos_x}")
        print(f"y coordinate of vacuum cleaner: {state.pos_y}")


        app = QApplication(sys.argv)
        ex = Current_State(state, size)
        sys.exit(app.exec_())

    if option == "2":
        helper_fn.print_floor(floor)
        print(f"x coordinate of vacuum cleaner: {state.pos_x}")
        print(f"y coordinate of vacuum cleaner: {state.pos_y}")
        sol_bfs = bfs.breadth_first_search(state, goal_state)

        print(f"This is the solution path: {bfs.sol_path(sol_bfs)}")
        print(f"Path cost : {sol_bfs.path_cost}")

    if option == "3":
        helper_fn.print_floor(floor)
        print(f"x coordinate of vacuum cleaner: {state.pos_x}")
        print(f"y coordinate of vacuum cleaner: {state.pos_y}")
        sol_idfs = iterative_deepening.iterative_deepening_search(state, goal_state)

        print(f"This is the solution path: {bfs.sol_path(sol_idfs)}")
        print(f"Path cost : {sol_idfs.path_cost}")

    if option == "4":

        #sol_bfs = bfs.breadth_first_search(state, goal_state)
        #action_path_bfs = helper_fn.sol_path(sol_bfs)
        #sol_idfs = iterative_deepening.iterative_deepening_search(state, goal_state)
        #action_path_idfs = helper_fn.sol_path(sol_idfs)
        """
        Note: This action path is computed using the commented out fns.
        As advised, we are using precomuted values
        It can be verified by calling bfs on floor generated below
        """

        floor = helper_fn.dirt_generator(5, 0)
        floor[8] = 1
        floor[18] = 1
        state = helper_ds.State(floor, 0, 0)
        helper_fn.print_floor(floor)
        print(f"x coordinate of vacuum cleaner: {state.pos_x}")
        print(f"y coordinate of vacuum cleaner: {state.pos_y}")
        action_path_bfs = ["mr", "mr", "mr", "md", "sd", "md", "sd", "md", "md", "mr"]
        action_path_idfs = ["mr", "mr", "mr", "md", "sd", "md", "sd", "md", "md", "mr"]


        app = QApplication(sys.argv)
        ex = AI_Vacuum(state, action_path_bfs, action_path_idfs)
        sys.exit(app.exec_())



    print("\n\nChoose among the following actions to proceed: ")
    print("\tOption 1: Display room environment")
    print("\tOption 2: Find the path (action sequence) and path cost using T1")
    print("\tOption 3: Find the path (action sequence) and path cost using T2")
    print("\tOption 4: Show all results and graph in the GUI")
    print("\tOption 5: Bye Bye")
    option = input()
    print("\n")
