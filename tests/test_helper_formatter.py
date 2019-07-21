import unittest

from helpers import formatter

formatMoney = formatter.formatMoney

class TestHelperFormatter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
      print('Test Cases starting for Helpers / Formatter')

    @classmethod
    def tearDownClass(cls):
      print('Test Case finished for Helpers / Formatter')

    def tearDown(self):
      print('tearDown\n')

    def test_should_return_correct_monetary_value(self):
      print('Testing Helper / Formatter / Formatting of Correct monetary value')
      self.assertEqual(formatMoney(13.949999999999999), 13.95)
      self.assertEqual(formatMoney(14.22222223), 14.22)
      self.assertEqual(formatMoney(2.16), 2.16)
      self.assertEqual(formatMoney(0.99334), 0.99)

if __name__ == '__main__':
    unittest.main()