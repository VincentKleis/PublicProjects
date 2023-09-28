# exercise math in python & using asser
import math

from matplotlib.pyplot import grid
def calculate_function(x):
    x = 4*math.pi*((math.sqrt(3/x))+(x**6))
    return x

def test_function(test_value):
    try:
        assert calculate_function(test_value)
        print(calculate_function(2))
    except:
        print('this function is false')


test_function(1)
# Battleships
import string
class Battleships():
    def __init__(self):
        self.gridPlayer1 = [(x, y, 'ship_type', 'not shot') for x in range(1, 11) for y in string.ascii_lowercase[0: 10]]
        self.gridPLayer2 = self.grid1

    def place_ship(self, ship:int, midle_position:tuple, rotation:bool):
        """takes the ship number, the position, and if the ship is rotated and uses the information to fill in the gridd where the ship is placed. 

        Args:
            ship (int): number from one to 6 corresponding to the chosen ship
            midle_position (tuple): the position of the ships midlepoint
            rotation (bool): if the ship is rotated or not
        """
    
    def test_overlapp(self, ship:int, midle_positon:tuple) -> bool:
        """test if a given ship is overlapping with existing ships on the grid. returns true or falce

        Args:
            ship (int): number from one to 6 corresponding to the chosen ship
            midle_position (tuple): the position of the ships midlepoint

        Returns:
            bool: if there is a overlapp or not
        """
    
    def dipslay_game(self):
        """dissplays the grid with the ships on it based on the tuples of position and ship type
        """
    
    def shoot_position(self, position:tuple)->bool:
        """shoots at a location on the oposit players board, test if the hit hits a ship, if the hit wipes a ship, and if the hit ends the game;
        diplay a message to the current player based on the result from the three tests

        Args:
            position (tuple): the position on the grid that the current playing tries to shoot at

        Returns:
            bool: if it is a hit or not
        """
    def test_if_sunk(self, position:tuple)->bool:
        """takes a the position of a shot and sees if it makes a ship sink

        Args:
            position (tuple): position of a shot

        Returns:
            bool: if a ship is sunk or not
        """
    
    def test_if_end(self):
        """test if there are more ships left
        """
    
    def play(self):
        """starts of by displaying a message showing that it's player1's turn and that player2 should not loog. 
        then asks player1 to place their ship while showing an epty gridd, uses the place_ship() function to place the ships and test for overlapp, 
        for each ship placed the grid is updated. 
        when the first player has placeded their ships do the same for player2.

        after all the ships have been placed alternate turns between player1 and player2, each time diplaying whoos turn it is and asking the oposing player to look away.
        each turn consist of promptiong the current player for a location to shoot while displaying a gridd of hit or un-hit spots 
        on the oposing players gridd and the current players gridd, a message telling if the shot hitt, and an uppdate to both grids.
        """

# UML taks
 