from random import randint as r
from random import random as f

unit_id = 0
class Unit():
    def __init__(self,name):
        self.id = unit_id
        unit_id += 1 
        self.name = name
        self.strength = 20
        self.dexterity = 20
        self.constitution = 20
        self.wisdom = 20
        self.charisma = 20
        self.ac = 30
        self.health = 100
        self.alive = True
        self.concious = True
        self.gclass = None
        self.inventory = ['clothes']
        self.wares = []
        self.mainhand = []
        self.belifes = []

    def upkeep(self):
        if not self.concious:
            wake_up = r(1,100)
            if wake_up == 100:
                self.health = 10

    def targeted(self,attacker):
        print(f'{self.name} was targeted by {attacker.name}')

    def attack(self,target):
        target.targeted(self)
        roll = r(1,100)
        if roll >= target.ac:
            if len(self.mainhand) == 0:
                damage = self.strength
            else:
                damage = self.mainhand[0].roll_damage
            target.health -= damage
            if target.health <= 0:
                target.health = 0
                target.concious = False

    def converse(self,target):
        print(f'{self.name} started a convorsation with {target.name} ')

    def trade(self,target):
        if len(target.wares) != 0:
            print(f'{self.name} started a trade with {target.name}')
            print(f'{target.name}: here is what I have for sale {target.wares}')
        else:
            print(f'{target.name} has nothing to trade')

class Rager(Unit):
    def upkeep(self):
        print('temp')

    def start_rage(unit):
        unit.rage_for = 1
        unit.is_raging = True
    
    def end_rage(unit):
        unit.rage_for = 0
        unit.is_raging = False

class Assasin(Unit):
    def attack(self,target):
        roll = r(1,100)
        if roll >= target.ac:
            if len(self.mainhand) == 0:
                damage = self.strength
            else:
                damage = ((r(1,4)+r(1,4)+r(1,4)+r(1,4))*10)+self.mainhand[0].roll_damage
            target.health -= damage
            if target.health <= 0:
                target.health = 0
                target.concious = False

class Bard(Unit):
    def convince(self,belief,target):
        # you can change/give a target (non player) belief
        target.belief.append(belief)
