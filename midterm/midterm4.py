def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    total = 0
    n = 0
    while total <= k:
        if total == k:
            return(True)
        else:
            n += 1
            total = n + total
    return(False)
