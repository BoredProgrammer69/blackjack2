import random
import argparse, sys, time
card1 = random.randint(1,11)
card2 = random.randint(1,11)
cards = []
count = 0
top = 21
wins = 0

numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# def replay():
#     bot2()
#     check2()

# def check2(): 
#     if sum(p1cards) > 21:
#         replay()
#     else:
#         return

# def bot2():
#     global card1, card2, cards, count, top, wins
#     print(str(cards))
#     while sum(cards) <= 21 and count == 0:
#         cards.append(random.randint(1, 11))
#         count = count + 1
#         time.sleep(1)
#         if count >= 1:
#             cards.append(random.randint(1, 11))
#             count = count - 1
#         if sum(cards) == 21:
#             wins = wins + 1




def whatever():
    global card1, card2, cards, count, top, wins, sumnatioj
    card1 = random.randint(1,11)
    card2 = random.randint(1,11)
    cards = []
    cards.append(card1)
    cards.append(card2)
    count = 0
    top = 21
    wins = 0
    for i in range (80000):
        time.sleep(2)
        print(str(cards))
        while sum(cards) < 21:
            count = count + 1 
            cards.append(random.randint(1, 11))
            sumnatioj = 0
            for j in range (len((cards))- 1):
                sumnatioj = sumnatioj + cards[j]
                numbers[sumnatioj] = numbers[sumnatioj] + 1
                count = count - 1   
            file = open('numbers.txt','w')
            file.write(str(numbers))
            if sum(cards) == 21:
                count = 0
                wins = wins + 1
                print("Win with cards: " + str(cards))
                file = open('numbers.txt','w')
                file.write("/nWIN! With cards " + str(cards))   
                whatever()
        if sum(cards) == 21:
                count = 0
                wins = wins + 1
                print("Win with cards: " + str(cards))
                file = open('numbers.txt','w')
                file.write("/nWIN! With cards " + str(cards))   
                whatever()
        if sum(cards) > 21:
            count = count - 1
            # lent = len(cards)
            sumnatioj = 0
            for j in range (0, len((cards))-1) :
                sumnatioj = sumnatioj + cards[j]
            # sumnatioj = sumnatioj + cards[j]
            numbers[sumnatioj] = numbers[sumnatioj] - 1
            print("Loss with: " + str(cards))
            file = open('numbers.txt','w')
            file.write(str(numbers))
            whatever()
        if count >= 1:
            cards.append(random.randint(1, 11))
            sumnatioj = 0
            for j in range (len((cards))-1) :
                sumnatioj = sumnatioj + cards[j]
                numbers[sumnatioj] = numbers[sumnatioj] + 1
                count = count - 1   
                file = open('numbers.txt','w')
                file.write(str(numbers))
                

whatever()