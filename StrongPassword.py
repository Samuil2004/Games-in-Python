# -------STRONG PASWWORD CREATOR-------

import random

storagePossibilities = ["Letter","CapLetter","Number","Symbol"]
storageLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
storageSymbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', '<', '=', '>', '?', '@', '[', ']', '^', '{', '}', '~']
storageNumbers = ["1","2","3","4","5","6","7","8","9","0"]
 
password = []
counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
duplicate_checker = None

print("A very strong password would be:")
for i in range (20):
    RandomChoice = random.choice(storagePossibilities)
    if RandomChoice == "Letter" and counter < 3:
        password.append(random.choice(storageLetters))
        counter = counter + 1
    elif RandomChoice == "CapLetter" and counter1 < 2:
        password.append(random.choice(storageLetters).capitalize())
        counter1 = counter1 + 1
    elif RandomChoice == "Number" and counter2 < 3:
        password.append(random.choice(storageNumbers))
        counter2 = counter2 + 1
    elif RandomChoice == "Symbol" and counter3 < 1:
        password.append(random.choice(storageSymbols))
        counter3 = counter3 + 1

password2 = "".join(password)
print(password2)
