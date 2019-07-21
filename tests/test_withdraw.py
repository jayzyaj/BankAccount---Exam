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

    def test_withdraw_correct_amount(self):
      print('Testing Bank Module withdraw should return correct amount')
      self.user_1.open_account("Wells Fargo", 10171996, 5000)
      user_1_bank = self.user_1.bankAccount

      self.assertEqual(user_1_bank.withdraw(3000), 3000)
      self.assertEqual(user_1_bank.withdraw(1000), 1000)
      with self.assertRaises(ValueError):
        user_1_bank.withdraw(-2323)
      self.assertEqual(user_1_bank.balance, 1000)

    def test_withdraw_correct_remaining_balance(self):
      print('Testing Bank Module withdraw should return correct remaining balance')
      self.user_1.open_account("Wells Fargo", 10171996, 5000)
      user_1_bank = self.user_1.bankAccount

      user_1_bank.withdraw(3000.00) # 5000 - 3000 = 2000
      user_1_bank.withdraw(959.63) # 2000 - 959.63 = 1000
      self.assertEqual(user_1_bank.balance, 1040.37)

    def test_withdraw_more_than_current_balance_with_no_agreed_overdraft(self):
      print('Testing Bank Module withdraw amount more than balance that has no agreed overdraft')
      self.user_1.open_account("Wells Fargo", 10171996, 5000)
      user_1_bank = self.user_1.bankAccount

      with self.assertRaises(ValueError):
        user_1_bank.withdraw(8000)

    def test_withdraw_more_than_current_balance_with_agreed_overdraft(self):
      print('Testing Bank Module withdraw amount more than balance that has no agreed overdraft')
      self.user_1.open_account("Wells Fargo", 10171996, 5000)
      user_1_bank = self.user_1.bankAccount

      user_1_bank.applyAgreedOverdraft()
      user_1_bank.withdraw(4000) # 5000 - 4000 = 1000
      user_1_bank.withdraw(3000) # 1000 - 3000 = -2000
      self.assertEqual(user_1_bank.balance, -2000)

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