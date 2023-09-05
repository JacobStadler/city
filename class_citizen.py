from random import randint as r
from random import random as f
from class_city import City
import time
class Citizen():
    def __init__(self,id):
        self.id = id
        # information
        self.age_days = 0
        self.age_years = 0 
        self.occupy = None
        self.verted = r(0,1)
        # currently no enbys but for now that is ok because we are testing
        self.gender = r(0,1)
        if self.gender == 1:
            self.can_have_babies = True
        else:
            self.can_have_babies = False
        self.known_languages = r(1,3)
        self.parents = []
        self.children = []
        self.gestation_days = 365
        self.preg_for = 0
        self.is_preg = [False,None]
        self.is_banned = False
        self.alive = True
        self.had_kid = False
        self.year_day_died = [0,0]
        self.like_current = 0
        # prefrences
        # trade, gender roles, event, religion, authority, caste, language, food, art, music
        #   votes = [[0,0,0,0],[0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.pref = [[f(),f(),f(),f()],[f(),f(),f()],[f(),f(),f()],[f(),f(),f(),f()],[f(),f(),f()],[f(),f(),f(),f()],[f(),f(),f(),f(),f()],[f(),f(),f()],[f(),f(),f(),f(),f(),f(),f()],[f(),f(),f(),f(),f(),f()],[f(),f(),f(),f(),f(),f(),f()]]
        # I cannot figure out how to do this  with logic so
        # for now I am leaving it logic-less because anything else sounds like an even worse headache
        # TODO: re add resouce prefrence in some manner

    def add_occupance(self,city):
        self.occupy = city

    def consider_move(self,city):
        options = self.occupy.nond_n
        
        if self.like_current < self.like(city):
            self.occupy = city
            self.like_current = self.like(city)

    
    def like(self,city):
        max = 11
        like_num = 0
        for i in range(len(city.pref)):
            like_num += self.pref[i][city.pref[i]]
        return round(like_num/max,2)*100
    
    def vacation(self):
        neighbors = self.occupy.neighbors
        vacation_areas = [neighbors[0]]
        self.like(vacation_areas[0][0])

    def found_city(self,cities):
        #TODO: add it as a node on the map need some way to determine how far they will travel
        came_from = self.occupy
        city_id = len(cities)
        cities.append(City(city_id))
        came_from.nond_n.append(cities[city_id])
        self.occupy = cities[city_id]
        self.like_current = self.like(self.occupy)
        cities[city_id].nond_n.append(came_from)
        cities[city_id].add_citizen(self)
        cities[city_id].founder = self
        cities[city_id].initiate_pref()

    def try_for_kid(self,civs,partner):
        if self.is_preg[0] == False:
            if f()*10 > 7:
                if self.can_have_babies:
                    self.is_preg = [True,partner]
                    partner.is_banned = True
                    
        else:
            if self.preg_for >= self.gestation_days:
                if f()*10 > 6 or self.gestation_days >= 400:
                    self.had_kid = True
                    bb_id = len(civs)
                    civs.append(Citizen(bb_id))
                    self.children.append(civs[bb_id])
                    self.is_preg[1].children.append(civs[bb_id])
                    civs[bb_id].parents = [self,self.is_preg[1]]
                    civs[bb_id].occupy = self.occupy
                    civs[bb_id].occupy.add_citizen(civs[bb_id])
            self.preg_for += 1


    def find_partner(self,civs):
        if self.is_preg[0] == False and self.is_banned == False:
            avalable = self.occupy.residents
            choices = []
            for i in range(len(avalable)):
                #print(f'{i} | av : id {avalable[i].id} gen {avalable[i].gender} sf : id {self.id} gen {self.gender} | {avalable[i].is_preg[0]}')
                if avalable[i].gender != self.gender and avalable[i].is_preg[0] == False:
                    choices.append(avalable[i])
                    #print('added')
                    #time.sleep(1)
            if choices:
                choice = r(0,len(choices)-1)
                if self.can_have_babies:
                    self.try_for_kid(civs,avalable[choice])
                else:
                    avalable[choice].try_for_kid(civs,self)

    def age(self,days,y,d):
        ten_d = 0
        i = 0
        while i < self.age_years:
            chance = r(0,500000)
            if chance == 500000:
                ten_d += 1
            i += 1

        if ten_d >= 1:
            if not self.is_preg[0]:
                self.alive = False
                self.year_day_died = [y,d]
                return False
            
        self.age_days += 1
        if self.age_days > days:
            self.age_years += 1
            self.age_days = 0
            
