def startUp(secretWord):
    '''
    secretWord: string, the secret word to guess.
    return: no return, prints the opening statments of the game.

    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = []
    startUp(secretWord)
    while guesses > 0 and isWordGuessed(secretWord, lettersGuessed) is False:
        print("-------------")
        print("You have", guesses, "left")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        guessThisRound = input("Please guess a letter:")
        guessInLowerCase = guessThisRound.lower()
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif guessInLowerCase in secretWord:
            lettersGuessed.append(guessInLowerCase)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guessInLowerCase)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
    if guesses == 0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secretWord)
    else:
        print("-------------")
        print("Congratulations, you won!")         
