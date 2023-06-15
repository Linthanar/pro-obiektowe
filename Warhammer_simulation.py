import random

class Core:  # Core to rdzeń mechaniki odpowiadającej za rzuty oraz testy
    def __init__(self,trait,adv_point):
        # ta klasa ma zmienne: 

        self.trait = trait              # (trait) - jest to cecha(wartość) do której porównuje się wynik na kości k100
        self.adv_point = adv_point      # (adv_point)- jest to wartość jaką się dodaje do punktów_sukcesu po rzucie(roll)
        self.win = False                # (win)- jest potrzebna do określenia kto wygrał
        self.save = []                  # (seve)- zapisuje rzuty zebym mógł sprawdzić jakie rzuty padły 

    def roll(self,parameter):   # ta funkcja rzuca kością a następnie oblicza sukcesy

        if self.adv_point > 3:
            self.adv_point = 3
        # ta linijka jest po to by punkty przewagi (adv_point) nie przekroczyły limitu(3)
        roll = random.randint(1,100)    
        self.save.append(roll)
        # ta linijka odpowiada za rzut kością oraz zapis wartości tego rzutu
        if parameter - roll >= 0 :
            ps = (parameter //10) - (roll//10) +1
            ps = ps + self.adv_point
            return ps
        else:
            ps = (parameter //10) - (roll//10) -1
            ps = ps + self.adv_point
            return ps 
        # te funkcje logiczne odpowiadają za oblicznie ilości punktów_sukcesu
    def skill_test(self,other):    # ta funkcja porównuje rzuty i określa zwycięzcę 

        roll_self = self.roll(self.trait)           
        roll_other = other.roll(other.trait)        # te linijki przypisują rzut do zmiennej
        self.win = False
        other.win = False                           # tu ustawia się zwycięstwo jako fałsz
        
        if roll_self > roll_other:
            self.win = True
            return roll_self 
        if roll_self < roll_other:
            other.win = True
            return roll_other
        # te linijki sprawdzają kto wygrał test i zwracają sukcesy wygrywającego 

class Creature(Core):       # ta funkcja odpowiada za cechy postaci oraz walkę kreatury

    def __init__(self,WW,Broń,PP,Żyw,trait,adv_point):
        super().__init__(trait,adv_point)

        self.WW = WW                # ta zmienna jest cechą która odpowiada za szansę powodzenia rzutu na atak
        self.Broń = Broń            # ta zmienna jest obrazeniami jakie zadaje postać
        self.PP = PP                # ta zmienna jest obrazeniami radukowanymi przez postać po przyjęciu obrazeń
        self.Żyw = Żyw              # ta zmienna jest ilością zycia postaci
        self.adv_point = 0           # ta zmienna jest punktami przewagi postaci
        self.death = False

    def atack(self,other):  # ta zmienna odpowiada za atak
        
        self.trait = self.WW
        other.trait = other.WW                  # ta linijka odpowiada za przypisanie Walki_Wręcz jako wartość dla rzutu
        result = self.skill_test(other)         # ta linijka przypisuje do rezultatu ilość sukcesów
        
        if self.win == True:                    # ta logika odpowiada za zdecydowanie kto wygrał oraz obliczeniu obrazeń przyjętych przez przeciwnika
            if other.PP < self.Broń + result:
                other.Żyw = other.Żyw +(other.PP - (self.Broń + result)) 
                self.adv_point +=1
                other.adv_point = 0             # tutaj dodaje się punkty przewagi atakującemu oraz zabiera się obrońcy
            else:
                other.Żyw -= 1
                self.adv_point +=1
                other.adv_point = 0             # tutaj dodaje się punkty przewagi atakującemu oraz zabiera się obrońcy
        
        if other.win == True:
            other.adv_point +=1
            self.adv_point = 0                  # tutaj dodaje się punkty przewagi obrońcy oraz zabiera się atakującemu
    
    def turn(self,other):
        if self.Żyw >= 0:
            self.death = False
            self.atack(other)
        else:
            self.death = True


    def __str__(self):
        return 'WW: {} Broń: {} PP: {} Żyw: {} Trait: {} Adv: {}'.format(self.WW,self.Broń,self.PP,self.Żyw,self.trait,self.adv_point)
    # ta funkcja pokazuje wartości cech postaci


niedzwiedz = Creature(45,8,5,28,0,0)                # zdefiniowanie klasy
krwiopuszcz = Creature(55,9,3,17,0,0)

print(niedzwiedz)                                   
print(krwiopuszcz)

game = True                                         # ustawienie warunków pętli 
round1 = True
round2 = True
win1 = 0
win2 = 0

for x in range(100000):                             # wstęp do pętli
    niedzwiedz = Creature(50,7,3,12,0,0)
    krwiopuszcz = Creature(50,7,3,12,0,0)
    game = True

    while game == True:                             
        round1 = True
        round2 = True
        #TODO  DRY - DON'T REPEAT YOURSELVES!
        while round1 == True:
            if niedzwiedz.death == False:           # jezeli kreatura zyje to zadaje obrazenia i kończy swoją turę
                niedzwiedz.turn(krwiopuszcz)        # jeśli nie to druga kreatura dostaje punkt zwycięstwa i kończą się tury i gra
                niedzwiedz.turn(krwiopuszcz)        
                round1 = False
            else:
                win2  += 1
                round1 = False
                round2 = False
                game = False

        while round2 == True:                       # jezeli kreatura zyje to zadaje obrazenia i kończy swoją turę 
            if krwiopuszcz.death == False:          # jeśli nie to druga kreatura dostaje punkt zwycięstwa i kończą się tury i gra
                krwiopuszcz.turn(niedzwiedz)
                round2 = False
            else:
                win1  += 1
                round1 = False
                round2 = False
                game = False

        

print(win1)
print(niedzwiedz)
print(win2)
print(krwiopuszcz)

# TODO: Zrób faktorkę
def factory():
    pass

# TODO
def main():
    print('hello world')

def runSimulation(arg=100000):
    print('run with',arg,"times")

if __name__ == "__main__":
    factory()
    main()














# print()
# krwiopuszcz.atack(niedzwiedz)

# print(niedzwiedz.save[len(niedzwiedz.save)-1])
# print(krwiopuszcz.save[len(krwiopuszcz.save)-1])

# # print("niedzwiedz broni się")
# print(niedzwiedz)
# # print("krwiopuszcz atakuje")
# print(krwiopuszcz)

# if niedzwiedz.Żyw < 0:
#     Game = False

# print()
# niedzwiedz.atack(krwiopuszcz)

# print(niedzwiedz.save[len(niedzwiedz.save)-1])
# print(krwiopuszcz.save[len(krwiopuszcz.save)-1])

# print("niedzwiedz atakuje")
# print(niedzwiedz)
# print("krwiopuszcz broni")
# print(krwiopuszcz)

# if krwiopuszcz.Żyw < 0:
#     Game = False

