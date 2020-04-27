import turtle
import time
my_turtle = turtle.Turtle()
my_turtle.speed(90)

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

time.sleep(5)
for i in range(100):
    square(100,90)
    my_turtle.right(13)

time.sleep(5)