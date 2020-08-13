#Newer version on Github _ newStory.py
def mad_libs():
    print("Welcome to the game of Mad Libs! Where you will build your vocabulary and be entertained for hours!")

    reptile = [] #create an empty list
    for i in range(5): #Add  five items
        reptile.append(input('Enter five new REPTILE: '))
    print(reptile)


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

    print("Once upon a time, there was a(n) %s. It was a very %s %s. It had %s %s. It lived %s ever after." % (
        reptile, adjective, reptile, str(number), noun, adverb))


def test():
    mad_libs()

test()