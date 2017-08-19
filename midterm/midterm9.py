def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) == 0 or len(L2) == 0:
        if len(L1) == len(L2):
            return(None, None, None)
        else:
            return(False)
    if len(L1) != len(L2):
        return(False)
    freqeuntVar = ()
    mostCommon = 0
    for element in L1:
        if element in L2:
            if L2.count(element) == L1.count(element):
                if L2.count(element) > mostCommon:
                    freqeuntVar = element
                    mostCommon = L2.count(element)
            else:
                return(False)
    answer = (freqeuntVar, L2.count(freqeuntVar), type(freqeuntVar))
    return(answer)
