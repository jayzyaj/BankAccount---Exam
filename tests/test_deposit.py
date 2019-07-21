import unittest

from user import User
from bank_account import BankAccount

class TestBankDeposit(unittest.TestCase):
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

    def test_deposit_correct_amount(self):
      print('Testing Bank Module deposit should return correct amount')
      self.user_1.open_account("Bank of America", 10171996, 100)
      user_1_bank = self.user_1.bankAccount

      self.assertEqual(user_1_bank.deposit(2550.68), 2550.68)
      self.assertEqual(user_1_bank.deposit(492.05), 492.05)
      with self.assertRaises(ValueError):
        user_1_bank.withdraw(-2323)
      with self.assertRaises(ValueError):
        user_1_bank.withdraw(-0.23)
      self.assertEqual(user_1_bank.displayBalance, 'Your current balance is: 3142.73')


if __name__ == '__main__':
    unittest.main()