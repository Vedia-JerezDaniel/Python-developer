while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if number <= 0:
        break
    
# guess.py

from random import randint

LOW, HIGH = 1, 5
secret_number = randint(LOW, HIGH)
clue = ""

while True:
    guess = input(f"Guess a number between {LOW} and {HIGH} {clue} ")
    number = int(guess)
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    else:
        print(f"You guessed it! The secret number is {number}")
        break
    

def process_move(clue):
    user_input = input(f"Guess a number between {LOW} and {HIGH} {clue} ")
    number = int(user_input)
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    return number, clue

number, clue = process_move(clue)  # First iteration

while number != secret_number:
    number, clue = process_move(clue)
else:
    print(f"You guessed it! The secret number is {number}")