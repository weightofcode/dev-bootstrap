

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
    list_of_words = __r.content.splitlines()
    # print(f"DEBUG: list_of_words = {list_of_words}")
    return list_of_words

def get_random_word():
    words = generate_list_of_words()
    random_word = random.choice(words)
    print(f"DEBUG: random_word = {random_word}")
    return random_word

# def obfuscate_random_word():
#     random_word = get_random_word()
#     obfuscated_word = ""
#     # for c in range(len(random_word)):
#     #     obfuscated_word[c].replace(f"{c}", "_")
#     for c in random_word:
#         obfuscated_word = random_word.replace(c, "_")
#         print(f"c = {c}")
#     print(f"DEBUG: obfuscated_word = {obfuscated_word}")
#     return obfuscated_word

def obfuscate_random_word():
    random_word = get_random_word()
    obfuscated_word = ""
    for c in random_word:
        obfuscated_word += '_, '
    print(f"DEBUG: obfuscated_word = {obfuscated_word}")
    return obfuscated_word

def guess_random_word():
    obfuscated_word = obfuscate_random_word()
    attempt = 0
    max_attempts = len(obfuscated_word) + 2
    # maybe use while:
    for c in range(len(max_attempts)):
        i = input("Enter a character: ")
        if i == c.exists(obfuscated_word):
            # locate c in word and assign the value provided by the user
            obfuscated_word[c].replace(i)
            print(f"DEBUG: {i}")
        # print it
    # return list_of_chars_in_word

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
    generate_list_of_words()
    obfuscate_random_word() # already includes get_random_word()
    # guess_random_word()
    return 0

if __name__ == "__main__":
    main()
