def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in abc:
        if i in lettersGuessed:
            abc = abc.replace(i, "")
    return(abc) 
