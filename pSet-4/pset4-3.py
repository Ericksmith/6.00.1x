def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    for i in wordList:
        if i == word:
            break
    else:
        return(False)
    for char in word:
        if char not in hand:
            return(False)
        else:
            if hand.get(char) < word.count(char):
                return(False)
    return(True)
