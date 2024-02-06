# -------------------------TRVIA GAME---------


def game ():
    answer_num = 1
    uanswers = []
    correct_guesses = 0
    for key in questions_answers:
        print("----------------------")
        print(key)
        for i in answers[answer_num - 1]:
            print(i)
        useranswer = input("Input you answer: ")
        usanswer = useranswer.upper()
        uanswers.append(usanswer)
        answer_num = answer_num + 1
        correct_guesses  = correct_guesses + checker(questions_answers.get(key),usanswer)
    percentage = int(correct_guesses/len(questions_answers)*100)
    results(percentage,uanswers)

def checker (answer,usanswer):
    if answer == usanswer:
        return 1
    else:
        return 0
    
def results(percentage,uanswers):
    print("The correct answers are:")
    for i in questions_answers:
        print(questions_answers.get(i), end = " ")
    print("\nYour answers are:")
    for i in uanswers:
        print(i, end = " ")
    print(f"\n Your score is {percentage}%")

questions_answers = {"What is the capital of Bulgaria?" : "A",
                     "What is the name of the sea that borders Bulgaria?": "C",
                     "When was Bulgaria established?" : "B",
                     "What is the name of the current president of Bulgaria?" : "D"}

answers = [ ["A: Sofia", "B: Plovdiv", "C: Burgas", "D: Varna"],
           ["A: Mediterenean", "B: Red", "C: Black", "D: Indian"],
           ["A: 2000", "B: 681", "C: 1876", "D: 1014"],
           ["A: Boyko Borisov", "B: Ivan Kostov", "C: Petur Stoyanov", "D: Rumen Radev"]]

game()


