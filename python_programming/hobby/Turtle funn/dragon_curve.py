import turtle
from time import sleep
import threading

def draw_dragon(dragon_iters= 10):
    turtle.penup()
    turtle.home()
    turtle.clear()
    turtle.pendown()

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
    turtle_n = turtle.Turtle()
    turtle_n.color(color)
    turtle_n.left(init_left)

    turtle_n.speed(speed)
    for i in path:
        calc_and_zoom(turtle_n)
        turtle_n.forward(line_size)

        if i == "r":
            turtle_n.right(90)
        
        if i == "l":
            turtle_n.left(90)


def quad_drag_draw(dragon_iters=10):    

    line_size = round(50)
    path = path_calc(dragon_iters)

    t1 = threading.Thread(target=draw, args=(path, line_size, 0, "black",))
    t2 = threading.Thread(target=draw, args=(path, line_size, 90, "red",))
    t3 = threading.Thread(target=draw, args=(path, line_size, 180, "green",))
    t4 = threading.Thread(target=draw, args=(path, line_size, 270, "blue",))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

def calc_and_zoom(turt:turtle):
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

path = path_calc(dragon_iters=5)
draw(path, 50, speed=0.1)

turtle.mainloop()