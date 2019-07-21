import unittest
import calc

from user import User
from bank_account import BankAccount

class TestBank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
      print('Test Cases starting for Bank Module')

    @classmethod
    def tearDownClass(cls):
      print('Test Case finished for Bank Module')

    def setUp(self):
      self.user_1 = User('Jayz', 'de Vera', 'deverajaycee17@gmail.com')
      self.user_2 = User('Son', 'Chaeyoung', 'twice@gmail.com')

    def tearDown(self):
      print('tearDown\n')

    def test_withdraw(self):
      user_1_bank = self.user_1.bankAccount
      self.assertIsNone(user_1_bank)

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