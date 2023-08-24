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
        self.leadership_type = 0
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
ppl = []
for i in range(100):
    ppl.append(Citizen(i))
num_of_ppl = 0
while num_of_ppl < 100:
    city = r.randint(0,4)
    cities[city].add_citizen(ppl[num_of_ppl])
    num_of_ppl += 1

man_r = len(man.residents)
counter = 0
while counter < man_r:
    print(man.residents[counter].id)
    counter += 1
#for i in man.residents:
#    print(man.residents[1])