from fibonacci_seq import __version__
import unittest
from unittest import TestCase
from fibonacci_seq.fibonacci_seq import sum_fib_seq


class FibonacciTest(TestCase):

    def test_fibonnaci(self):
        self.assertEqual(0, sum_fib_seq(0))


if __name__ == "__main__":
    unittest.main()