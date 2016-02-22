def Fibonacci(n):
    """
    Return the n-th value of the Fibonacci sequuence [0, 1, 1, 2, 3, 5, 8, 13, ...]
    """
    if n<2:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
