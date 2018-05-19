import random
import turtle
t = turtle.Turtle()
t.up()
t.ht()
screen = t.getscreen()
style1 = ('Arial', 14, 'bold')
style2 = ('Arial', 20, 'bold')


cards = dict()
fhand = open('cards.txt')
for line in fhand:
    name, power, intelligence, image = line.strip().split(',')
    cards[name] = [power, intelligence, image]
    screen.register_shape(image)
fhand.close()


def choose_card(card, cards, pen, xcor, ycor):
    if card == 'random':
        card = random.choice(list(cards.keys()))
    if card in cards:
        stats = cards[card]
        pen.goto(xcor,ycor)
        pen.shape(stats[2])
        pen.stamp()
        pen.setheading(-90)
        pen.forward(120)
        pen.write("Name: " + card, font = style1, align = 'center' )
        pen.forward(25)
        pen.write("Power: " + stats[0], font = style1, align = 'center' )
        pen.forward(25)
        pen.write("Intelligence: " + stats[1], font = style1, align = 'center' )
        score = int(stats[0]) + int(stats[1])
    return score


while True:
    player_1 = input("Player 1 : ")
    player_2 = input("Player 2 : ")
    t.clear()
    s1 = choose_card(player_1, cards, t, -100, 100)
    t.goto(50,50)
    t.write("VS.", font = style2, align = 'center')
    s2 = choose_card(player_2, cards, t, 200, 100)

    t.goto(50,150)
    t.color('red')
    if s1>s2:
        t.write("Player 1 WIN !", font = style2, align = 'center')
    elif s1<s2:
        t.write("Player 2 WIN !", font = style2, align = 'center')
    else:
        t.write("DRAW !", font = style2, align = 'center')
        
