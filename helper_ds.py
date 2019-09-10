#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
import sys
import math
#import helper_fn

#import global_var

#constants




# states of the model
def hash1(floor):
    "Returns hash of 2D list"


    list_int = [int("".join(str(x) for x in row_list), 2) for row_list in floor]
    j = 1
    hash_value = sum([i * j for i, j  in enumerate(list_int, 1)]) % 50000
    return hash_value

class State:

    def __init__(self, floor, pos_x, pos_y):

        self.floor = floor
        self.pos_x = pos_x
        self.pos_y = pos_y


    def left(self):
        self.pos_y = self.pos_y - 1

    def right(self):
        self.pos_y = self.pos_y + 1

    def up(self):
        self.pos_x = self.pos_x - 1

    def down(self):
        self.pos_x = self.pos_x + 1

    def suck(self):
        col = int(math.sqrt(len(self.floor)))
        self.floor[self.pos_x * col + self.pos_y] = 0

    def do_nothing(self):
        pass


    def __str__(self):

        return "floor: " + str(self.floor) + "  " + f"{self.pos_x, self.pos_y}"


# node comprises:
# state, parent, action, path cost, depth

class Node:

    def __init__(self, initial_state, parent, action, path_cost, depth):

        self.initial_state = initial_state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

    def __str__(self):

        return "Printing node" + " state " + \
        str(self.initial_state) + "action: " + str(self.action) \
        + " path cost: " + str(self.path_cost) + " depth " + str(self.depth)

    # Here equality would just mean if there are states are equal or # NOTE:
    # which is suitable for our use case
    def __eq__(self, other):

        if not isinstance(other, State):
            return NotImplemented

        return self.initial_state == other.initial_state

    def __hash__(self):

        return hash((self.initial_state))

    def __sizeof__(self):

        return sys.getsizeof(self.initial_state) + sys.getsizeof(self.action) + \
            sys.getsizeof(self.path_cost) + sys.getsizeof(self.depth) + sys.getsizeof(self.parent)
