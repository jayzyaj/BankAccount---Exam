import unittest
import calc

from constants import variables
from bank_account import BankAccount

calc = calc.Math

class TestBank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
      print('Test Cases starting for Bank Module')

    @classmethod
    def tearDownClass(cls):
      print('Test Case finished for Bank Module')

    def setUp(self):
      self.user_1 = variables.user_1
      self.user_2 = variables.user_2

    def tearDown(self):
      print('tearDown\n')

    # def test_add(self):
    #     self.assertEqual(calc.add(10, 5), 15)

    # def test_subtract(self):
    #     self.assertEqual(calc.subtract(10, 5), 5)

    # def test_multiply(self):
    #     self.assertEqual(calc.multiply(10, 5), 50)

    # def test_divide(self):
    #     self.assertEqual(calc.divide(10, 5), 2)
    #     with self.assertRaises(ValueError):
    #         calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()