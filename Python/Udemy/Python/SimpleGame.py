import random


result = 0


def start_game():

    num_list = list(range(10))
    random.shuffle(num_list)
    global  result
    result = num_list[:3]
    print (result)
    start_guess()


def start_guess():

    print(""" Welcome to the simple game.  
            1. The computer will think of 3 digit number that has no repeating digits.
            2. You will then guess a 3 digit number
            3. The computer will then give back clues, the possible clues are:
            

            Close: You've guessed a correct number but in the wrong position
            Match: You've guessed a correct number in the correct position
            Nope: You haven't guess any of the numbers correctly

            Based on these clues you will guess again until you break the code with a
            perfect match! """)


    guess_count = 0


    while(True):

        try:

            print("\n")
            guess = input(" Please enter a 3 digit number without repetition : ")

            guess_count+=1

            # This check is required for python 2 and 3 compatibility
            if (type(guess) is int):
                guess = str(guess)

            guess_list = list(map(int, guess))

            print (guess_list)

            for number in guess_list:
                if number in result:
                    if (result.index(number) == guess_list.index(number)):
                        print("__Match__",end=" ")
                        if("".join([str(x) for x in result]) == "".join([str(x) for x in guess_list])):
                            print("\n")
                            print(" Congratulations!!!!!You have guessed the number right... ")
                            print(" You found the right number in {} guesses ".format(guess_count))
                            return
                    else:
                        print("__Close__",end=" "),

                else:
                    print("No match")

        except KeyboardInterrupt:
            pass















start_game()