import turtle
from q1 import check_time, counter
import random
import threading
def func(x):
    a = x**3-6
    b = 2-x**2
    return a/b
def point(t:turtle.Turtle, x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(5)
def paint(t):
    while True:
        x = random.randint(-500,500)
        y = func(x)
        point(t,x,y)



if __name__ == '__main__':
    s = turtle.getscreen()
    t = turtle.Turtle()
    t.hideturtle()
    paint(t)
    # threads = [] #turtle dont work in threads
    # for _ in range(1):
    #     a = threading.Thread(target=paint, args=(t,))
    #     threads.append(a)
    #     a.start()
    #     t = turtle.Turtle()
    #     t.hideturtle()
    # for i in threads:
    #     i.join()
