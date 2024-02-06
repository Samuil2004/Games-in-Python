# --------MASTERMIND GAME------------


import random

storage = [0,1,2,3,4,5,6,7,8,9]

def number_generator():
    num1 = []
    while True:    
        while len(num1) < 4:
            element = random.choice(storage)
            if element not in num1:
                num1.append(element)
            if num1[0] == 0:
                num1.pop(0)
        return(num1)


num2 = number_generator()
num3 = [str(num) for num in num2]
num4 = "".join(num3)

for i in range(4):
    print("* ", end = "")


def checker(num2):
    counter5 = 0
    while True:
        counter = 0
        counter2 = 0
        sss = []
        guess = input("\nPlease input a number ")
        counter5 = counter5 + 1
        guess1 = [int(digit) for digit in str(guess)]
        if guess1 == num2:
            print("Correct. You win")
            break
        elif counter5 == 12:
            print(f"Unfortunatelly you ran out of tries :( the hidden number was {num4}")
            break
        elif len(guess) == 4:
            for i in range(0,4):
                a = guess1[i]
                b = num2[i]
                if a == b:
                    counter += 1
                    sss.append(a)
            for i in range (0,4):
                a = guess1[i]
                if a in num2 and a not in sss:
                    sss.append(a)
                    counter2 = counter2 + 1
            print(f"{counter} digits are at the correct possition")
            print(f"{counter2} correcet digits, but at wrong possitions")
        else:
            print("The number must be four digits long.Try again")
checker(num2)
