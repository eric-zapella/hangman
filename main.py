from sources import logo, stages
import os
import random

from word_list import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_wrong_letters = []

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

print(logo)
print(" ".join(display))


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls')
    if guessed_wrong_letters:
        print(
            f"wrong letters: {' '.join(guessed_wrong_letters).upper()}")
        print('--------------------------')

    if guess in display or guess in guessed_wrong_letters:
        print(f"You've already guessed {guess.upper()}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        if guess not in guessed_wrong_letters:
            print(f"nope, {guess.upper()} is not in the word :/")
            lives -= 1
            guessed_wrong_letters.append(guess)
        if lives == 0:
            os.system('cls')
            end_of_game = True
            print("GAME OVER")
            print('--------------------------')
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
