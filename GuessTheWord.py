# -----------GUESS THE WORD GAME--------

def main():
    import random
 

    storage = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', "apple", 
         "banana", "cherry", "dog", "elephant", "flower",
        "giraffe", "hamburger", "icecream", "jacket", "kangaroo",
        "lemon", "monkey", "noodle", "octopus", "penguin", 
        "quokka", "rabbit", "strawberry", "tiger", "umbrella",
        "culture", "watermelon", "xylophone", "zebra", "astronomy",
        "basketball", "computer", "dolphin", "eagle", "fireworks",
        "guitar", "happiness", "internet", "jigsaw", "kitchen",
        "lighthouse", "mountain", "nirvana","ocean", "paradise",
        "quantum", "rainbow", "starfish", "telescope", "universe",
        "volcano", "waterfall", "xylophone","yellow", "zeppelin"]

    word = random.choice(storage)

    hiddenletters = word[1:-1]

    mrm = list(word)
    rmr = list(hiddenletters)
    newword = []

    print("The hidden word is:")
    print(mrm[0], end = "")
    for x in range(0, len(mrm) -2):
        print("*", end = "")
    print(mrm[-1])

    ggg = []
    for i in range(0,len(rmr)):
        ggg.append("*")

    print("Try to guess it. You are permited to guess only 15 times, otherwise the balloon will explode and destroy everything, hence try to save the world. Wish you luck!")
    counter = 0
    for g in range(10):
        counter = counter +1      
        if counter == 10:
            print(f"The hidden word is {word.capitalize()}.Unfortunatelly, you ran out of tries and lost.")
            again1 = input("If you want to play again press Y, if you want to exit press E ")
            if again1 == "Y" or again1 == "y":
                main()
            else:
                exit()   
        if ggg == rmr:
            print(f"Congratulations, you won the game. The hidden word is {word.capitalize()}")
            again = input("If you want to play again press Y, if you want to exit press E ")
            if again == "Y" or again == "y":
                main()
            else:
                exit()
        m = input("Input a letter:")
        if m.isalpha() == False:
            print("Please input only letters")
        elif m not in rmr:
            print(f"Wrong input. There isn't {m} in the word. Try again")
        elif m in word:
            for x in range(len(rmr)):
                if rmr[x] == m:
                    ggg.pop(x)
                    ggg.insert(x,m)
                    guess = "".join(ggg)
            print(mrm[0] + guess + mrm[-1])  
main()

