import unittest
from tdd.math_operations import addition_operation


class TestMathOperations(unittest.TestCase):
    def test_addition_operation(self):
        math_addition_result = addition_operation(num_1=5, num_2=10)
        self.assertEqual(math_addition_result, 15)

if __name__ == '__main__':
    unittest.main()