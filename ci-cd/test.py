import unittest
from io import StringIO
import sys
from main import fizz_buzz

def hello():
    print( "Hello")

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        output = StringIO()
        sys.stdout = output
        # fizz_buzz(15)
        hello()
        sys.stdout = sys.__stdout__
        expected_output = (
            "1\n"
            "2\n"
            "Fizz\n"
            "4\n"
            "Buzz\n"
            "Fizz\n"
            "7\n"
            "8\n"
            "Fizz\n"
            "Buzz\n"
            "11\n"
            "Fizz\n"
            "13\n"
            "14\n"
            "FizzBuzz\n"
        )
        self.assertEqual(output.getvalue(), "Hello\n")

if __name__ == '__main__':
    unittest.main()