import unittest
import calc

from user import User
from bank_account import BankAccount

class TestBankWithdrawal(unittest.TestCase):
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

    def test_close_account_no_overdraft_fees(self):
      print('Testing Bank Module close account that has no overdraft fees')
      self.user_1.open_account("Wells Fargo", 10171996, 5000)
      user_1_bank = self.user_1.bankAccount

      self.assertEqual(user_1_bank.withdraw(3000), 3000)
      self.assertEqual(user_1_bank.withdraw(1000), 1000)
      with self.assertRaises(ValueError):
        user_1_bank.withdraw(-2323)
      self.assertEqual(user_1_bank.balance, 1000)
      
      self.user_1.close_account()
      self.assertIsNone(self.user_1.bankAccount)

    def test_close_account_with_overdraft_fees(self):
      print('Testing Bank Module close account with overdraft fees')
      self.user_1.open_account("Wells Fargo", 10171996, 5000.00)
      user_1_bank = self.user_1.bankAccount

      user_1_bank.applyAgreedOverdraft()
      user_1_bank.withdraw(4000.00) # 5000 - 4000 = 1000
      user_1_bank.withdraw(3000.12) # 1000 - 3000 = -2000
      self.assertEqual(user_1_bank.displayBalance, 'Your current balance is: -2000.12')
      
      with self.assertRaises(ValueError):
        self.user_1.close_account()

if __name__ == '__main__':
    unittest.main()