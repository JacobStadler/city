import random as r
#import time as t

#ts = t.time()
#print(ts)

Caste = ['All equal', 'Strong Lead', 'Born Into', 'Employment', 'Skill']
Religion = ['No one major religion', 'Monothieistic', 'Polythieistic', 'Atheistic']
Language = ['Abundance of language', 'One major language', 'A couple major languages']
Languages = ['FirtLang','SecLang','ThiLang','FifLang','SixLang','SevLeng','EigLang','NinLang','TenLeng']
Food = ['Focus on spices', 'Focus on herbs', 'Focus on sweetness', 'Focus on savory', 'Focus on unseasoned', 'Mixed food focus', 'All focuses']
Art = ['Focus on abstract', 'Focus on realism', 'Focus on realism', 'Focus on impressionism', 'No real focus', 'Sporatic focus']

Music = ['String focus', 'Woodwind focus', 'Percussion focus', 'Brass focus', 'Mixed focus', 'No focus', 'Wide focus']
Resource = ['Inland-water', 'Ocean', 'Farmland', 'Lumber', 'Quarry[stone]', 'Mine[ores/gems]', 'Finished Goods', 'Exotics']

Gender = ['Male','Female','Non-Binary']

GenderRolls = ['Equal', 'Patriacle', 'Matriachal']
Trade = ['Abundance', 'Some', 'Very little', 'None']
Events = ['Events through the year','A few major events','No major events']

Verted = ['Introverted','Extroverted'] # the idea is this will affect thier likyhood to like cities with more events

Authority = ['No major authority', 'Single ruler', 'Council', 'Single ruler with council', 'Elected single ruler', 'Elected council', 'Elected single ruler and council']
Authority0 = ['Elected','No major authority','Inherited']
# if Authority0 is 0 or 2 then also need to select from Authority1
Authority1 = ['Single ruler','Single ruler with inherited council','Single ruler with elected council','Council']


class City():
    def __init__(self,name):
        self.name = name
        self.population = 0
        self.residents = []
        self.neighbors = []
        # prefrences
        self.trade = r.randint(0,3)
        self.genderroles = r.randint(0,2)
        self.event = r.randint(0,2)
        self.religion = r.randint(0,3)
        self.authority = [r.randint(0,2),r.randint(0,3)]
        self.caste = r.randint(0,4)
        self.language = r.randint(0,2)
        self.food = r.randint(0,6)
        self.art = r.randint(0,5)
        self.music = r.randint(0,6)
        self.resource= r.randint(0,7)
    def add_citizen(self,civ):
        self.residents.append(civ)
        self.population += 1
    def rem_citizen(self,civ):
        i = 0
        while i < len(self.residents):
            if self.residents[i].id == civ.id:
                #print(f'removed {self.residents[i].id}  | intended : {civ.id}')
                self.residents.pop(i)
                break
            i += 1
        self.population -= 1
    def add_neighbor(self,insert):
        self.neighbors.append(insert)


# my basic idea is that each citizen has a opinion on each of these from 0-1 0 being strong dislike and 1 being strong like.
# basically I will call a routine that will cause them to move if they view another city as more likeable
# some citizens may also prefer lower or higher populace cities

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
        #print(round(metch/total,2))
        return round(metch/total,2)*100

tom = City('tom')
randy = City('randy')
brad = City('brad')
joel = City('joel')
man = City('man')

# t --- r
# | \ / |
# |  m  |
# | / \ |
# b --- j
cities = [tom,randy,brad,joel,man]
tom.add_neighbor(randy)
tom.add_neighbor(brad)
tom.add_neighbor(man)
randy.add_neighbor(tom)
randy.add_neighbor(joel)
randy.add_neighbor(man)
brad.add_neighbor(tom)
brad.add_neighbor(joel)
brad.add_neighbor(man)
joel.add_neighbor(brad)
joel.add_neighbor(randy)
joel.add_neighbor(man)
man.add_neighbor(tom)
man.add_neighbor(randy)
man.add_neighbor(joel)
man.add_neighbor(brad)

total_amount_of_cities = 10
tcities = []
for i in range(total_amount_of_cities):
    tcities.append(City(i))

def neighbors():
    # this is for randomally asigning neighbors but neighbor relations have to be mutual like:
    random_city_one = r.randint(0,total_amount_of_cities)
    random_city_two = r.randint(0,total_amount_of_cities)
    tcities[random_city_one].add_neighbor(tcities[random_city_two])
    tcities[random_city_two].add_neighbor(tcities[random_city_one])
    print("temp")

total_amount_of_people = 1000
ppl = []
for i in range(total_amount_of_people):
    ppl.append(Citizen(i))
num_of_ppl = 0
while num_of_ppl < total_amount_of_people:
    city = r.randint(0,4)
    cities[city].add_citizen(ppl[num_of_ppl])
    ppl[num_of_ppl].occupy = cities[city]
    num_of_ppl += 1

"""man_r = len(man.residents)
counter = 0
while counter < man_r:
    print(man.residents[counter].id)
    counter += 1"""
#occ = ppl[1].occupy
#print(occ.name)
#print(ppl[1].like(occ))

cycles = 3
while cycles > 0:
    moves = 0
    civs = total_amount_of_people
    while civs > 0:
        pers = ppl[civs-1]
        civ_like_store = []
        civ_like_score = []
        civ_city = pers.occupy
        #print(f'{pers.id} lives in {civ_city.name}')
        civ_like_store.append(pers.occupy)
        civ_like_score.append(pers.like(pers.occupy))
        highest_like = 0
        civ_city_n = len(civ_city.neighbors)
        i = 0
        while i < civ_city_n:
            civ_like_store.append(civ_city.neighbors[i])
            civ_like_score.append(pers.like(civ_city.neighbors[i]))
            if civ_like_score[i] > civ_like_score[highest_like]:
                highest_like = i
            i += 1
        if highest_like != 0:
            moves += 1
            print(f'{pers.id} moved from {civ_city.name} to {civ_city.neighbors[highest_like-1].name}')
            civ_city.rem_citizen(pers)
            civ_city.neighbors[highest_like-1].add_citizen(pers)
            pers.add_occupance(civ_city.neighbors[highest_like-1])
            #print(f'{pers.occupy.name}')
        civs -= 1
    print(f'\nmoves : {moves}\n')
    cycles -= 1

def city_info(c):
    i = 0
    total_aproval = 0
    while i < len(c.residents):
        total_aproval += c.residents[i].like(c)
        i += 1
    print(f'''
    City :          {c.name}
    Avg Approval :  {round(total_aproval/c.population,2)}
    Pop:            {c.population}
    Auth:           {Authority0[c.authority[0]]} {Authority1[c.authority[1]]}
    Trade:          {Trade[c.trade]}
    Gender Roles:   {GenderRolls[c.genderroles]}
    Events :        {Events[c.event]}
    Religion :      {Religion[c.religion]}
    Caste :         {Caste[c.caste]}
    Language :      {Language[c.language]}
    Food :          {Food[c.food]}
    Art:            {Art[c.art]}
    Music :         {Music[c.music]}
    Resource :      {Resource[c.resource]}
        ''')

city_info(tom)
city_info(randy)
city_info(joel)
city_info(brad)
city_info(man)