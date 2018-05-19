
import turtle
t = turtle.Turtle()
t.up()
t.ht()
screen = t.getscreen()

cards = dict()
fhand = open('cards.txt')
for line in fhand:
    name, power, intelligence, image = line.strip().split(',')
    cards[name] = [power, intelligence, image]
    screen.register_shape(image)
fhand.close()
print(cards)
print(screen.getshapes())

print('---------')
while True:
    card = input('Choose a card')
    t.clear()
    if card in cards:
        style = ('Arial', 14, 'bold')
        t.goto(-100,200)
        t.shape(cards[card][2])
        t.stamp()
        t.setheading(-90)
        t.forward(120)
        t.write("Name: " + card, font = style, align = 'center' )
        t.forward(25)
        t.write("Power: " + cards[card][0], font = style, align = 'center' )
        t.forward(25)
        t.write("Intelligence: " + cards[card][1], font = style, align = 'center' )
