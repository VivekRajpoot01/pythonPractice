# Number guessing game
# I have to create a number guessing game where the user have to guess a number between 1 to 10 and
# the program will tell that the number you guessed is right or wrong.
import random

guess_count = 0
guess_limit = 3
rand_no = random.randint(0,9)
while(guess_count<guess_limit):
    guess = int(input("Guess a number between 1 to 10: "))
    #guess_count += 1
    if(rand_no == guess):
        print("Guessed Number is correct")
        guess_count += 1
        break
    else:
        print("Sorry!! You failed in guessing the number")
        guess_count += 1



print("Correct number was: ", rand_no)
