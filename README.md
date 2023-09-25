# Python Practice Repository

## Overview

Welcome to the Python Practice repository! This repository is a space for you to explore, learn, and practice Python programming through various projects. The initial project in this repository is a simple number guessing game. You can use this as a template to add more practice projects and build your Python skills.

## How to Use

1. **Clone this repository to your local machine:**

   ```
   git clone https://github.com/VivekRajpoot01/pythonPractice.git


## Project 1: Number Guessing Game

**Description:** The number guessing game allows the user to guess a random number between 1 and 10. The program provides feedback on whether the guess was correct or not and limits the user to three attempts.

**How to Play:**

1. Run the Python script in your preferred Python environment.

2. You will be prompted to enter a number between 1 and 10. Enter your guess and press Enter.

3. If your guess matches the randomly generated number, you win the game, and the program will display "Guessed Number is correct."

4. If your guess does not match the random number, the program will display "Sorry!! You failed in guessing the number."

5. You will have a total of 3 attempts to guess the correct number.

6. After you have made your guesses, the program will reveal the correct number.

7. The game will end, and you can choose to play again or exit the program.


## Project 2: Simple Car Game

### Overview

The Simple Car Game is a basic Python program that takes user input to control a virtual car. Depending on the user's input, the program will simulate various car-related actions, such as starting, stopping, or quitting the game.

### How to Play

1. Run the Python script in your preferred Python environment.

2. You will be prompted to enter a command. You can enter the following commands:

   - `help`: Displays a list of available commands.
   - `start`: Starts the car and displays a message.
   - `stop`: Stops the car and displays a message.
   - `quiet`: Quits the game.

3. The program will respond according to your input:

   - If you enter `help`, it will display a list of commands.
   - If you enter `start`, it will simulate starting the car.
   - If you enter `stop`, it will simulate stopping the car.
   - If you enter any other input, it will display a message indicating that it doesn't understand the command.

4. The game will continue until you enter `quiet` to exit.

### Code Explanation

```python
inp = input()
command = ""

while command != "quiet":
    if inp == "help":
        print("start -> to start the car")
        print("stop -> to stop the car")
        print("quiet -> to quit from this game")
    elif inp == "start":
        print("Car Started.... Ready to run on the Road!!")
    elif inp == "stop":
        print("Car Stopped... Sorry!! It can't run anymore")
    else:
        print("I don't understand this..")

    inp = input()

