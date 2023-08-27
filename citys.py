import random as r
import graphviz as gv
dot = gv.Digraph('Cities')
#G = gv.AGraph()
#dot.graph_attr.update(size="10,10")
Caste = ['All equal', 'Strong Lead', 'Born Into', 'Employment', 'Skill']
Religion = ['No one major religion', 'Monothieistic', 'Polythieistic', 'Atheistic']
Language = ['Abundance of language', 'One major language', 'A couple major languages']
Languages = ['FirtLang','SecLang','ThiLang','FifLang','SixLang','SevLeng','EigLang','NinLang','TenLeng']
Food = ['Focus on spices', 'Focus on herbs', 'Focus on sweetness', 'Focus on savory', 'Focus on unseasoned', 'Mixed food focus', 'All focuses']
Art = ['Focus on abstract', 'Focus on realism', 'Focus on realism', 'Focus on impressionism', 'No real focus', 'Sporatic focus']
Music = ['String focus', 'Woodwind focus', 'Percussion focus', 'Brass focus', 'Mixed focus', 'No focus', 'Wide focus']
Resource = ['Inland-water', 'Ocean', 'Farmland', 'Lumber', 'Quarry[stone]', 'Mine[ores/gems]', 'Finished Goods', 'Exotics']
Gender = ['Male','Female','Non-Binary']
GenderRolls = ['Equal', 'Patriarchal', 'Matriarchal']
Trade = ['Abundance', 'Some', 'Very little', 'None']
Events = ['Events through the year','A few major events','No major events']
Verted = ['Introverted','Extroverted'] 
# the idea is this will affect thier likyhood to like cities with more events
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
                self.residents.pop(i)
                break
            i += 1
        self.population -= 1
    def add_neighbor(self,insert):
        self.neighbors.append(insert)
    def poll_residence(self):
        cat = ["Trade","Gender Roles","Event","Religion","Authority0","Authority1","Caste","Language","Food","Art","Music","Resource"]
        cr_slt = [self.trade,self.genderroles,self.event,self.religion,self.authority[0],self.authority[1],self.caste,self.language,self.food,self.art,self.music,self.resource]
        votes = [[0,0,0,0],[0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        for i in range(len(self.residents)):
            votes[0][self.residents[i].trade_pref] += 1
            votes[1][self.residents[i].genderroles_pref] += 1
            votes[2][self.residents[i].event_pref] += 1
            votes[3][self.residents[i].religion_pref] += 1
            votes[4][self.residents[i].authority_pref[0]] += 1
            votes[5][self.residents[i].authority_pref[1]] += 1
            votes[6][self.residents[i].caste_pref] += 1
            votes[7][self.residents[i].language_pref] += 1
            votes[8][self.residents[i].food_pref] += 1
            votes[9][self.residents[i].art_pref] += 1
            votes[10][self.residents[i].music_pref] += 1
            votes[11][self.residents[i].resource_pref] += 1

        biggest_dif = [0,0]
        diff = ''
        for i in range(len(votes)):
            for j in range(len(votes[i])):
                if j != cr_slt[i]:
                    if votes[i][j] > votes[i][cr_slt[i]]:
                        t_dif = votes[i][j] - votes[i][cr_slt[i]]
                        if t_dif > biggest_dif[1]:
                            diff = 'changed '
                            biggest_dif = [i,j]

        """for i in range(len(votes)):
            for j in range(len(votes[i])):
                if votes[i][j] > most_votes:
                    most_votes = votes[i][j]
                    voted_to_change = [i,j]"""
        voted_to_change = biggest_dif
        print_string = f"{diff}Residents of {self.name} voted to change {cat[voted_to_change[0]]} from "
        #print(f'Residents of {self.name} voted to change {cat[voted_to_change[0]]} from {self.}')
        if diff != '':
            match voted_to_change[0]:
                case 0:
                    print_string += f"{Trade[self.trade]} to {Trade[voted_to_change[1]]}"
                    self.trade = voted_to_change[1]
                case 1:
                    print_string += f"{GenderRolls[self.genderroles]} to {GenderRolls[voted_to_change[1]]}"
                    self.genderroles = voted_to_change[1]
                case 2:
                    print_string += f"{Events[self.event]} to {Events[voted_to_change[1]]}"
                    self.event = voted_to_change[1]
                case 3:
                    print_string += f"{Religion[self.religion]} to {Religion[voted_to_change[1]]}"
                    self.religion = voted_to_change[1]
                case 4:
                    print_string += f"{Authority0[self.authority[0]]} to {Authority0[voted_to_change[1]]}"
                    self.authority[0] = voted_to_change[1]
                case 5:
                    print_string += f"{Authority1[self.authority[1]]} to {Authority1[voted_to_change[1]]}"
                    self.authority[1] = voted_to_change[1]
                case 6:
                    print_string += f"{Caste[self.caste]} to {Caste[voted_to_change[1]]}"
                    self.caste = voted_to_change[1]
                case 7:
                    print_string += f"{Language[self.language]} to {Language[voted_to_change[1]]}"
                    self.language = voted_to_change[1]
                case 8:
                    print_string += f"{Food[self.food]} to {Food[voted_to_change[1]]}"
                    self.food = voted_to_change[1]
                case 9:
                    print_string += f"{Art[self.art]} to {Art[voted_to_change[1]]}"
                    self.art = voted_to_change[1]
                case 10:
                    print_string += f"{Music[self.music]} to {Music[voted_to_change[1]]}"
                    self.music = voted_to_change[1]
                case 11:
                    print_string += f"{Resource[self.resource]} to {Resource[voted_to_change[1]]}"
                    self.resource = voted_to_change[1]
            print(print_string)

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
        #print(f"metch: {metch}/{total} {self.id} {round(metch/total,2)*100}")
        return round(metch/total,2)*100

total_amount_of_cities = 20
cities = []
for i in range(total_amount_of_cities):
    cities.append(City(i))
    dot.node(f'{i}',shape="square")

city_neighbors = 5
def neighbors(city):
    added_n = 0
    while added_n < city_neighbors:
        random_city = r.randint(0,total_amount_of_cities-1)
        #print(f'{cities[random_city]} {city.neighbors}' )
        if cities[random_city] not in city.neighbors and cities[random_city] != city:
            city.add_neighbor(cities[random_city])
            dot.edge(f'{cities[random_city].name}',f'{city.name}',dir='both')
            cities[random_city].add_neighbor(city)
            added_n += 1

for i in range(total_amount_of_cities):
    neighbors(cities[i])

total_amount_of_people = 2000
ppl = []
for i in range(total_amount_of_people):
    ppl.append(Citizen(i))

num_of_ppl = 0
while num_of_ppl < total_amount_of_people:
    city = r.randint(0,total_amount_of_cities-1)
    cities[city].add_citizen(ppl[num_of_ppl])
    ppl[num_of_ppl].occupy = cities[city]
    num_of_ppl += 1

cycles = 10
while cycles > 0:
    moves = 0
    civs = total_amount_of_people
    while civs > 0:
        pers = ppl[civs-1]
        civ_like_store = []
        civ_like_score = []
        civ_city = pers.occupy
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
            #print(f'{pers.id} moved from {civ_city.name} to {civ_city.neighbors[highest_like-1].name}')
            civ_city.rem_citizen(pers)
            civ_city.neighbors[highest_like-1].add_citizen(pers)
            pers.add_occupance(civ_city.neighbors[highest_like-1])
        civs -= 1
    print(f'\nmoves : {moves}\n')
    for i in range(total_amount_of_cities):
        cities[i].poll_residence()
    cycles -= 1

def city_info(c):
    i = 0
    total_aproval = 0
    while i < len(c.residents):
        total_aproval += c.residents[i].like(c)
        i += 1
    string = f'''
    City :          {c.name}\l
    Avg Approval :  {round(total_aproval/len(c.residents),2)}\l
    Pop:            {c.population}\l
    Auth:           {Authority0[c.authority[0]]} {Authority1[c.authority[1]]}\l
    Trade:          {Trade[c.trade]}\l
    Gender Roles:   {GenderRolls[c.genderroles]}\l
    Events :        {Events[c.event]}\l
    Religion :      {Religion[c.religion]}\l
    Caste :         {Caste[c.caste]}\l
    Language :      {Language[c.language]}\l
    Food :          {Food[c.food]}\l
    Art:            {Art[c.art]}\l
    Music :         {Music[c.music]}\l
    Resource :      {Resource[c.resource]}\l
    '''
    return string

for i in range(total_amount_of_cities):
    dot.node(f'{i}',label=f'{city_info(cities[i])}')
    #city_info(cities[i])

dot.render(view=True)