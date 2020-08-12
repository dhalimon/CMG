def mad_libs():
    print("Welcome to the game of Mad Libs! Where you will build your vocabulary and be entertained for hours!")
    reptile = []
    for i in range(5):
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



    #reptile = input("REPTILE: ")
    #adjective = input("ADJECTIVE: ")
    #number = input("NUMBER: ")
    #noun = input("PLURAL NOUN: ")
    #adverb = input("ADVERB: ")

    print("Once upon a time, there was a(n) %s. It was a very %s %s. It had %s %s. It lived %s ever after." % (
        reptile, adjective, reptile, str(number), noun, adverb))

    # else:
    #     print("Once upon a time, there was a %s." %(reptile))

def test():
    mad_libs()

test()