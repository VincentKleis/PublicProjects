# code coppied from user cdlane posted at: https://stackoverflow.com/questions/19498447/multithreading-with-python-turtle

import queue
import threading
import turtle

def tes1():
    while range(360):
        graphics.put(turtle1.forward)
        graphics.put(turtle1.left)

def tes2():
    while range(360):
        graphics.put(turtle2.forward)
        graphics.put(turtle2.right)

graphics = queue.Queue(1)  # size = number of hardware threads you have - 1

turtle1 = turtle.Turtle('turtle')
turtle1.speed(0)
thread1 = threading.Thread(target=tes1)
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()

turtle2 = turtle.Turtle('turtle')
turtle2.speed(0)
thread2 = threading.Thread(target=tes2)
thread2.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread2.start()

while not graphics.empty():
    (graphics.get())(1)

turtle.exitonclick()