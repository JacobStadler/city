from enum_choices import *
import random as r
class City():
    def __init__(self,name):
        self.name = name
        self.population = 0
        self.residents = []
        self.nond_n = [] # non directinal neighbors for testing
        self.neighbors = [None,None,None,None]
        self.readable_neighbors = [None,None,None,None]
        self.founder = None
        # prefrences
        self.pref = []
        #self.trade = None
        #self.genderroles = None
        #self.event = None
        #self.religion = None
        #self.authority = None
        #self.caste = None
        #self.language = None
        #self.food = None
        #self.art = None
        #self.music = None
        #self.resource= None
    def random_pref(self):
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

    def initiate_pref(self):
        votes = [[0,0,0,0],[0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0]]
        most_votes = [0,0,0,0,0,0,0,0,0,0]
        #print(f'{len(votes)} {len(most_votes)}')
        for i in range(len(self.residents)):
            for j in range(len(votes)):
                for k in range(len(votes[j])):
                    #print(self.residents[i].pref[j][k])
                    votes[j][k] += self.residents[i].pref[j][k]
                if votes[j][k] > votes[j][most_votes[j]]:
                    most_votes[j] = k
        self.pref = most_votes

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
            #print(print_string)
    def city_info(self):
        i = 0
        total_aproval = 0
        while i < len(self.residents):
            total_aproval += self.residents[i].like(self)
            i += 1
        string = f'''
        City :          {self.name}\l
        Avg Approval :  {round(total_aproval/len(self.residents),2)}\l
        Pop:            {self.population}\l
        Auth:           {Authority0[self.authority[0]]} {Authority1[self.authority[1]]}\l
        Trade:          {Trade[self.trade]}\l
        Gender Roles:   {GenderRolls[self.genderroles]}\l
        Events :        {Events[self.event]}\l
        Religion :      {Religion[self.religion]}\l
        Caste :         {Caste[self.caste]}\l
        Language :      {Language[self.language]}\l
        Food :          {Food[self.food]}\l
        Art:            {Art[self.art]}\l
        Music :         {Music[self.music]}\l
        Resource :      {Resource[self.resource]}\l
        '''
        return string