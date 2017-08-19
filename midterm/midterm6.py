def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    L.sort()
    answer = None
    for i in L:
        count = 1
        indexCount = 1
        while len(L) > L.index(i) + indexCount  and i == L[L.index(i) + indexCount]:
            count += 1
            indexCount += 1
        if count%2 != 0:
            answer = i
    return(answer)
