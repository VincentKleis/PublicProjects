'''
    Class representing the state of a robot (named Servus) used for a planning problem in
    the course INFO180 at UoB, Norway
    Written by Bjornar Tessem
'''

from copy import deepcopy

# number to represent the things Servus can have in its hands
FULL_SNACK = 1  # represent a full snack bowl
EMPTY_SNACK = 2  # represent an empty snack bowl
FULL_GLASS = 3  # represent a full glass
EMPTY_GLASS = 4  # represent an empty glass

# number to represent no snack bowl at table
NO_SNACK = 0


class ServusState:
    '''
    The class representing a state of Servus the serving robot, the 12 different actions
    and a method that returns the possible children of a state
    '''

    def is_legal(start):
        '''
        Checks is a servus initial state is legal
        :param start:
        :return:
        '''
        servus_cnt = len(start["hands"])
        t1_cnt = start["t1_full"] + start["t1_empty"]
        t2_cnt = start["t2_full"] + start["t2_empty"]
        t1_snack = start["t1_snack"]
        t2_snack = start["t2_snack"]
        return (2 >= servus_cnt >= 0 and # no more than 2 things in the hands
                3 >= t1_cnt >= 0 and # no more than 3 full or empty glasses at a table
                3 >= t2_cnt >= 0 and
                2 >= t1_snack >= 0 and # status of snack is on of NO_SNACK (0), EMPTY_SNACK (1) or FULL_SNACK (2)
                2 >= t2_snack >= 0)

    def __init__(self, start=None):
        '''
        Constructor for servus' state
        :param start: a dictionary with parameters for initial state
        '''
        if start is None or not ServusState.is_legal(start):
            # creates status with nothing on the tables
            self.servus_loc = 'K'  # initially at kitchen
            self.servus_hands = []
            # nothing in hands, hands is a list of up to two elements,
            # i.e., two things in Servus's hands
            self.t1_empty = 0  # no empty glasses at table 1
            self.t2_empty = 0  # no empty glasses at table 2
            self.t1_full = 0  # no full glasses at table 1
            self.t2_full = 0  # no full glasses at table 2
            self.t1_snack = NO_SNACK  # no snack bowl at table 1
            self.t2_snack = NO_SNACK  # no snack bowl at table 2
        else:
            self.set_state(start)

    def set_state(self, state):
        '''
        Sets the state from a dictionary
        :param state: the dictionary
        :return:
        '''
        self.servus_loc = state["loc"]
        self.servus_hands = deepcopy(state["hands"])
        self.t1_empty = state["t1_empty"]
        self.t2_empty = state["t2_empty"]
        self.t1_full = state["t1_full"]
        self.t2_full = state["t2_full"]
        self.t1_snack = state["t1_snack"]
        self.t2_snack = state["t2_snack"]

    def act_move_k_t1(self):
        '''
        the move action from k to t1
        :return: a new state if action is legal
        '''
        # precondition
        if self.servus_loc == 'K' and EMPTY_GLASS not in self.servus_hands and EMPTY_SNACK not in self.servus_hands:
            # effect (missing)
            return None
        else:
            return None

    def act_move_k_t2(self):
        '''
        the move action from k to t2
        :return: a new state if action is legal
        '''
        # precondition
        if self.servus_loc == 'K' and EMPTY_GLASS not in self.servus_hands and EMPTY_SNACK not in self.servus_hands:

            # effect
            new_state = deepcopy(self)
            new_state.servus_loc = 'T2'
            return new_state
        else:
            return None

    def act_move_t1_k(self):
        '''
        the move action from t1 to k
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect
            new_state = deepcopy(self)
            new_state.servus_loc = 'K'
            return new_state
        else:
            return None

    def act_move_t2_k(self):
        '''
        the move action from t2 to k
        :return: a new state if action is legal
        '''
        # precondition
        if self.servus_loc == 'T2' and FULL_SNACK not in self.servus_hands and FULL_GLASS not in self.servus_hands:

            # effect
            new_state = deepcopy(self)
            new_state.servus_loc = 'K'
            return new_state
        else:
            return None

    def act_move_t1_t2(self):
        '''
        the move action from t1 to t2
        :return: a new state if action is legal
        '''
        # precondition
        if self.servus_loc == 'T1':

            # effect
            new_state = deepcopy(self)
            new_state.servus_loc = 'T2'
            return new_state
        else:
            return None

    def act_move_t2_t1(self):
        '''
        the move action from t2 to t1
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect (missing)
            return None
        else:
            return None

    def act_pickup_glass_k(self):
        '''
        the pickup of glass action in the kitchen
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect
            new_state = deepcopy(self)
            new_state.servus_hands.append(FULL_GLASS)
            return new_state
        else:
            return None

    def act_setdown_glass_k(self):
        '''
        the setdown action of glass in the kitchen
        :return: a new state if action is legal
        '''
        # precondition
        if (self.servus_loc == 'K' and
                EMPTY_GLASS in self.servus_hands):

            # effect
            new_state = deepcopy(self)
            new_state.servus_hands.remove(EMPTY_GLASS)
            return new_state
        else:
            return None

    def act_pickup_snack_k(self):
        '''
        the pickup of snack bowl action in the kitchen
        :return: a new state if action is legal
        '''
        # precondition
        if (self.servus_loc == 'K' and
                len(self.servus_hands) < 2 and
                EMPTY_GLASS not in self.servus_hands and
                EMPTY_SNACK not in self.servus_hands):

            # effect (missing)
            return None
        else:
            return None

    def act_setdown_snack_k(self):
        '''
        the setdown of snack bowl action in the kitchen
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect (missing)
            return None
        else:
            return None

    def act_setdown_glass_t1(self):
        '''
        the setdown of glass action at table 1
        :return: a new state if action is legal
        '''
        # precondition
        if (self.servus_loc == 'T1' and
                FULL_GLASS in self.servus_hands and
                self.t1_full + self.t1_empty < 3):

            # effect
            new_state = deepcopy(self)
            new_state.servus_hands.remove(FULL_GLASS)
            new_state.t1_full = new_state.t1_full + 1
            return new_state
        else:
            return None

    def act_pickup_glass_t1(self):
        '''
        the pickup of glass action at table 1
        :return: a new state if action is legal
        '''
        # precondition
        if (self.servus_loc == 'T1' and
                len(self.servus_hands) < 2 and
                self.t1_empty > 0):

            # effect
            new_state = deepcopy(self)
            new_state.servus_hands.append(EMPTY_GLASS)
            new_state.t1_empty = new_state.t1_empty - 1
            return new_state
        else:
            return None

    def act_setdown_glass_t2(self):
        '''
        the setdown of glass action at table 2
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect
            new_state = deepcopy(self)
            new_state.servus_hands.remove(FULL_GLASS)
            new_state.t2_full = new_state.t2_full + 1
            return new_state
        else:
            return None

    def act_pickup_glass_t2(self):
        '''
        the pickup of glass action at table 2
        :return: a new state if action is legal
        '''
        # precondition
        if (self.servus_loc == 'T2' and
                len(self.servus_hands) < 2 and
                self.t2_empty > 0):

            # effect (missing)
            return None
        else:
            return None

    def act_pickup_snack_t1(self):
        '''
        the pickup of snack action at table 1
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect (missing)
            return None
        else:
            return None

    def act_setdown_snack_t1(self):
        '''
        the setdown of snack action at table 1
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect (missing)
            return None
        else:
            return None

    def act_pickup_snack_t2(self):
        '''
        the pickup of snack action at table 2
        :return: a new state if action is legal
        '''
        # precondition (missing)
        if False:

            # effect (missing)
            return None
        else:
            return None

    def act_setdown_snack_t2(self):
        '''
        the setdown of snack action at table 2
        :return: a new state if action is legal
        '''
        # precondition
        if (self.servus_loc == 'T2' and
                FULL_SNACK in self.servus_hands and
                self.t2_snack == NO_SNACK):

            # effect (missing)
            return None
        else:
            return None

    def generate_children(self):
        '''
        Generates legal actions from a state
        :return: a list of pairs of actions and states
        '''
        result = []
        for act in dir(self):
            # runs through fields and methods of self
            if act.startswith('act_'):
                # for methods that start with act
                # run the method which is obtained from getattr(self, m)() and get a new state
                new_state = getattr(self, act)()
                if new_state is not None:
                    result.append((act, new_state))
        return result

    def __hash__(self):
        '''
        A hash function for the purpose of efficient set representation of Servus states
        :return: a hash function for self
        '''
        result = 0
        if self.servus_loc == 'K':
            result = 0
        elif self.servus_loc == 'T1':
            result = 10
        else:
            result = 20
        result = (result +
                  len(self.servus_hands) * 2 +
                  self.t1_empty * 3 +
                  self.t1_full * 5 +
                  self.t2_empty * 7 +
                  self.t2_full * 11 +
                  self.t2_snack * 13
                  )
        return result

    def __eq__(self, other):
        '''
        Checks if two states are equal
        :param other: an other state
        :return: true if the states have same values in all fields
        '''
        if (self.servus_loc == other.servus_loc and
                self.servus_hands.count(EMPTY_SNACK) == other.servus_hands.count(EMPTY_SNACK) and
                self.servus_hands.count(FULL_SNACK) == other.servus_hands.count(FULL_SNACK) and
                self.servus_hands.count(EMPTY_GLASS) == other.servus_hands.count(EMPTY_GLASS) and
                self.servus_hands.count(FULL_GLASS) == other.servus_hands.count(FULL_GLASS) and
                self.t1_empty == other.t1_empty and
                self.t1_full == other.t1_full and
                self.t1_snack == other.t1_snack and
                self.t2_empty == other.t2_empty and
                self.t2_full == other.t2_full and
                self.t2_snack == other.t2_snack):
            return True
        else:
            return False

    def __str__(self):
        '''
        :return: a (pretty?) print representation of the state
        '''
        # makes a printed list from the hands
        hands = "["
        for i in range(0,len(self.servus_hands)):
            if self.servus_hands[i] == FULL_GLASS: hands = hands + "FULL GLASS"
            elif self.servus_hands[i] == EMPTY_GLASS: hands = hands + "EMPTY GLASS"
            elif self.servus_hands[i] == FULL_SNACK: hands = hands + "FULL SNACK"
            else: hands = hands + " " + "EMPTY SNACK"
            if i < len(self.servus_hands) - 1: hands = hands + ","
        hands = hands + "]"

        # converts numbers to strings
        if self.t1_snack == NO_SNACK: t1_sn = "NO SNACK"
        elif self.t1_snack == FULL_SNACK: t1_sn = "FULL SNACK"
        else: t1_sn = "EMPTY SNACK"
        if self.t2_snack == NO_SNACK: t2_sn = "NO SNACK"
        elif self.t2_snack == FULL_SNACK: t2_sn = "FULL SNACK"
        else: t2_sn = "EMPTY"

        # makes a formated print string
        result = '\nServus({},{})\nT1(FULL GLASS = {}, EMPTY GLASS = {},{})\nT2(FULL GLASS = {}, EMPTY GLASS = {},{})\n'.\
            format(self.servus_loc,
                    hands,
                    self.t1_full,
                    self.t1_empty,
                    t1_sn,
                    self.t2_full,
                    self.t2_empty,
                    t2_sn)
        return result
