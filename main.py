import random
from hangman_art import game_stages, logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)

#make a list with blanks from the randomly selected letter
display = []
for letter in range(len(chosen_word)):
    display.append("_")

#check the player's guess against the word and replace blanks in the list with correct guesses
game_state = True

lives = 6
#make a list of past guesses so the player doesn't get punshied for repeated guesses
guesses = []

while game_state == True:
    guess = input("Guess a letter\n").lower()
    
    skip = False
    
    if guess in guesses:
        skip = True

    position = 0
    for letter in chosen_word:
        if letter == guess:
            display[position] = guess
            position += 1
        else:
            position += 1

    if skip == True:
        print(f"You've already guessed '{guess}'. Try again")
        skip = False
        guesses.append(guess)
    elif guess not in display:
        lives -= 1
        guesses.append(guess)
        if lives == 0:
            game_state = False
            print(game_stages[0])
            print(f"The word was, '{chosen_word}'. You lose.")
        else:
            print(game_stages[lives])
            print(f"{' '.join(display)}")
            print(f"You guessed '{guess}'. That is not part of the chosen word")
    elif "_" not in display:
        game_state = False
        print(f"{' '.join(display)}")
        print("You've won!")
    else:
        print(game_stages[lives])
        print(f"{' '.join(display)}")
        guesses.append(guess)