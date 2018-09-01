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
    def __init__(self, name, health, attack, defense, skills = []):
        self.name = name
        self.hp = health
        self.atk = attack
        self.defense = defense
        self.skills = skills

    def show_me(self):
        print("Name: ", self.name)
        print("Health: ", self.hp)
        print("HP: ",self.hp)
        print("Attack: ",self.atk)
        print("Defense: ",self.defense)
        for i in self.skills:
            print("Skill: {0} , Damage {1}".format(i["name"],i["damage"]))
        print("-"*20)

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
        
    def skill_attack(self,skill_num,target):
        skill = self.skills[skill_num]
        dmg = skill["damage"] - target.get_defense()
        print("{0} used {1} againse {2}".format(self.name, skill["name"],target.get_name()))
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

ironman_skill = [{"name":"Iron Punch","damage":200},{"name":"Laser Beam","damage":400}]
ironman = Heroes("Ironman",900,50,20,ironman_skill)

hulk_skill = [{"name":"Squat","damage":180},{"name":"Hulk Punch","damage":450}]
hulk = Heroes("Hulk",1000,45,30,hulk_skill)



while True:
    time.sleep(1)
    turn = random.randrange(6)
    ironman.show_me()
    hulk.show_me()
    if turn == 0:
        ironman.normal_attack(hulk)
    elif turn == 1:
        hulk.normal_attack(ironman)
    elif turn == 2:
        ironman.skill_attack(0,hulk)
    elif turn == 3:
        ironman.skill_attack(1,hulk)
    elif turn == 4:
        hulk.skill_attack(0,ironman)
    elif turn == 5:
        hulk.skill_attack(1,ironman)
    if ironman.is_dead() or hulk.is_dead():
        print("Game Over")
        break
