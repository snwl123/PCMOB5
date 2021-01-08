import random

def roll_dice():
    for i in range (0,5):
        print ('Dice ' + str(i+1) + " rolls " + str(random.randint(1,7)) + ".")

roll_dice()