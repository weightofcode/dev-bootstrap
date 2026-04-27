# - The program randomly selects a word from a list of secret words.
# - The player has limited chances to guess the word.
# - When a correct letter is guessed, it is revealed in its correct position.
# - The player wins if all letters are guessed before running out of chances.
# - For simplicity, the program gives word length + 2 chances.
#   Example: If the secret word is mango (5 letters), the player gets 7 chances.


# DRAFT IDEAS
# not yet sure how to code this (need more Py documentation)
# grab the word
# split the word's chars in a 'list'
# 'hide' the chars and print them as _ , e.g.: _,_,_,_,_ (w,a,t,e,r)
# if a char is provided, check if it's in the list
#   if it is, replace the _ at the corresponding index with the character
#   TODO: handle use-case with multiple instances of the same char (aPPle)
#   display the char
# increase the counter
# etc.

# py -m pip install requests


import random
import requests


def generate_list_of_words():
    # NOTE: This may become unreliable with network issues or if website is down
    # consider random_word library (real words, not scrambled strings)
    words_wiki = "https://www.mit.edu/~ecprice/wordlist.10000"
    __r = requests.get(words_wiki)
    text_content = __r.content.decode("utf-8")  # decode raw bytes from requests
    list_of_words = text_content.splitlines()
    return list_of_words


def get_random_word():
    words = generate_list_of_words()
    random_word = random.choice(words)
    print(f"DEBUG: random_word = {random_word}")
    return random_word


def guess_random_word():
    rand_word = get_random_word()
    obfuscated_word = ["_"] * len(rand_word)  # str multiplication
    attempt = 0
    max_attempts = len(rand_word) + 2
    print(f"DEBUG3: rand_word = {rand_word}")
    print(f"DEBUG4: len(obfuscated_word) = {len(obfuscated_word)}")
    print(f"DEBUG5: obfuscated_word = {obfuscated_word}")
    while attempt < max_attempts:
        inp = input("Enter a character: ")
        attempt += 1
        print(f"DEBUG6: {attempt}")
        for i, c in enumerate(rand_word):
            if c == inp:
                obfuscated_word[i] = inp
                print(f"DEBUG7: {obfuscated_word}")
        print(f"DEBUG8: {obfuscated_word}")
    return


def greet_user():
    print("---------------------------------------------------------------------")
    username = input(
        "Who are you? ",
    )
    print("Hello", username, "!")
    print("Objective:\t Guess the word.")
    print("Gameplay:\t Guess characters.")
    print("Rules:\t\t You may guess a character (word length + 2) times.")
    print("* If you guessed the character, its position is revealed in word.")
    print("---------------------------------------------------------------------")


def main():
    greet_user()
    generate_list_of_words()
    guess_random_word()


if __name__ == "__main__":
    main()
