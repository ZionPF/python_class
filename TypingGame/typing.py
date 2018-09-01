import turtle
import time

t1 = turtle.Turtle()
t1.setheading(-90)
t1.ht()
t1.up()
t1.goto(0,200)

t2 = turtle.Turtle()
t2.goto(0,-200)

def a():
    t2.clear()
    t2.write("a")
    return "a"

def b():
    t2.clear()
    t2.write("b")
    return "b"

def c():
    t2.clear()
    t2.write("c")
    return "c"

screen = turtle.getscreen()
screen.onkey(a, "a")
screen.onkey(b, "b")

screen.onkey(c, "c")



while True:
    screen.listen()
    t1.write("permanent", font=("Arial", 20, "normal"), align="center")

    time.sleep(0.1)
    t1.clear()

    t1.fd(1)

    
