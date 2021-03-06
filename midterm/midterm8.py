def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def secondFunc(x):
        total = 0
        listLength = len(L)-1
        for i in L:
            total += i * x**listLength
            listLength -= 1
        return(total)
    return secondFunc
