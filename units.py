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

    def unarmed_attack(self,target):
        roll = r(1,100)
        if roll >= target.ac:
            target.health -= self.strength
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

    