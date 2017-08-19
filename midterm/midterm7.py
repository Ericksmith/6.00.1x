def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    newDict = {}
    for k, v in d.items():
        newDict[v] = newDict.get(v, [])
        newDict[v].append(k)
        newDict[v] = sorted(newDict[v])
    return(newDict)
