import random


# - The program randomly selects a word from a list of secret words.
# - The player has limited chances to guess the word.
# - When a correct letter is guessed, it is revealed in its correct position.
# - The player wins if all letters are guessed before running out of chances.
# - For simplicity, the program gives word length + 2 chances.
#   Example: If the secret word is mango (5 letters), the player gets 7 chances.



def populate_list_of_words():
    # define a static list of words
    # perhaps use a random word generator
    # with API from a dedicated site?
    return list_of_words

def get_word():
    # grab a random word from list_of_words
    return random_word

def display_word(word):
    # code?
    return list_of_chars_in_word



def greet_user():
    print("---------------------------------------------------------------------")
    username = input("Who are you? ", )
    print("Hello", username, "!")
    print("Objective:\t Guess the word.")
    print("Gameplay:\t Guess characters.")
    print("Rules:\t\t You may guess a character (word length + 2) times.")
    print("* If you guessed the character, its position is revealed in word.")
    print("---------------------------------------------------------------------")





def main():
    return 0

if __name__ == "__main__":
    main()
