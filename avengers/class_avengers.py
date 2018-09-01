import time
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
    name, power, intelligence, speed, image = line.strip().split(',')
    cards[name] = [power, intelligence, speed, image]
    screen.register_shape(image)
fhand.close()



class Heroes():
    def __init__(self, name, health, attack, defense, image, x, y):
        self.name = name
        self.hp = health
        self.atk = attack
        self.defense = defense
        self.image = image
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.up()
        self.t.ht()

    def show_me(self):
        pen = self.t
        pen.clear()
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()
        pen.setheading(-90)
        pen.forward(120)
        pen.write("Name: " + self.name, font = style1, align = 'center' )
        pen.forward(25)
        pen.write("HP: " + str(self.hp), font = style1, align = 'center' )
        pen.forward(25)
        pen.write("Attack: " + str(self.atk), font = style1, align = 'center' )
        pen.forward(25)
        pen.write("Defense: " + str(self.defense), font = style1, align = 'center' )


    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_defense(self):
        return self.defense

    def attack(self,dmg,target):
        target.hurt(dmg)
        print("{0} suffered {1} damage".format(target.get_name(),dmg))
        print("{0}'s HP is now {1}".format(target.get_name(),target.get_hp()))
        if target.get_hp() == 0:
            print("{0} has killed {1}!".format(self.name,target.get_name()))
        print("-" * 20)
        
    def normal_attack(self,target):
        dmg = self.atk - target.get_defense()
        print("{0} attacks {1}".format(self.name,target.get_name()))
        self.attack(dmg,target)
        
    def hurt(self, damage):
        self.hp -= damage
        if self.hp <=0:
            self.hp = 0

    def is_dead(self):
        if self.hp > 0:
            return False
        else:
            return True

ironman = Heroes("Ironman",900,50,20,"ironman.gif",-100,100)

hulk = Heroes("Hulk",1000,45,30,"hulk.gif",200,100)

pen = turtle.Turtle()
pen.up()
pen.ht()
pen.goto(50,120)

while True:
    time.sleep(1)
    turn = random.randrange(2)


    if turn == 0:
        ironman.normal_attack(hulk)
        hulk.show_me()
    elif turn == 1:
        hulk.normal_attack(ironman)
        ironman.show_me()
    if ironman.is_dead():
        pen.write("Hulk Wins!", font = style1, align = 'center' )
        break
    elif hulk.is_dead():
        pen.write("Hulk Wins!", font = style1, align = 'center' )
        break
