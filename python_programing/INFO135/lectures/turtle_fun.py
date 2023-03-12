import turtle
import math

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, length, degrees):
    if length > 0:
        my_turtle.forward(length)
        my_turtle.right(degrees)
        draw_spiral(my_turtle, length - 1, degrees)

def draw_spiral_midle(my_turtle, lenght, degrees):
    my_turtle.color("white")
    my_turtle.goto(-lenght/2, lenght/2)
    my_turtle.color("black")
    draw_spiral(my_turtle, lenght, degrees)

def queen_tree(my_turtle, board_size:int):
    ...

def eight_queens(board_size:int) -> list:

    queen_posible_positions = []
    for x in range(0, board_size):
        queen_posible_positions.append([(x, 0)])
    
    

            




my_win.exitonclick()