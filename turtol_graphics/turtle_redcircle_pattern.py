import turtle, time
my_turtle = turtle.Turtle()
my_turtle.speed(20)
cl = ["red"]

def draw (d,angle,x,y):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.down()
    time.sleep(10)
    for i in range(1,610):
        my_turtle.pencolor(cl[0])
        my_turtle.forward(d)
        my_turtle.left(angle)
        d = d-1

draw(150,98,-50,-50)

time.sleep(10)