import turtle
from time import sleep
import threading

def draw_dragon(dragon_iters= 10):
    """first dragon curve drawing function, takes the number of itterations you want of a 
    dragon curve and draws untill the last itteration is compleete

    Args:
        dragon_iters (int, optional): number of dragon curve itterations. Defaults to 10.
    """

    n_lines = (dragon_iters**2)-1
    x = 0
    path = ["r"]
    line_size = round(1000/n_lines)

    turtle.speed(0)

    while x < dragon_iters:
        
        turtle.forward(line_size)

        coppy = path.copy()

        reversed_range = reversed(list(range(len(coppy))))

        turtle.right(90)
        path.append("r")
        for i in reversed_range:
            turtle.forward(line_size)
            if path[i] == "l":
                turtle.right(90)
                path.append("r")
            if path[i] == "r":
                turtle.left(90)
                path.append("l")

        x += 1

def path_calc(dragon_iters)->list:
    """calculates the path that the turtle has to go to draw the dragoncurve of itteration n

    Args:
        dragon_iters (_type_): the itteration you want of the dragoncurve

    Returns:
        list: list of directions to turn in the form of ["r","l"....] 
            there is a presumed forward motion before each directional turn, and they are presumed to be 90 degree turns
    """
    x = 0
    path = ["r"]

    while x < dragon_iters:

        coppy = path.copy()

        reversed_range = reversed(list(range(len(coppy))))

        path.append("r")
        for i in reversed_range:
            if path[i] == "l":
                path.append("r")
            if path[i] == "r":
                path.append("l")

        x += 1

    return path


def draw(path, line_size, init_left:int=0 , color="black", speed=0):
    """creates a new tutrtle and draws the path in the path variable

    Args:
        path (_type_): a path of instructions in the form of list of 
            strings where r is 90 degree turn right and l is a 90 degree turn left.

        line_size (_type_): the length of the lines between each turn.

        init_left (int, optional): initial left turn, used for cases where you want to 
            draw multiple curves with the same starting point. Defaults to 0.

        color (str, optional): color of the lines, uses the turtle color scheem. Defaults to "black".
        speed (int, optional): drawing speed of the turtle. Defaults to 0.
    """
    turtle_n = turtle.RawTurtle(screen)
    turtle_n.color(color)
    turtle_n.left(init_left)

    turtle_n.speed(speed)
    for i in path:
        turtle_n.forward(line_size)

        if i == "r":
            turtle_n.right(90)
        
        if i == "l":
            turtle_n.left(90)


def quad_drag_draw(dragon_iters=10):
    """creates 4 dragons that use 4 individual threads of the computer cpu to draw a curve

    Args:
        dragon_iters (int, optional): the itteration of dragon curve you want to draw. Defaults to 10.
    """

    line_size = 2
    path = path_calc(dragon_iters)

    draw(path, line_size, 0, "black")
    draw(path, line_size, 90, "red")
    draw(path, line_size, 180, "green")
    draw(path, line_size, 270, "blue")

    """ matplotlib ,the underlying method that turlte uses for drawing, is not thread safe, 
    meaning that multithreading can cause issues of un ordered data collection at the end of processes,
    so the dragon curve can be drawn with multiple turtles but not at the same time, 
    unless i somehow collect the data that the turtles ar making and the draw it to the main canvas as the turtles are drawing,
    but this is outside of the scope of the project i wanted to make"""

    # t1 = threading.Thread(target=draw, args=(path, line_size, 0, "black",))
    # t2 = threading.Thread(target=draw, args=(path, line_size, 90, "red",))
    # t3 = threading.Thread(target=draw, args=(path, line_size, 180, "green",))
    # t4 = threading.Thread(target=draw, args=(path, line_size, 270, "blue",))

    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()


def calc_and_zoom(turt:turtle):
    """Currently not working, is suposed to calculate the position of a 
    turtle compared to the edge of the window and expand the window if the turtle gets near the edge

    Args:
        turt (turtle): _description_
    """
    pos = turt.pos()
    x_pos, y_pos = pos
    x_pos, y_pos = (x_pos**2)**(1/2), (y_pos**2)**(1/2)
    x_screen, y_screen = screen_size

    if x_pos > x_screen or y_pos > y_screen:
        print(True)
        for x in range(0,20):
            x_screen += 1
            y_screen += 1
            screen.screensize(x_screen, y_screen)
            screen.update()

    print(pos, screen_size)

screen = turtle.Screen()
screen_size = turtle.screensize()

quad_drag_draw(5)

turtle.mainloop()