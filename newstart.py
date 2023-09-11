from random import randint as r
from random import random as f
from random import choices as choices
from opensimplex import OpenSimplex

class Map():
    def __init__(self,size):
        ahx = r(1,10) # alter height x
        ahy = r(1,10) # alter height y
        atx = r(1,10) # alter tempature x
        aty = r(1,10) # alter tempature y
        self.size = size
        self.height_map = []
        self.tempature_map = []
        height = OpenSimplex(1)
        tempature = OpenSimplex(2)                                                            
        max_num = .8
        min_num = -.8
        for i in range(size):
            self.height_map.append([])
            self.tempature_map.append([])
            for j in range(size):
                # is now normalized between 0 and 1
                self.height_map[i].append((height.noise2(x=i+ahx,y=j+ahy)-min_num)/(max_num-min_num))
                self.tempature_map[i].append((tempature.noise2(x=i+atx,y=j+aty)-min_num)/(max_num-min_num))
        # TODO: add seasons or variability through the year 
    def display(self):
        for i in range(self.size):
            print(self.height_map[i])
        print('')
        for i in range(self.size):
            print(self.tempature_map[i])

    def mine_resources(self,x,y):
        # 0  = deep sea      9 =
        # 1  = sea          10 =
        # 2  = beach        11 = 
        # 3  = river        12 = rolling hills
        # 4  =              13 = hills
        # 5  =              14 = mountain base
        # 6  =              15 = mountains slopes
        # 7  =              16 = Mountain Tops
        # 8  = plains
        height = self.height_map[x][y]
        if height >= .3:
            if height >= .3 and height <= .4:
                #weights = [1]
                #selected = 'sandstone'
                return 'sandstone'
            if height > .4 and height <= .6:
                selected = ['anystone','ore','gems']
                weights = [.6,.3, .1]
            if height > .6 and height <= .8:
                selected = ['anystone','ore','gems']
                weights = [.4,.4,.2]
            if height > .8:
                selected = ['marble','ore','gems']
                weights = [.2,.4,.4]
            chosen = choices(selected,weights,k=1)
            if chosen[0] == 'anystone':
                selected = ['granite','slate','limestone','sandstone']
                weights = [.25,.25,.25,.25]
                chosen = choices(selected,weights,k=1)
            if chosen[0] == 'ore':
                selected = ['iron','coal','copper','gold']
                weights = [.25,.25,.25,.25]
                chosen = choices(selected,weights,k=1)
            if chosen[0] == 'gems':
                selected = ['saphire','ruby','diamond','quartz']
                weights = [.25,.25,.25,.25]
                chosen = choices(selected,weights,k=1)

            return Good(chosen[0]).name
        else:
            return 'Not mineable'
        # stone = [granite,marble,slate,limestone,sandstone,iron/coal,gems]
        # when mine there is a percent chance you mine one of a couple of things based on elevation.
        # 0-2   None
        # 3-4   100 Sandstone/Sand
        # 5-8   60% any stone 30% iron/coal 10% gems
        # 9-13  40% any stone 40% iron/coal 20% gems
        # 14-16 20% marble 40% iron 40% gems 



class Person():
    def __init__(self,name):
        self.name = name
        self.job = None
        self.parents = []
        self.children = []
        self.gender = r(0,1)
        # trade, gender roles, event, religion, authority, caste, language, food, art, music
        self.culture_pref = [[f(),f(),f(),f()],[f(),f(),f()],[f(),f(),f()],[f(),f(),f(),f()],[f(),f(),f()],[f(),f(),f(),f()],[f(),f(),f(),f(),f()],[f(),f(),f()],[f(),f(),f(),f(),f(),f(),f()],[f(),f(),f(),f(),f(),f()],[f(),f(),f(),f(),f(),f(),f()]]

    def culture_match(self,city):
        max = 11
        matches = 0
        for i in range(len(city.culture)):
            matches += self.culture_pref[i][city.culture[i]]
        return round(matches/max,2)*100

class City():
    def __init__(self,name):
        self.name = name
        self.population = 0
        self.citizens = []
        self.neighbors = []
        self.founder = None
        self.culture = []
        self.jobs = []
        self.resource = None

    def add_citizen(self,civ):
        self.citizens.append(civ)
        self.population += 1
    
    def rem_citizen(self,civ):
        for i in range(self.citizens):
            if self.citizens[i].name == civ.name:
                self.citizens.pop(i)
                break
        self.population -= 1

    def add_good(self,good):
        print('good job!')

    
class Good():
    def __init__(self,name):
        self.name = name
        self.value = 0

class Resource():
    def __init__(self,name):
        self.name = name
        self.jobs = None

    def jobs(self):
        print('temp')

    def retrive_resource(self,city):
        city.resource.append(self.good)


# jobs = Herder, Trader, Fisher, Miner, Hunter, Logger
# more gems at higher altatude
class Job():
    def __init__(self,name):
        self.name = name

grand_size = 100
souper = Map(grand_size)
souper.display()
print(souper.mine_resources(r(0,grand_size-1),r(0,grand_size-1)))