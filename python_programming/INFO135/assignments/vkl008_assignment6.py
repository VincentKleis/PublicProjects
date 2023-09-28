# 1. "wich of the folowing options best represents the comparisons of pre order traversal in the given binary tree"
# answe: a)

# 2. "write a class called QuizGift, with the method compute_result() and print_result(), print_result() should print result, 
# and compute result should solve the folowing:
# Sara is going to attend a written quiz where she can receive a prize based
# on the number of points she obtains. The written quiz has 5 questions each
# of them is worth different points and each takes different amount of time to
# answer. Sara will have 100 minutes and can choose which subset of
# questions to answer from the following question set:
# • Question 1 has 120 points and it takes 15 minutes to answer
# • Question 2 has 200 points and it takes 20 minutes to answer
# • Question 3 has 150 points and it takes 40 minutes to answer
# • Question 4 has 350 points and it takes 50 minutes to answer
# • Question 5 has 100 points and it takes 20 minutes to answer
# • Question 6 has 90 points and it takes 10 minutes to answer
# Sara will receive a watch if she obtains up to 250 points, a smartphone if
# she obtains 250 - 750 points, and, a laptop if she obtains more than 750
# points. Sara would like to have a Python program, based on Dynamic
# Programming, to compute the maximum number of points she can obtain (in
# the given time) and to print it out. The program should also print the gift
# that she will receive as the result of answering the quiz. Please help her!"
# this is the knapsack problem, i use code from the lecture on knapsack problem and i test the results to print the optimal gift.

class QuizGift:
    def knapsack_dp(self, capacity: int, weights: list, values: list, n: int):
        """takes two lists of weight and values and tries to optimize based on the capasity, capasity referes to the weight

        Args:
            capacity (int): weight capacity
            weights (list): how much the item of index x is weighted
            values (list): the value of item of index x
            n (int): number of item indexes

        Returns:
            _type_: optimal solution
        """
        grid = [[0 for x in range(capacity + 1)]
                for x in range(n + 1)]

        for item in range(n + 1):
            for cap in range(capacity + 1):

                if item == 0 or cap == 0:
                    grid[item][cap] = 0

                elif weights[item - 1] <= cap:
                    grid[item][cap] = max(values[item - 1] +
                                    grid[item - 1][cap - weights[item - 1]],
                                    grid[item - 1][cap])
                
                else:
                    grid[item][cap] = grid[item - 1][cap]

        return grid[n][capacity]

    def compute_result(self):
        item_val = [120, 200, 150, 350, 100, 90]
        item_weight = [15, 20, 40, 50, 20, 10]
        cap = 100
        n = len(item_val)
        self.solution = self.knapsack_dp(cap, item_weight, item_val, n)

    def print_result(self):
        result = self.solution
        if result < 250:
            print("Sara obtains a watch")
        elif result >= 250 and result <= 750:
            print("Sara obtains a smartphone")
        elif result > 750:
            print("Sara obtains a laptop")
        else:
            print("Sara was unable to obtain anything")

test = QuizGift()
test.compute_result()
test.print_result()

# 3. "Write an inteface Shape that has the abstract method compute_area() then write the folowing classes, all implementing Shape:
#   a) Square class that has a constructor which receives as parameter the
#       side of the square and sets it as an instance variable. This class should
#       implement compute_area() method to compute and print the area
#       of the square (area of square = side * side)
#   b) Circle class that has a constructor which receives as parameter radius
#       of the circle and sets it as an instance variable. This class should
#       implement compute_area() method to compute and print the area
#       of the circle (area of circle = 3.14 * radius * radius)
#   c) Triangle class that has a constructor which receives as parameters
#       the values of the 3 sides of the triangle and sets them as instance
#       variables. This class should implement compute_area() method to
#       compute and print the area of triangle, based on the following formula:"
from abc import abstractmethod
from math import pi, sqrt
class Shape:
    @abstractmethod
    def compute_area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, side_lengt:int = 0):
        self.area = side_lengt*side_lengt

class Circle(Shape):
    def __init__(self, radius:int = 0):
        self.area = round(pi*radius**2,2)

class Triangle(Shape):
    def __init__(self, a:int=0, b:int=0, c:int=0):
        """takes a list of three lengths of a triangle and calculates the area

        Args:
            side_lengths (list, optional): thre lengths, each of one side of the triangle.
        """
        s = (a+b+c)/2
        self.area = sqrt(s*(s-a)*(s-b)*(s-c))

my_square = Square(2)
my_circle = Circle(2)
my_triangle = Triangle(5, 4, 3)
print('Area of square:', end=' ')
my_square.compute_area()
print('Area of circle:', end=' ')
my_circle.compute_area()
print('Area of triangle:', end=' ')
my_triangle.compute_area()

# 4.
class House:
    count = 0

    def __init__(self, owner:str, price:int, condition:str):
        self.owner = owner
        self.price = price
        self.condition = condition
        self.cost = 0
        self.sold = False
        House.count += 1

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        profit = self.price - self.cost
        print(f'House sold! Profit: {profit}')

    def change_price(self, new_price):
        if self.sold is True:
            print('House has been sold')
        else:
            self.price = new_price
    
    def renovate(self, expense, new_condition):
        self.cost += expense
        self.condition = new_condition
        print('House renovated!')
    
    def print_info(self):
        print(f'Owner: {self.owner}, Condition: {self.condition}, Price: {self.price}')

house1 = House('John', 100000, 'Good')
house2 = House('Sara', 250000, 'Bad')
print()
house1.print_info()
house2.print_info()
print()
house1.renovate(50000, 'Great')
house1.sell('Leo')
print()
house1.print_info()
print(f'Total number of Houses: {House.count}')
