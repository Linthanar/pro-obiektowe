import random

#Deck = 52 cards Jack Queen King Ace
#Clubs    - trefl - C2
#Diamonds - karo  - DA
#Heards   - kier  - H10
#Spades   - pik   - SJ

#talia kart wygenerowana wcześniej
kced = []
deck = [['C2', 2], ['C3', 3], ['C4', 4], ['C5', 5], ['C6', 6], ['C7', 7], ['C8', 8], ['C9', 9], ['C10', 10], ['CJ', 10], ['CQ', 10], ['CK', 10], ['CA', 11],
        ['D2', 2], ['D3', 3], ['D4', 4], ['D5', 5], ['D6', 6], ['D7', 7], ['D8', 8], ['D9', 9], ['D10', 10], ['DJ', 10], ['DQ', 10], ['DK', 10], ['DA', 11],
        ['H2', 2], ['H3', 3], ['H4', 4], ['H5', 5], ['H6', 6], ['H7', 7], ['H8', 8], ['H9', 9], ['H10', 10], ['HJ', 10], ['HQ', 10], ['HK', 10], ['HA', 11],
        ['S2', 2], ['S3', 3], ['S4', 4], ['S5', 5], ['S6', 6], ['S7', 7], ['S8', 8], ['S9', 9], ['S10', 10], ['SJ', 10], ['SQ', 10], ['SK', 10], ['SA', 11]]

#zmienne
oppvalue = 0
pvalue = 0
oppsigns = " "
signs = " "

win = False
round = True
oppturn = True

oppHand = []
plaHand = []

#ta funkcja dodaje kartę do stosu kart odrzuconych i usuwa z stosu.
def save():
    kced.append(deck[0])
    deck.pop(0)

#ta funkcja dodaje pierwszą kartę z decku do ręki komputera i do stosu kart odrzuconych a następnie usuwa i tak dwa razy
def opponentcards():
    for i in range(2):
        oppHand.append(deck[0])
        save()
    print("Your opponents card is "+ str(oppHand[0][0]))

#ta funkcja liczy wartość kart gracza i zwraca ją w postaci int
def playerval():
    global pvalue
    pvalue = 0
    for i in range(len(plaHand)):
        pvalue += plaHand[i][1]
    return pvalue

#ta funkcja zapisuje znaki kart z ręki gracza
def playersigns():
    global signs
    signs = " "
    for i in range(len(plaHand)):
        signs += plaHand[i][0] + " "
    return signs
#ta funkcja liczy wartość kart komputera
def opponentval():
    global oppvalue
    oppvalue = 0
    for i in range(len(oppHand)):
        oppvalue += oppHand[i][1]
    return oppvalue
#ta funkcja zapisuje znaki kart z ręki komputera
def opponentsings():
    global oppsigns
    oppsigns = " "
    for i in range(len(oppHand)):
        oppsigns += oppHand[i][0] + " "
    return oppsigns

#Początek gry
random.shuffle(deck)
while win == False:
    #pokazuje nam ręke komputera
    opponentcards()

    while round == True:
        #sprawdza znaki i wartości kart
        playerval()
        playersigns()
        #pyta nas o to czy strzelać czy pasować
        choice = input("Your cards: "+ signs +" - write h if hit or s if stay: ")

        #sprawdza czy pasowaliśmy pokazuje nasze karty i kończy naszą turę
        if choice == "s":
            print("Your cards: "+signs+" your points "+str(pvalue))
            break
        #sprawdza czy strzelaliśmy
        if choice == "h":
            #dodaje kartę z decku i sprawdza wartość kart
            plaHand.append(deck[0])
            save()
            playerval()
            playersigns()
            #jeśli wartość kart przekracza 21 to przegrywa gracz
            if pvalue > 21:
                print("You lose :(")
                print("Your cards- "+signs+" points- "+str(pvalue))
                oppturn = False
                break
            #jeśli wartość kart przekracza 21 to gramy dalej
            else:
                print("Go next")

    while oppturn == True:
        #sprawdzanie kart komputera i wyświetlenie wyniku
        opponentval()
        opponentsings()
        print("Opponents cards "+ oppsigns)
        print("Opponents points "+str(oppvalue))
        #Jezeli wartość jest większa od 17 to komputer pasuje
        if oppvalue >= 17 and oppvalue <= 21:
            #Jezeli komputer ma więcej lub tyle samo punktów to wygrywa
            if oppvalue >= pvalue:
                print("You lose :(")
                print("Your cards- "+signs+" points- "+str(pvalue))
                print("Your opponent cards- "+oppsigns+" points- "+str(oppvalue))
                break
            
            #W przeciwnym razie przegrywa
            else:
                print("You win!!!")
                print("Your cards- "+signs+" points- "+str(pvalue))
                print("Your opponent cards- "+oppsigns+" points- "+str(oppvalue))
                break
        #Jezeli wartość jest większa od 21 to komputer przegrywa
        elif oppvalue > 21:
            print("You win!!!")
            print("Your cards- "+signs+" points- "+str(pvalue))
            print("Your opponent cards- "+oppsigns+" points- "+str(oppvalue))
            break
        #Jezeli komputer ma ponizej 17 to dobiera kartę
        else:
            oppHand.append(deck[0])
            save()
            print("Opponent draw Next")

    win = True

