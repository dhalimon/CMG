import random

def mad_libs():
    print("Welcome to the game of Mad Libs! Where you will build your vocabulary and be entertained for hours!")
    reptile = []  #create an empty list
    for i in range(5): #Add  five items
        reptile.append(input('Enter five new REPTILE: '))
    print(reptile) # prints out list- optional


    adjective = []
    for i in range(5):
        adjective.append(input('Enter new ADJECTIVE: '))
    print(adjective)
    # a list of nouns, verbs, adjectives used in the GAME OF MADLIBS!

    number = []
    for i in range(5):
        number.append(input('Enter new NUMBER: '))
    print(number)

    noun = []
    for i in range(5):
        noun.append(input('Enter new NOUN: '))
    print(noun)

    adverb = []
    for i in range(5):
        adverb.append(input('Enter new ADVERB: '))
    print(adverb)

    # Creates random choice from list of five items
    print("Once upon a time, there was a(n) %s. It was a very %s %s. It had %s %s. It lived %s ever after." % (random.choice(reptile),
random.choice(adjective),
random.choice(reptile),
random.choice(str(number)),
random.choice(noun),
random.choice(adverb)))


def test():
    mad_libs() # Runs above function

test()