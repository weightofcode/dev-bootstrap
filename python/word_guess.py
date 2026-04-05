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

def greet_user():
    print("-------------------------------------------")
    username = input("Who are you? ", )
    print("Hello", username)
    print("-------------------------------------------")


if __name__ == "__main__":
    greet_user()

    # ask for char from user
    # is char in word?
    #   if yes -> ask user to guess the word
    #       print the success if word is a match with random word
    #   if not -> try again and decrease try count

    char_list = []
    word = get_word_from_list()
    error_counter = 8
    word_guess = ""
    while error_counter < MAX_ALLOW_TRIES:
        print("-------------------------------------------")
        c = read_char_from_input()
        if c in word:
            print(f"The character [{c}] exits in the word!")
            char_list.append(c)
            print(f"Current guessed characters: {char_list}")
            print("Want to guess the word?")
            if word_guess:
                gw = input("Guess the word: ", )
                if word_guess == word:
                    print(f"SUCCESS! The word was: {word}")
                else:
                    print("Try again?")
                    # where do we stop? this seems almost correct
                    # TODO: fix it
        else:
            print(f"The character [{c}] does not exist in the word. Try again!")
            error_counter += 1


