# Word guessing game

import random

# define the list of words to guess from
# pick a random word from the list
# define the allowed number of retries
# read chars from input and inform the user if they are part of the word or not
# etc


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
    char = input("Enter a character:", )
    return char

def keep_track_of_counter(counter, max_tries_allowed):
    if counter <= max_tries_allowed:
        counter += 1
        print(f"Number of tries: {counter} out of {max_allow_tries}")
    else:
        printf(f"Max tries reached: {counter} out of {max_tries_allowed}.")
        printf(f"Game over! Better luck next time!")
    return counter

def greet_user():
    print("----------------------------------------------------------------")
    username = input("Who are you? ", )
    print("Hello", username)
    print("Objective: guess the word.")
    print("Gameplay: Guess characters.")
    print("If you guessed the character, attempt to guess the word")
    print("Leave blank if you do not want to guess the word.")
    print("Rules: You may guess a char 8 times. Word guess does not count.")
    print("----------------------------------------------------------------")


def main():
    greet_user()

    # ask for char from user
    # is char in word?
    #   if yes -> ask user to guess the word
    #       print the success if word is a match with random word
    #   if not -> try again and decrease try count

    char_list = []
    word = get_word_from_list()
    print(f"DEBUG = word: ", word)
    try_counter = 0
    while try_counter <= MAX_ALLOW_TRIES:
        print("----------------------------------------------------------------")
        c = read_char_from_input()
        print(f"DEBUG = c: ", c)

        if c in word:
            print(f"The character [{c}] exists in the word.")
            if c not in char_list:
                char_list.append(c)
            else:
                print("Character already in guessed.")
            print(f"Current guessed characters: {char_list}")

            # TODO: Handle try_counter >= MAX_ALLOW_TRIES
            # try_counter += 1
            # print(f"Number of tries: {try_counter} out of {MAX_ALLOW_TRIES}")
            keep_track_of_counter(try_counter, MAX_ALLOW_TRIES)
            print("----------------------------------------------------------------")
            word_guess = input("Guess the word. Leave blank if not want to guess: ", )
            if word_guess == word:
                print(f"SUCCESS! The word was: {word}")
                return
            else:
                print("Skipped guessing the word. Back to guessing characters.")
        else:
            print(f"The character [{c}] does not exist in the word. Try again.")
            # try_counter += 1
            # print(f"Number of tries: {try_counter} out of {MAX_ALLOW_TRIES}")



if __name__ == "__main__":
    main()
