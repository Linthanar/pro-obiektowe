import random
class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    #robimy listę kolorów kart i wartośći kart
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    #tworzymy klasę karta z zmiennymi kolor i wartość
    def __str__(self):
        return f"{Card.ranks[self.rank]}{Card.suits[self.suit]}"
    #łączymy kolor i wartość karty oraz sprawiamy ze mozna printować kartę w postaci - Q♦ J♦ 2♣
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank
    # ta funkcja sprawia ze mozemy porównywać karty, najpierw porównujemy wartości i jezeli są takie same (2♠,2♣) to
    # szeregujemy wzglądem koloru, ta funkcja pozwala porównywać obiekty "Card" bez tej funkcji nie dało by się 
    # szeregować kart a dodatkowo ten rodzaj funkcji nazywa się magiczny.


class Deck:
    # klasa "Deck" jest po to by stworzyć talię z obiektów "Card" i wykonywać proste działania na tej talii
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()
    # tutaj twozymy klasę talia która ma zmienną listę do której dodajemy pętlą obiekty "Card"
    def __len__(self):
        return len(self.deck)
    # ta funkcja sprawdza długość listy
    def add_card(self, card):
        self.deck.append(card)
    # ta funkcja dodaje karty
    def pop_card(self):
        return self.deck.pop()
    # ta funkcja zabiera karty
    def shuffle(self):
        random.shuffle(self.deck)
    # ta funkcja tasuje talię 

class Hand(Deck):
    # ta funkcja odpowiada za stworzenie ręki gracza. Ma ona swoją talię a do tego etykietę "Label" oraz punkty "win_count"
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0
        
    def __str__(self):
        return self.label + ': ' + ' '.join([str(card) for card in self.deck])
    # funkcja dzięki której mozna printować rękę, powyrzszą linię stworzyła 
    # obca cywilizacja
    def get_label(self):
        return self.label
    def get_win_count(self):
        return self.win_count

    def round_winner(self):
        self.win_count = self.win_count + 1


game_play = True

while game_play == True:

    deck = Deck()
    # tutaj tworzymy talię
    Player_1 = Hand('Player_1')
    Player_2 = Hand('Player_2')
    Player_3 = Hand('Player_3')
    Player_4 = Hand('Player_4')
    # tutaj tworzymy graczy
    for i in range(13):
        Player_1.add_card(deck.pop_card())
    for i in range(13):
        Player_2.add_card(deck.pop_card())
    for i in range(13):
        Player_3.add_card(deck.pop_card())
    for i in range(13):
        Player_4.add_card(deck.pop_card()) 
    # tutaj rozdajemy kazdemu graczowi karty
    print("You are",Player_1)
    # tutaj pokazuje którym jesteś graczem i wypisuje twoje kart

    bank = []
    # a tam gdzie to kretowisko będzie stało San Francisco 
    # a tam gdzie to kretowisko będzie stał mój bank

    for round in range(13):
        # ta pętla to światowej sławy hard-kod
        bank.append(Player_1.deck[len(Player_1.deck)-1])
        bank.append(Player_2.deck[len(Player_2.deck)-1])
        bank.append(Player_3.deck[len(Player_3.deck)-1])
        bank.append(Player_4.deck[len(Player_4.deck)-1])
        # tutaj dodajemy ostatni element z listy do banku
        if max(bank) == Player_1.deck[len(Player_1.deck)-1]:
            Player_1.round_winner()
            print("Player_1 win")
        if max(bank) == Player_2.deck[len(Player_2.deck)-1]:
            Player_2.round_winner()
            print("Player_2 win")
        if max(bank) == Player_3.deck[len(Player_3.deck)-1]:
            Player_3.round_winner()
            print("Player_3 win")
        if max(bank) == Player_4.deck[len(Player_4.deck)-1]:
            Player_4.round_winner()
            print("Player_4 win")
        # następnie porównujemy ostatnie elementy z decku do największego elementu z banku. 
        # Następnie dodajemy punkty i pokazujemy kto zasłuzył na zwycięstwo
        for y in range(4):
            bank.pop()
        # tutaj usuwamy karty z banku
        print('')
        print('Player_1 :',Player_1.pop_card())
        print('Player_2 :',Player_2.pop_card())
        print('Player_3 :',Player_3.pop_card())
        print('Player_4 :',Player_4.pop_card())
        print('')
        # tutaj pokazujemy ostatnie karty graczy i je usuwamy

    print(Player_1.get_win_count())
    print(Player_2.get_win_count())
    print(Player_3.get_win_count())
    print(Player_4.get_win_count())
    # na końcu pokazujemy wyniki
    game_play = False
    # to kończy grę i jeszcze krótka fraszka 

print("kto gra w karty ten ma łeb obdarty")



