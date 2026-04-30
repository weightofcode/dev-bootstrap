# - The program randomly selects a word from a list of secret words.
# - The player has limited chances to guess the word.
# - When a correct letter is guessed, it is revealed in its correct position.
# - The player wins if all letters are guessed before running out of chances.
# - For simplicity, the program gives word length + 2 chances.


import random
import requests


def generate_list_of_words():  # >>>>
    # NOTE: This may become unreliable with network issues or if website is down
    # consider random_word library (real words, not scrambled strings)
    words_wiki = "https://www.mit.edu/~ecprice/wordlist.10000"
    __r = requests.get(words_wiki)
    text_content = __r.content.decode("utf-8")  # decode raw bytes from requests
    list_of_words = text_content.splitlines()
    return list_of_words
# <<<<

def get_random_word(list_of_words):  # >>>>
    random_word = random.choice(list_of_words)
    print(f"DEBUG: random_word = {random_word}")
    return random_word
# <<<<

def obfuscate_word(rand_word):  # >>>>
    obfuscated_word = ["_"] * len(rand_word)
    return obfuscated_word
# <<<<

# TODO:
# Should the user have a chance to guess the word?
# Display explicit failure message

def guess_random_word(rand_word, obfuscated_word):  # >>>>
    attempt = 0
    max_attempts = len(rand_word) + 2
    chars_to_guess = len(rand_word)
    print(f"DEBUG3: rand_word = {rand_word}")
    print(f"DEBUG4: len(obfuscated_word) = {len(obfuscated_word)}")
    print(f"DEBUG5: obfuscated_word = {obfuscated_word}")
    while attempt < max_attempts:
        inp = input("Enter a character: ")
        attempt += 1
        print(f"INFO: Attempt:\t\t {attempt}. Attempts left: {max_attempts - attempt}")
        for i, c in enumerate(rand_word):
            if c == inp:
                obfuscated_word[i] = inp
                chars_to_guess -= 1
                print(f"DEBUG6: chars_to_guess = {chars_to_guess}")
                # TODO: Fix success condition: works incorrectly in case 
                # multiple chars are guessed with the same input value
                if chars_to_guess == 0:
                    print("SUCCESS!\t You guessed the word!")
                    return
        print(f"WORD TO GUESS:\t {obfuscated_word}")
        print("---------------------------------------------------------------------")
    return
# <<<<

def greet_user():  # >>>>
    print("---------------------------------------------------------------------")
    username = input("Who are you? ")
    print("Hello", username, "!")
    print("Objective:\t Guess the word.")
    print("Gameplay:\t Guess characters.")
    print("Rules:\t\t You may guess a character (word length + 2) times.")
    print("* If you guessed the character, its position is revealed in word.")
    print("---------------------------------------------------------------------")
# <<<<

def main():  # >>>>
    # Hello
    greet_user()
    # Generate the data
    m_word_list = generate_list_of_words()
    m_random_word = get_random_word(m_word_list)
    m_obf_word = obfuscate_word(m_random_word)
    # Use the data
    guess_random_word(m_random_word, m_obf_word)


if __name__ == "__main__":
    main()
# <<<<

# vim: fmr=>>>>,<<<< fdm=marker
