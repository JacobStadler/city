from random import randint as r
from random import random as f
from class_city import City
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
        self.known_languages = r(1,3)
        self.parents = []
        self.gestation_days = 90
        self.preg_for = 0
        self.is_preg = [False,None]
        self.alive = True
        # prefrences
        # trade, gender roles, event, religion, authority, caste, language, food, art, music
        #   votes = [[0,0,0,0],[0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.pref = [[f,f,f,f],[f,f,f],[f,f,f],[f,f,f,f],[f,f,f],[f,f,f,f],[f,f,f,f,f],[f,f,f],[f,f,f,f,f,f,f],[f,f,f,f,f,f],[f,f,f,f,f,f,f]]
        # I cannot figure out how to do this  with logic so
        # for now I am leaving it logic-less because anything else sounds like an even worse headache
        # TODO: re add resouce prefrence in some manner
        # resource
        
        #self.trade_pref = r(0,3)
        #self.genderroles_pref = r(0,2)
        #self.event_pref = r(0,2)
        #self.religion_pref = r(0,3)
        #self.authority_pref = [r(0,2),r(0,3)]
        #self.caste_pref = r(0,4)
        #self.language_pref = r(0,2)
        #self.food_pref = r(0,6)
        #self.art_pref = r(0,5)
        #self.music_pref = r(0,6)
        #self.resource_pref = r(0,7)
    def add_occupance(self,city):
        self.occupy = city
    def move(self):
        self.like_current = self.like(self.occupy)
    def old_like(self,city):
        # still need to make thier likes more variable which will help with the current dislike problems I think
        # each civ should have a like/dislike % for each thing instead of a yes no one just one this should be easy using a list
        total = 11
        metch = 0
        if self.trade_pref == city.trade:
            metch += 1
        if self.genderroles_pref == city.genderroles:
            metch += 1
        if self.event_pref == city.event:
            metch += 1
        if self.religion_pref == city.religion:
            metch += 1
        if self.authority_pref == city.authority:
            metch += 1
        if self.caste_pref == city.caste:
            metch += 1
        if self.language_pref == city.language:
            metch += 1
        if self.food_pref == city.food:
            metch += 1
        if self.art_pref == city.art:
            metch += 1
        if self.music_pref == city.music:
            metch += 1
        if self.resource_pref == city.resource:
            metch += 1
        #print(f"metch: {metch}/{total} {self.id} {round(metch/total,2)*100}")
        return round(metch/total,2)*100
    def like(self,city):
        max = 11
        like_num = 0
        like_num += self.pref[0][city.trade]
        like_num += self.pref[1][city.genderroles]
        like_num += self.pref[2][city.event]
        like_num += self.pref[3][city.religion]
        like_num += self.pref[4][city.authority]
        like_num += self.pref[5][city.caste]
        like_num += self.pref[6][city.language]
        like_num += self.pref[7][city.food]
        like_num += self.pref[8][city.art]
        like_num += self.pref[9][city.music]
        like_num += self.pref[10][city.resource]
        return round(like_num/max,2)*100
    def vacation(self):
        neighbors = self.occupy.neighbors
        vacation_areas = [neighbors[0]]
        self.like(vacation_areas[0][0])
    def found_city(self,cities):
        came_from = self.occupy
        city_id = len(cities)-1
        cities.append(City(city_id))
        came_from.nond_n += cities[city_id]
        self.occupy = cities[city_id]
        cities[city_id].nond_n += came_from
        cities[city_id].add_citizen(self)
        cities[city_id].founder = self
        cities[city_id].initiate_pref()
    def try_for_kid(self,civs,partner):
        if not self.is_preg[0]:
            if f*10 > 7:
                if self.can_have_babies:
                    self.is_preg = [True,partner]
        else:
            self.preg_for += 1
            if self.preg_for >= self.gestation_days:
                if f*10 > 6 or self.gestation_days >= 100:
                    bb_id = len(civs)
                    civs.append(Citizen(bb_id))
                    civs[bb_id].parents.append(self,self.is_preg[1])
                    civs[bb_id].occupy = self.occupy
                    civs[bb_id].occupy.add_citizen[civs[bb_id]]

    def age(self,days):
        self.age_days += 1
        if self.age_days > days:
            self.age_years += 1
            self.age_days = 0
        die = r(0,100)
        if die < self.age_years:
            die = r(0,100)
            if die < self.age_years:
                # temporary stop to prevent bugs
                if not self.is_preg:
                    self.alive = False
            
