class Hangman:

    wordArray = []

    def __init__(self, word):
        self.word = word
        self.wordLength = len(word) - 1
        self.wrongGuesses = 0
        self.wordArray = []
        self.wrongGuessArray = []

    def startGame(self, array):
        #Starts game. Draws initial board. Fills array with blank lines indicated number of letters
        print("==========\n"
              "||      ||\n"
              "||\n"
              "||\n"
              "||\n"
              "=====\n")
        for x in range(self.wordLength):
            array.insert(x, "_")

        print(array)

    def checkGuess(self, letter, word):
        # Checks user guess. Makes sure its only one character. Adds letter to either the word array or
        # the wrong guess array and determines if you've won.
        if len(letter) > 1:
            print("Only a single letter. Try again")
        else:
            if letter in word:
                i = self.word.index(letter)
                self.wordArray.pop(i)
                self.wordArray.insert(i, letter)

                # Word length variable is only used for initial startup of game.
                # Here I use it for tracking how close to winning the user is.
                self.wordLength -= 1

                if self.wordLength == 0:
                    print("The word is: " + self.word.upper())
                    print("You WIN!")
                    exit()

            elif letter not in word:
                self.wrongGuessArray.insert(self.wrongGuesses, letter)
                self.wrongGuesses += 1


    def redrawBoard(self):
        #Redraws the board based on how many wrong guesses were made
        if self.wrongGuesses == 1:
            print("==========\n"
                  "||      ||\n"
                  "||      O\n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "=====\n")

        elif self.wrongGuesses == 2:
            print("==========\n"
                  "||      ||\n"
                  "||      O\n"
                  "||     /\n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "=====\n")

        elif self.wrongGuesses == 3:
            print("==========\n"
                  "||      ||\n"
                  "||      O\n"
                  "||     /|\n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "=====\n")

        elif self.wrongGuesses == 4:
            print("==========\n"
                  "||      ||\n"
                  "||      O\n"
                  "||     /|\ \n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "=====\n")

        elif self.wrongGuesses == 5:
            print("==========\n"
                  "||      ||\n"
                  "||      O\n"
                  "||     /|\ \n"
                  "||      |\n"
                  "||\n"
                  "||\n"
                  "=====\n")

        elif self.wrongGuesses == 6:
            print("==========\n"
                  "||      ||\n"
                  "||      O\n"
                  "||     /|\ \n"
                  "||      |\n"
                  "||     /\n"
                  "||\n"
                  "=====\n")

        elif self.wrongGuesses == 7:
            print("==========\n"
                  "||      ||\n"
                  "||      O\n"
                  "||     /|\ \n"
                  "||      |\n"
                  "||     / \ \n"
                  "||\n"
                  "=====\n"
                  "You LOSE!")
            exit()

        else:
            print("==========\n"
                  "||      ||\n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "||\n"
                  "=====\n")
        print(self.wordArray)
        print("\nWrong Letters:")
        print(self.wrongGuessArray)


import random
file = open('word.txt', 'r')

# Loads entire file the picks random line from file.
secretWord = random.choice(file.readlines())
newGame = Hangman(secretWord)

newGame.startGame(newGame.wordArray)

while newGame.wrongGuesses < 7:
    userGuess = input("Guess a letter...\n")
    newGame.checkGuess(userGuess, secretWord)
    newGame.redrawBoard()


file.close()