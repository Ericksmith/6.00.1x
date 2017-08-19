def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    handCount = 0
    for v in hand.values():
        handCount += v
    return(handCount)
