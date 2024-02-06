# --------------The Gambling Pig Game--------
import random
sum = 0
counter = 0
while True:
    if sum >= 50:
        print("You won. You have already reached 50 points")
        break
    choice = input("Do you want to roll the dice? \n Answer 'Yes' or 'No' ")
    if choice == "yes" or choice == "Yes":
        num = random.randint(1,6)
        counter = counter + 1
        if num == 1:
            sum = 0
            print(f"Your score is {sum}")
            print(f"{counter} tries")
        else:
            sum = sum + num
            print(f"Your score is {sum}")
            print(f"{counter} tries")
    elif choice == "no" or choice == "No":
        print(f"Your score is {sum}")
        print(f"{counter} tries")
        break
