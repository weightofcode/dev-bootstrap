# Word guessing game

import random

# REQ from PRJ
# - Import random
# - Getting the User's Name, and Greeting the User
# - List of Words and Choosing a Random Word
# - Prompting the User to Guess
# - The Main Game Loop
#     Checking Each Character in the Word
#     has the user won?
#     prompt next guess
#     handle incorrect guess
#     check if user has lost
#     end


MAX_ALLOW_TRIES = 8

def define_word_list():
    words_to_pick_from = [
            "apple", "orange", "banana", "kiwi", "pear", "plum", "pineapple", 
            "grapes", "cherry"
            ]
    return words_to_pick_from

def get_word_from_list():
    word_list = define_word_list()
    word = random.choice(word_list)
    return word

def read_char_from_input():
    char = input("Enter a character: ", )
    return char

def keep_track_of_counter(counter, max_tries_allowed):
    if counter < max_tries_allowed:
        counter += 1
        print(f"Number of attempts: {counter} / {max_tries_allowed}")
    else:
        pass
    if counter == max_tries_allowed:
        print(f"Max number of attempts reached.")
        print(f"Game over! Better luck next time!")
    else:
        pass
    return counter

def greet_user():
    print("----------------------------------------------------------------")
    username = input("Who are you? ", )
    print("Hello", username, "!")
    print("Objective:\t Guess the word.")
    print("Gameplay:\t Guess characters.")
    print("Rules:\t\t You may guess a char 8 times.")
    print("* If you guessed the character, you may guess the word.")
    print("* Leave blank if you do not want to guess the word.")
    print("----------------------------------------------------------------")


def main():
    greet_user()

    char_list = []
    word = get_word_from_list()
    try_counter = 0

    while try_counter < MAX_ALLOW_TRIES:
        print("----------------------------------------------------------------")
        c = read_char_from_input()

        if c in word:
            print(f"The character [{c}] exists in the word.")
            if c not in char_list:
                char_list.append(c)
            else:
                print("Character already in guessed.")
            print(f"Current guessed characters: {char_list}")
            try_counter = keep_track_of_counter(try_counter, MAX_ALLOW_TRIES)

            print("----------------------------------------------------------------")
            word_guess = input("Guess the word. Leave blank if not want to guess: ", )
            if word_guess == word:
                print(f"SUCCESS! The word was: {word}")
                return
            else:
                print("Not guessing or wrong guess. Back to guessing characters.")
        else:
            print(f"The character [{c}] does not exist in the word.")
            try_counter = keep_track_of_counter(try_counter, MAX_ALLOW_TRIES)
            if try_counter < MAX_ALLOW_TRIES:
                print("Try again.")


if __name__ == "__main__":
    main()
