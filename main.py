from random import randint
from art import logo

winning_number = 0
guesses = 0

def random_number():
    """Generates number, to be guessed, from 1 to 100."""
    winning_number = randint(1, 100)
    return winning_number

def difficulty(game_mode):
    """Set mode to easy (10 guesses) or hard (5 guesses)"""
    if game_mode == "easy":
        guesses = 10
    else:
        guesses = 5
    return guesses

def game_play():
    print(logo)
    print("Welcome to Guess The Number!\nI'm thinking of a number from 1 to 100.")
    winning_number = random_number()
    # print(f"TESTING, winner is {winning_number}!")
    guesses = difficulty(input("Choose a difficulty, Type 'easy' or 'hard'. ").lower())
    game_over = False

    while not game_over:
        print(f"Attempts remaining to Guess The Number is {guesses}!")
        player_guess = int(input("Make a guess: "))
        if guesses == 1:
            game_over = True
            print("You are out of guesses, Game Over.")
        else:
            if player_guess == winning_number:
                game_over = True
                print("Way to Go! You Guess The Number!")
            elif player_guess > winning_number:
                print("That's too high\nGuess again.")
                guesses -= 1
            else:
                print("That's too low\nGuess again.")
                guesses -= 1

game_play()
