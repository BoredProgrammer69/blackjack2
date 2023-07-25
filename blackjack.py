import random
import jetson_inference, jetson_utils, argparse, sys

#todo add ML file to imports above
#todo fix the infinite looping problem -- CHECK
#todo add data collection !!

#create data for the game at start
mlCard1 = random.randint(1, 11)
mlCard2 = random.randint(1, 11)
ml_cards = [mlCard1, mlCard2]


p1card = random.randint(1,11)
p1card2 = random.randint(1,11)
p1cards = [p1card, p1card2]
extras = []
extra = 0
top = 21

#replay the game if required
def replay():
    replay = input("Would you like to play again? (y/n) ")
    if str.lower(replay) == "yes" or str.lower(replay) == "y" :
        global p1cards, extras, ml_cards
        p1cards = []
        extras = []
        ml_cards = [] 
        begin()
    else:
        exit()

#checks if number is over 21 
def check(): 
    if sum(p1cards) > 21:
        print("You've broken 21! You loose! ") 
        replay()
    else:
        return

#whenever cards is to be raised, go here
def raiser():
    global extra, p1cards, extras
    extra = extra + 1   
    while(extra > 0):
        extras.append(random.randint(1,11))
        p1cards = extras + p1cards
        print("your next card is: " + str(extras) + " , making your hand: "+ str(p1cards))
        print("and now your new total is: " + str((sum(p1cards))))
        check()
        extra = 0
        up2 = input("do you raise again?(y/n) ")
        if str.lower(up2) == "yes" or str.lower(up2) == "y":
            extra = extra + 1
            extras = []
            check()
        else:
            extra == 0
            return



# the ask
def ask():
    up = input("Do you raise? (y/n) ")
    print(up)
    print(str.lower(up) == "yes")
    if str.lower(up) == "yes" or str.lower(up) == "y":
        raiser()
    else:
        print("you chose to stay.")
        game()


#start of game
def begin():
    mlCard1 = random.randint(1, 11)
    mlCard2 = random.randint(1, 11)
    ml_cards = [mlCard1, mlCard2]

    p1card = random.randint(1,11)
    p1card2 = random.randint(1,11)
    p1cards = [p1card, p1card2]
    extras = []
    print("Your starting cards are " + str(p1cards) + ".. totaling " + str(sum(p1cards)) )
    print("your opponent has: " + str(mlCard1) +" , and a card you cannot see.") 
    ask()

# game itself?
def game():
    print("game")

#  the bot deciding wether or not to raise, lower
#  todo add data/decision collection!!
 def bot():
    global mlCard1, ml_cards, mlCard2, p1card
    














begin()

