import random 
import jetson_inference, jetson_utils, argparse, system

#todo add ML file to imports above

#create data for the game at start
mlCard1 = random.randint(0, 11)
mlCard2 = random.randint(0, 11)
ml_cards = [mlCard1, mlCard2]

p1card = random.randint(0,11)
p1card2 = random.randint(0,11)
p1cards = [p1card, p1card2]
extras = []
extra = 0

#checks if number is over 21 
def check(): 

#whenever cards is to be raised, go here
def raiser():
    global extra, p1cards, extras
    extra = extra + 1   
    while(extra > 0):
        extras.append(random.randint(0,11))
        p1cards = extras + p1cards
        print("your next card is: " + str(extras))
        print("and now your new total is: " + str((sum(p1cards))))
        extra = extra - 1
        up2 = input("do you raise again?(y/n)")
        if str.lower(up2) == "yes" or "y":
                extra = extra + 1
        else:
            game()

# the game
def game():
    up = input("Do you raise? (y/n) ")
    if str.lower(up) == "yes" or "y" :
        raiser()

    elif str.lower(up) == "no" or "n":
        print("you chose to stay.")


#start of game ONLY
print("Blackjack")
print("Your starting cards are " + str(p1cards) + ".. totaling " + str(sum(p1cards)) )
print("your opponent has: " + str(mlCard1) +" , and a card you cannot see.") 
