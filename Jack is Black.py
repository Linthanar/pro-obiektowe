from pickle import TRUE
import random
#tworzymy klasę "Deck". Ma ona na celu wykonywanie prostych czynności na stosie kart oraz stworzenie tego stosu.
class Deck:

    def __init__(self):
        self.deck = [['C2', 2], ['C3', 3], ['C4', 4], ['C5', 5], ['C6', 6], ['C7', 7], ['C8', 8], ['C9', 9], ['C10', 10], ['CJ', 10], ['CQ', 10], ['CK', 10], ['CA', 11],
        ['D2', 2], ['D3', 3], ['D4', 4], ['D5', 5], ['D6', 6], ['D7', 7], ['D8', 8], ['D9', 9], ['D10', 10], ['DJ', 10], ['DQ', 10], ['DK', 10], ['DA', 11],
        ['H2', 2], ['H3', 3], ['H4', 4], ['H5', 5], ['H6', 6], ['H7', 7], ['H8', 8], ['H9', 9], ['H10', 10], ['HJ', 10], ['HQ', 10], ['HK', 10], ['HA', 11],
        ['S2', 2], ['S3', 3], ['S4', 4], ['S5', 5], ['S6', 6], ['S7', 7], ['S8', 8], ['S9', 9], ['S10', 10], ['SJ', 10], ['SQ', 10], ['SK', 10], ['SA', 11]]
        self.shuffle()
    #tutaj tworzymy listę kart i tasujemy
    
    def append(self,card):
        self.deck.append(card)
    #tutaj dodajemy kartę
    def pop(self):
        return self.deck.pop()
    #tutaj zabieramy kartę
    def len(self):
        return len(self.deck)
    #tutaj sprawdzamy długość decku jakby była potrzebna
    def shuffle(self):
        random.shuffle(self.deck)
    #tutaj tasujemy talię
    def __str__(self):
        return str(self.deck)
    #tutaj dajemy mozliwość podglądu decku

game_deck = Deck()

#to jest serce naszego programu. tutaj będą funkcje takie jak: pokazanie kart, liczenie punktów, dobieranie karty lub pasowanie.
# te najwazniejsze funkcje odpowiadające za grę to: *Dla bota sprawdzenie warunków dobierania, *Dla gracza pytanie czy strzela czy pasuje.
class Player(Deck):

    def __init__(self,label,cards_num):
        self.label = label
        self.cards_num = cards_num
        self.deck = []
        #tutaj tworzymy zmienne
        self.signs = ""
        self.points = 0
        for i in range(cards_num):
            self.deck.append(game_deck.pop())
        #tutaj dodajemy karty i sprawdzamy punkty
        self.point_counter()
        self.card_counter()

    def point_counter(self):
        #ta funkcja odpowiada za liczenie punktów
        self.points = 0
        for i in range(len(self.deck)):
            self.points += self.deck[i][1]
        return self.points

    def card_counter(self):
        #ta funkcja odpowiada za dodawanie znaków kart z talii
        self.signs = ""
        for i in range(len(self.deck)):
            self.signs += self.deck[i][0] + " "
        return self.signs

    def player_round(self):
        # to jest tura gracza
        choice = input("{} write h if hit or s if stay: ".format(self.__str__()))
        if choice == "s":
            print(self.__str__())
            return 'stay'
        #sprawdza czy strzelaliśmy
        if choice == "h":
            #dodaje kartę z decku i sprawdza wartość kart
            self.deck.append(game_deck.pop())
            self.point_counter()
            self.card_counter()
            print(self.__str__())
            return 'hit'

    def bot_round(self):
        # to jest tura bota
        if self.points >= 17:
            print(self.__str__())
            return 'stay'
        else:
            self.deck.append(game_deck.pop())
            self.point_counter()
            self.card_counter()
            print(self.__str__())
            return 'hit'

    def __str__(self):
        #ta funkcja pokazuje schemat printowania klasy
        return ("{} cards: {} points: {} ").format(self.label,self.signs,self.points)


player = Player('Simon',0)
opponent = Player('Peter',1)

print(opponent)
print(player)

score = 0
round = True 
oppround = True

# to jest logika gry
while round == True:
    message = player.player_round()
    if message == 'hit':
        if player.points > 21:
            print('You are louser')
            oppround = False
            break
    elif message == 'stay' :
        break

while oppround == True:
    oppmessage = opponent.bot_round()
    if oppmessage == 'stay':
        if 21 > opponent.points >=player.points:
            print('You are Louser')
            break
        elif opponent.points > 21:
            print('You are Winner')
            break
        else:
            print('You are Winner')
            break
    else:
        print("Opponent draw")

