# Edinburgh College Quiz
# Adrian Sanchez Rodriguez - EC1939656
# 31/05/2021

# Import random library to generate random numbers
import random
# Import the students, questions and answers from the information.py file.
from information import storedstudents, storedanswers, storedquestions

# Create two list to store the students that have been saved or trapped inside.
savedstudents = []
trappedstudents = []
# Output a presentation for the user
print("Welcome to the Edinburgh College Quiz.")
# Store the value of the lists from information.py in new lists for this file.
students = storedstudents
questions = storedquestions
answers = storedanswers

# While there is still students in the list, keep running the loop
while len(students) > 0:
    # Select random student and question slots, the value for the question will also be used for the answer
    # since they have relative positions in their respective list.
    randomqa = random.randint(0, len(questions) - 1)
    randomstudent = random.randint(0, len(students) - 1)
    # Store the student in a temporary variable for later use in the student re-selection.
    temprandomstudent = randomstudent
    # While the question hasn't been answered, keep running the loop
    while True:
        # Print the question and the student that must answer it, ask the student if they want to play or pass.
        print("The question is: ", questions[randomqa], " for the student: ", students[randomstudent],
              ". Do you want to play or pass? (please type play/pass)")
        # Wait for student input
        choice = input().lower()
        # If they input play, then the game starts
        if choice == "play":
            # Ask for the answer to the student
            useranswer = input("Please enter your answer: ")

            # If the student's answer matches the information from the answer list
            if useranswer.lower() == answers[randomqa].lower():
                # Output that the student is correct
                print("Correct! Student ", students[randomstudent],
                      "is saved and the question has been removed.")
                # If there is more questions in the list
                if len(questions) > 0:
                    # Output a continue message
                    print("Up to the next one!")
                # If there is none, break the loop
                else:
                    break
                # Delete the answered question and its answer from their lists
                del questions[randomqa]
                del answers[randomqa]
                # add the student to the saved students list
                savedstudents.append(students[randomstudent])
                # delete the student from the player list and break the loop to start a new question
                del students[randomstudent]
                break
            # If the student answer doesn't match the answer from the list
            else:
                # Output a wrong answer message
                print("Wrong answer. The student couldn't be saved.")
                # If there are no more students in the list, break the loop
                if len(students) == 0:
                    break
                # If there are more students, pick another student
                else:
                    # While the new random student is the same as the previous student, keep picking a random number
                    while temprandomstudent == randomstudent:
                        temprandomstudent = random.randint(0, len(students) - 1)
                    # Add the student to the trapped student list
                    trappedstudents.append(students[randomstudent])
                    # Delete the student from the player list
                    del students[randomstudent]
                    # Assign the new random student to the previous student variable
                    randomstudent = temprandomstudent
        # If the user input is pass, check if there are more students to play or not
        elif choice == "pass":
            # If there are no more students in the list, output a message and make the same student play again
            if len(students) == 1:
                print("You're the last student, you can't escape from this.")
            # If there are more students, pick another student
            else:
                while temprandomstudent == randomstudent:
                    temprandomstudent = random.randint(0, len(students) - 1)
                randomstudent = temprandomstudent
        # If the student input doesn't match play or pass, output a wrong input message and make the user try again.
        else:
            print("Wrong input. Please try again.")

# If there are remaining students, the class has lost the game
# output a loose message with the trapped and saved students
if len(trappedstudents) > 0:
    print("Gotcha! You lost this match. The students still trapped inside are:", trappedstudents, " and: ",
          savedstudents, " managed to escape!")
# If there are no remaining students in the student list, the class has won the game.
# Output a win message with the winners
else:
    print("Congratulations! You've beaten this match. You won't be so lucky next time... Students that escaped are: ",
          savedstudents)
