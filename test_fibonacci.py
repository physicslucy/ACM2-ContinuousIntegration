import unittest

class FibTest(unittest.TestCase):

    def test_fibonacci(self):
        """
        In this function we import file fibonacci.py and test the function inside it, Fibonacci(n) against known values
        """

        import fibonacci as fb
        assert fb.Fibonacci(10) == 55
        assert fb.Fibonacci(5) == 5


    def test_Fib_throws_exception(self):
        import fibonacci as fb
        self.assertRaises(ValueError, fb.Fibonacci, -5)
