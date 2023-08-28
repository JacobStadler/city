import random as r
class Citizen():
    def __init__(self,id):
        self.id = id
        # information
        self.occupy = None
        self.verted = r.randint(0,1)
        self.gender = r.randint(0,2)
        self.known_languages = r.randint(1,3)
        # prefrences
        self.trade_pref = r.randint(0,3)
        self.genderroles_pref = r.randint(0,2)
        self.event_pref = r.randint(0,2)
        self.religion_pref = r.randint(0,3)
        self.authority_pref = [r.randint(0,2),r.randint(0,3)]
        self.caste_pref = r.randint(0,4)
        self.language_pref = r.randint(0,2)
        self.food_pref = r.randint(0,6)
        self.art_pref = r.randint(0,5)
        self.music_pref = r.randint(0,6)
        self.resource_pref = r.randint(0,7)
    def add_occupance(self,city):
        self.occupy = city
    def move(self):
        self.like_current = self.like(self.occupy)
    def like(self,city):
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