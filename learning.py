import random
import argparse, sys, time
card1 = random.randint(1,11)
card2 = random.randint(1,11)
cards = []
count = 0
top = 21
wins = 0

numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def replay():
    bot2()
    check2()

def check2(): 
    if sum(p1cards) > 21:
        replay()
    else:
        return

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

def begin():
    bot2()
    check2()


def whatever():
    global card1, card2, cards, count, top, wins, sumnatioj
    for i in range (80000):
        time.sleep(2)
        print(str(cards))
        while sum(cards) < 21:
            count = count + 1 #todo add cards to hand here
            print(count)
            cards.append(random.randint(1, 11))
            sumnatioj = 0
            for j in range (len((cards))- 1):
                sumnatioj = sumnatioj + cards[j]
                numbers[sumnatioj] = numbers[sumnatioj] + 1
                count = count - 1   
            file = open('numbers.txt','w')
            file.write(str(numbers))
        if count >= 1:
            cards.append(random.randint(1, 11))
            sumnatioj = 0
            for j in range (len((cards))-1) :
                sumnatioj = sumnatioj + cards[j]
                numbers[sumnatioj] = numbers[sumnatioj] + 1
                count = count - 1   

whatever()