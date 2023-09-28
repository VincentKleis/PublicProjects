from abc import abstractmethod
from logging import PlaceHolder


def detailed_knap_sack(values: list, weights: list, max_cap: int) -> list:
    n = len(values)
    # creates a grid the size of the capacity times the number of values
    grid = [[0 for x in range(max_cap + 1)] for x in range(n +1)]
    
    for item in range(n + 1):
        for cap in range(max_cap + 1):

            # if the current item or the current test capasity is equal to 0 add 0 to that part of the grid
            if item == 0 or cap == 0:
                grid[item][cap] = 0
            # else if the weight of the current item is les than the cap chose the maximum between, the previus optimum pluss current object and the the previus optimum.
            elif weights[item-1] <= cap:
                grid[item][cap] = max(values[item - 1] +
                                grid[item - 1][cap - weights[item - 1]],
                                grid[item - 1][cap])
            # else choose the previus optimum
            else:
                grid[item][cap] = grid[item - 1][cap]
    print(*grid, sep='\n')
    return grid[n][max_cap]

values = [120, 200, 150, 350, 100, 90]
weights = [15, 20, 40, 50, 20, 10]
capacity = 100

print(detailed_knap_sack(values, weights, capacity))

# ex 2
class student:

    def __init__(self, name, id, address, grade):
        self.name = name
        self.id = id
        self.address = address
        self.grade = grade
    
    def set_address(self, address):
        self.address = address
    
    def get_address(self):
        return self.address
    
    def set_grade(self, grade):
        self.grade = grade
    
    def get_grade(self):
        return self.grade

# ex 3
class Comunication:
    home = None

    def call_home(self, message):
        """Sends a message to pre defined home

        Args:
            message (_type_): message that is sendt
        """
    
    def send_message(self, message, destination):
        """Sends message to a given destination

        Args:
            message (_type_): message that is sendt
            destination (_type_): destination the message is sendt
        """

class Engine:
    tilt = 0
    yaw = 0
    fuel = None
    acceleration = None
    positon = None

    def enter_orbit(self, orbit_path):
        """Takes a path for entering orbit and launches the rocket into orbit, burning fuel in the process and uppdating position

        Args:
            orbit_path (_type_): vektors for each point in time between launch and orbit
        """

    def exit_orbit(self, land_path):
        """Takes a path for exiting orbit and lands the rocket on the closest object, burning fuel and uppdating position in the process

        Args:
            orbit_path (_type_): vectors for every point in time between execution and touch down
        """


class RocketShip:

    def __init__(self, fuel, time, home):
        Engine.fuel = fuel
        self.time = time
        Comunication.home = home

    @abstractmethod
    def launch(self):
        """Calculates orbit, executes Engine.enter_orbit(orbit_path) with the path for orbit
        """
    
    @abstractmethod
    def land(self):
        """Calculates landing, executes Engine.exit_orbit(land_path) with the path for landing on the closes object
        """
    
    def crfuuise(self):
        """Progresses time and uppdates position
        """

    def call_home(self, message):
        Comunication.call_home(message)

    def send_message(self, message, destination):
        Comunication.send_message(message, destination)

#ex 4
# https://drive.google.com/file/d/12r17_ChYLPdpkgw59rRO7ZsHIhWTycQG/view?usp=sharing

