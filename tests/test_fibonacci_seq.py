from fibonacci_seq import __version__
import unittest
from unittest import TestCase
from fibonacci_seq.fibonacci_seq import sum_fib_seq


class FibonacciTest(TestCase):

    def test_fibonaci(self):
        test_cases = [[0,0], [1,1]]
        for i in test_cases:
            self.assertEqual(i[0], sum_fib_seq(i[1]))


if __name__ == "__main__":
    unittest.main()
