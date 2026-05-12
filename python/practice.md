## Number guessing game
The objective of this project is to build a simple number guessing game that 
challenges the user to identify a randomly selected number within a specified 
range. The game begins by allowing the user to define a range by entering a 
lower and an upper bound (for example, from A to B). Once the range is set, the 
system randomly selects an integer that falls within this user-defined interval. 
The user's task is then to guess the chosen number using as few attempts as 
possible. The game provides feedback after each guess, helping the user refine 
their next guess based on whether their previous attempt was too high or too 
low.

## Word guessing game
This program is a simple word-guessing game where the user has to guess the 
characters in a randomly selected word within a limited number of attempts. The 
program provides feedback after each guess, helping the user to either complete 
the word or lose the game based on their guesses. (the pool of words to guess 
from is limited, so it may be a good idea to sort them by a category that makes 
sense (fruit, money, etc.)

## Hangman game
Hangman is a classic word-guessing game. Its origins are not exactly known but
it appears to date back to Victorian times. A player writes down the first and
last letters of a word, and another player guesses the letters in between.
-- How the Game Works --
The program randomly selects a word from a list of secret words.
The player has limited chances to guess the word.
When a correct letter is guessed, it is revealed in its correct position.
The player wins if all letters are guessed before running out of chances.
For simplicity, the program gives word length + 2 chances.
Example: If the secret word is mango (5 letters), the player gets 7 chances.

## 21 Number Game
21 Number Game (also known as Bagram or Twenty Plus One) is a simple counting
game in which players take turns to count numbers from 1 to 21. The player who
calls "21" loses the game. It can be played between multiple players, but here
we demonstrate a player vs computer version using Python. 
For Example:
Player says: 1 2
Computer says: 3 4 5
Player says: 6 7
Computer says: 8 9 ...
Player says: 21

Since the Player says 21, the Player loses the game.

Game Rules
The game is played between two players who take turns one after another.
On each turn, a player can call 1 to 3 numbers.
The numbers must be consecutive (for example, 5 6 7) skipping numbers leads to
disqualification.
The counting always starts from 1 and continues upward.
The one who calls 21, loses the game.
