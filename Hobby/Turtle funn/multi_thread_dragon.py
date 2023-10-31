from dragon_curve import path_calc
import turtle
from queue import Queue
from threading import Thread, active_count

ITERATIONS = 5
DISTANCE = 2

path = path_calc(ITERATIONS)

que = Queue(3)

def dragon_draw(turtle:turtle.Turtle, init_rotate:int):
    """ads the arguments to draw a dragon cruve into the existing que

    Args:
        turtle (Turtle): a turtle object used for drawing
    """
    que.put(turtle.right(init_rotate))
    for direction in path:
        que.put(turtle.forward(DISTANCE))

        if direction == "l":
            que.put(turtle.left(90))
        if direction == "r":
            que.put(turtle.right(90))

# code coppied from user cdlane posted at: https://stackoverflow.com/questions/19498447/multithreading-with-python-turtle

def process_queue():
    while not que.empty():
        (que.get())(1)

    if active_count() > 1:
        turtle.ontimer(process_queue, 100)

# code coppied from user cdlane posted at: https://stackoverflow.com/questions/19498447/multithreading-with-python-turtle


turtle1 = turtle.Turtle('classic')
turtle1.speed(0)
thread1 = Thread(target=dragon_draw, args=(turtle1, 0))
thread1.daemon = True
thread1.start()

turtle2 = turtle.Turtle()
turtle2.speed(0)
thread2 = Thread(target=dragon_draw, args=(turtle2, 90))
thread2.daemon = True
thread2.start()

turtle3 = turtle.Turtle()
turtle3.speed(0)
thread3 = Thread(target=dragon_draw, args=(turtle3, 180))
thread3.daemon = True
thread3.start()

turtle4 = turtle.Turtle()
turtle4.speed(0)
thread4 = Thread(target=dragon_draw, args=(turtle4, 270))
thread4.daemon = True
thread4.start()

process_queue()

turtle.exitonclick()