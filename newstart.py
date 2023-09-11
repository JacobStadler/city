from random import randint as r
from random import random as f
from opensimplex import OpenSimplex

class Map():
    def __init__(self,size):
        map = []
        tmp = OpenSimplex()
        for i in size:
            map.append([])
            for j in size:
                map[i].append(tmp.noise2d(x=i,y=j)) 

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

class Resource():
    def __init__(self,name):
        self.name = name
        self.jobs = None

    def jobs(self):
        print('temp')

    def retrive_resource(self,city):
        city.resource.append(self.good)


# jobs = Herder, Trader, Fisher, Miner, Hunter, 
# more gems at higher altatude
class Job():
    def __init__(self,name):
        self.name = name