import unittest
from user import User

class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print('Test Cases starting for User Module')

  @classmethod
  def tearDownClass(cls):
    print('Test Case finished for User Module')

  def setUp(self):
    self.user_1 = User('Jayz', 'de Vera', 'deverajaycee17@gmail.com')
    self.user_2 = User('Son', 'Chaeyoung', 'twice@gmail.com')

  def tearDown(self):
    print('tearDown\n')
      
  def test_email(self):
    print('Testing User should return email correctly')
    self.assertEqual(self.user_1.email, 'deverajaycee17@gmail.com')
    self.assertEqual(self.user_2.email, 'twice@gmail.com')

  def test_fullname(self):
    print('Testing User should return full name correctly')
    self.assertEqual(self.user_1.fullname, 'Jayz de Vera')
    self.assertEqual(self.user_2.fullname, 'Son Chaeyoung')

    self.user_1.firstName = 'John Clifford'

    self.user_2.firstName = 'Mi'
    self.user_2.lastName = 'Chaeng'

    self.assertEqual(self.user_1.fullname, 'John Clifford de Vera')
    self.assertEqual(self.user_2.fullname, 'Mi Chaeng')

  def test_user_open_account(self):
    print('Testing User should return bank account details correctly')
    self.user_1.open_account("Wells Fargo", 10171996, 5000)
    user_1_bank = self.user_1.bankAccount
    # Assertion test for Bank Object
    self.assertEqual(user_1_bank.name, "Wells Fargo")
    self.assertEqual(user_1_bank.accountName, "Jayz de Vera")
    self.assertEqual(user_1_bank.accountNumber, 10171996)
    self.assertEqual(user_1_bank.pin, 123456)
    self.assertEqual(user_1_bank.balance, 5000)

  def test_user_open_another_account(self):
    print('Testing User should not open a new account if it has one')
    self.user_1.open_account("Wells Fargo", 10171996, 5000)
    with self.assertRaises(ValueError):
      self.user_1.open_account("Bank of America", 10172019, 3000)

if __name__ == '__main__':
    unittest.main()