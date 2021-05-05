from fibonacci_seq import __version__
import unittest
from unittest import TestCase
from fibonacci_seq.fibonacci_seq import fib_num


class FibonacciTest(TestCase):

    def test_fibonaci(self):
        test_cases = [[0, 0], [1, 1], [1, 2], [2, 3], [6765, 20]]
        for i in test_cases:
            self.assertEqual(i[0], fib_num(i[1]))


if __name__ == "__main__":
    unittest.main()
