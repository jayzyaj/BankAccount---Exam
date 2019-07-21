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
    self.user_2.firstName = 'Mina'

    self.assertEqual(self.user_1.fullname, 'John Clifford de Vera')
    self.assertEqual(self.user_2.fullname, 'Mina Chaeyoung')

if __name__ == '__main__':
    unittest.main()