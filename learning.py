import random
import argparse, sys, time
card1 = random.randint(1,11)
card2 = random.randint(1,11)
cards = []
count = 0
top = 21
wins = 0

#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
numbers = []

def replay():
    bot2()
    check2()

def check2(): 
    if sum(p1cards) > 21:
        replay()
    else:
        return

def bot2():
    global card1, card2, cards, count, top, wins
    print(str(cards))
    while sum(cards) <= 18 and count == 0:
        cards.append(random.randint(1, 11))
        count = count + 1
        time.sleep(1)
        if count >= 1:
            cards.append(random.randint(1, 11))
            count = count - 1
        if sum(cards) == 21:
            wins = wins + 1
                