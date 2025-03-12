import sys
import os
import platform


def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


print("\nWelcome to my QUIZ GAME!\n")


def Question_setup():
    global Questions
    while True:
        try:
            Questions = int(input("\nHow many questions would you like to input? \n" ))
            if isinstance(Questions, int): 
                break
        except ValueError:
            print("Please enter a valid integer.")
        else:
            print("The number of questions must be an integer.")


def Playing():
    playing = input("Do you want to set up the Quiz? (Yes/No) \n")
    if playing.lower() == "yes":
        Question_setup()
    elif playing.lower() == "no":
        clear_terminal()
        print("Thank you for playing.")
        sys.exit()
    else:
        print("Invalid response. Please answer with 'Yes' or 'No'.")
        Playing()


Playing()


questions = []
answers = []


def Question_reset(start_idx=0, total_questions=0):
    i = start_idx
    while i < total_questions:
        question = input(f"\nEnter question {i + 1}: ")
        answer = input(f"Enter Answer {i + 1}: ")
        questions.append(question)
        answers.append(answer)
        i += 1


Question_reset(0, Questions)


def Confirmation():   
    confirmation = input("Would you like to add more questions? (Yes/No) \n")
    if confirmation.lower() == "yes":
        try:
            additional_questions = int(input("\nHow many more questions? \n"))
            global Questions
            Questions += additional_questions  
            Question_reset(len(questions), Questions)  
            main() 
        except ValueError:
            print("Invalid Input. Please enter a valid integer for the number of questions.\n")
            Confirmation()
    elif confirmation.lower() == "no":
        print("\nThank you for setting up the quiz!\n")
        quiz_start()
    else:
        print("Invalid response. Please answer with 'Yes' or 'No'.\n")
        Confirmation() 


def quiz_start():
    quizstart=input("Should we start the quiz.\n")
    if quizstart.lower() == "yes":
        clear_terminal()
        quiz()
    elif quizstart.lower() == "no":
        clear_terminal()
        print("Thank you for attempting Quiz Game.")
    else:
        print("Invalid response: Input should be Yes or No.\n")
        quiz_start()


def quiz(): 
    score = 0 
    for idx in range(len(questions)):
        print(f"Question {idx + 1}: {questions[idx]}")
        user_answer = input("Your answer: ").lower()  
        if user_answer == answers[idx].lower():  
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {answers[idx]}\n")
    print(f"\nYour final score: {score}/{len(questions)}")
    print("")
    New()


def New():
    Starting_New = input("Would you like to continue, restart or exit?\n") 
    if Starting_New.lower() == "continue" :
        print("")
        Confirmation()
    elif Starting_New.lower() == "restart" :
        clear_terminal()
        restart()
    elif Starting_New.lower() == "exit" :
        clear_terminal()
        print("Thank You for Playing.\n")
        sys.exit()
    else : 
        print("Invalid Input")
        New()


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def main():
    print("\nYou have entered the following questions and answers:")
    for idx in range(len(questions)):
        print(f"\nQuestion {idx + 1}: {questions[idx]}")
        print(f"Answer {idx + 1}: {answers[idx]}")
        print() 
    Confirmation()


main()