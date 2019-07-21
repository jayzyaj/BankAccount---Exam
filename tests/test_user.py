import unittest
from constants import variables

class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print('Test Cases starting for User Module')

  @classmethod
  def tearDownClass(cls):
    print('Test Case finished for User Module')

  def setUp(self):
    self.user_1 = variables.user_1
    self.user_2 = variables.user_2

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
    self.user_2.firstName = 'Mina'

    self.assertEqual(self.user_1.fullname, 'John Clifford de Vera')
    self.assertEqual(self.user_2.fullname, 'Mina Chaeyoung')

  def test_user_open_account(self):
    self.user_1.open_account("Wells Fargo", 10171996, 5000)
    user_1_bank = self.user_1.bankAccount
    self.assertEqual(user_1_bank.name, "Wells Fargo")
    self.assertEqual(user_1_bank.accountName, "John Clifford de Vera")
    self.assertEqual(user_1_bank.accountNumber, 10171996)
    self.assertEqual(user_1_bank.pin, 123456)
    self.assertEqual(user_1_bank.balance, 5000)
    self.assertEqual(user_1_bank.agreedOverdraft, False)

if __name__ == '__main__':
    unittest.main()