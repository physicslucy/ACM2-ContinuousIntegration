def test_fibonacci():
    """
    In this function we import file fibonacci.py and test the function inside it, Fibonacci(n) against known values
    """

    import fibonacci as fb
    assert fb.Fibonacci(10) == 55
    assert fb.Fibonacci(5) == 5
