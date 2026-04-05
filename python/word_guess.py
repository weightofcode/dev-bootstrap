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


if __name__ == "__main__":

    username = input("Who are you?", )
    print("Hello", username)
