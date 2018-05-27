import turtle
import random
import time

t = turtle.Pen()
t.speed(0)
t.up()
t.goto(-200,150)

for i in range(21):
    t.write(i)
    t.right(90)
    t.down()
    t.forward(300)
    t.up()
    t.backward(300)
    t.left(90)
    t.forward(20)
t.goto(0,180)


screen = t.getscreen()

cards = dict()
fhand = open('cards.txt')
for line in fhand:
    l = line.strip().split(',')
    print(l)
    cards[l[0]] = [l[1], l[2], l[3]]
    screen.register_shape(l[3])


alice = turtle.Pen()
alice.shape('hulk.gif')
alice.color('red')
alice.up()
alice.goto(-220,100)

ben = turtle.Pen()
ben.shape('captain.gif')
ben.color('blue')
ben.up()
ben.goto(-220,0)

claire = turtle.Pen()
claire.shape('ironman.gif')
claire.color('green')
claire.up()
claire.goto(-220,-100)


max_a = 10
max_b = 10
max_c = 10

terminal = 200
while True:
    time.sleep(0.1)
    alice.forward(random.randrange(max_a))
    ben.forward(random.randrange(max_b))
    claire.forward(random.randrange(max_c))

    if alice.xcor() >= terminal:
        t.write('Winner is Alice!')
        break
    if ben.xcor() >= terminal:
        t.write('Winner is Ben!')
        break
    if claire.xcor() >= terminal:
        t.write('Winner is Claire!')
        break
