import time
import unittest

from calculate_age.calculate import convert_age_to_days, convert_age_to_months


class TestConvertToMonthsMethod(unittest.TestCase):
  # get the number of months passed in the current year
  def current_month(self):
    return time.localtime(time.time()).tm_mon

  # unit test with payload = an int number
  def test_month_with_int(self):
    self.assertEqual(convert_age_to_months(1), 1 * 12 + self.current_month())
    self.assertEqual(convert_age_to_months(2), 2 * 12 + self.current_month())
    self.assertEqual(convert_age_to_months(4), 4 * 12 + self.current_month())
    self.assertEqual(convert_age_to_months(12), 12 * 12 + self.current_month())
    self.assertEqual(convert_age_to_months(100), 100 * 12 + self.current_month())

  # unit test with payload = a float number
  def test_month_with_float(self):
    self.assertEqual(convert_age_to_months(0.5), self.current_month())
    self.assertEqual(convert_age_to_months(4.5), 4 * 12 + self.current_month())

  # unit test with payload = 0
  def test_month_with_zero(self):
    self.assertEqual(convert_age_to_months(0), self.current_month())

  # unit test with payload = a huge number (> 256 - int)
  def test_month_with_huge_number(self):
    self.assertEqual(convert_age_to_months(999999999), 12000000000)

  # unit test with payload = a string number
  def test_month_with_string_number(self):
    self.assertEqual(convert_age_to_months('4'), 60)

  # unit test with payload = a negative number (< 0)
  def test_month_with_negative_number(self):
    self.assertTrue(convert_age_to_months(-4) < 0)
    self.assertEqual(convert_age_to_months(-0.4), 12)

  # unit test with payload = a bool type
  def test_month_with_boolean(self):
      self.assertEqual(convert_age_to_months(True), 'Not a valid age')
      self.assertEqual(convert_age_to_months(False), 'Not a valid age')

  # unit test with payload = a characters
  def test_month_with_characters(self):
    with self.assertRaises(ValueError) as cm:
      convert_age_to_months('abc')

    self.assertIn("invalid literal for int() with base 10: 'abc'", cm.exception.args)

  # unit test with no payload
  def test_month_with_no_input(self):
    with self.assertRaises(TypeError) as cm:
      convert_age_to_months()

    self.assertIn("convert_age_to_months() missing 1 required positional argument: 'age'", cm.exception.args)

  # unit test with payload = dict() value
  def test_month_with_dict(self):
    with self.assertRaises(TypeError) as cm:
      convert_age_to_months(dict())

    self.assertIn("int() argument must be a string, a bytes-like object or a number, not 'dict'", cm.exception.args)

  # unit test with payload = list() value
  def test_month_with_list(self):
    with self.assertRaises(TypeError) as cm:
      convert_age_to_months(list())

    self.assertIn("int() argument must be a string, a bytes-like object or a number, not 'list'", cm.exception.args)

  # unit test with payload = None value
  def test_month_with_none(self):
    with self.assertRaises(TypeError) as cm:
      convert_age_to_months(None)

    self.assertIn("int() argument must be a string, a bytes-like object or a number, not 'NoneType'", cm.exception.args)


#  similar to TestConvertToMonthsMethod
class TestConvertToDaysMethod(unittest.TestCase):
  def test_month_with_int(self):
    # date: 12/25/2021
    # for age(1) = 1y + days_in_current_year = 365 + 360 = 725
    self.assertEqual(convert_age_to_days(1), 725)

  # [...]


if __name__ == '__main__':
  unittest.main()