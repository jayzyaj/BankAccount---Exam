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
      self.assertEqual(formatMoney(13.949999999999999), 13.95)

if __name__ == '__main__':
    unittest.main()