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
    self.assertEqual(convert_age_to_months(999999999), 11999999989)

  # unit test with payload = a string number
  def test_month_with_string_number(self):
    self.assertEqual(convert_age_to_months('4'), 49)

  # unit test with payload = a negative number (< 0)
  def test_month_with_negative_number(self):
    self.assertTrue(convert_age_to_months(-4) < 0)
    self.assertEqual(convert_age_to_months(-0.4), 1)

  # unit test with payload = a bool type
  def test_month_with_boolean(self):
    with self.assertRaises(ValueError) as cm:
      convert_age_to_months(False)

    self.assertIn("Not a valid age", cm.exception.args)

  # unit test with payload = a characters
  def test_month_with_characters(self):
    with self.assertRaises(ValueError) as cm:
      convert_age_to_months('abc')

    self.assertIn("Not a valid age", cm.exception.args)

  # unit test with no payload
  def test_month_with_no_input(self):
    with self.assertRaises(TypeError) as cm:
      convert_age_to_months()

    self.assertIn("convert_age_to_months() missing 1 required positional argument: 'age'", cm.exception.args)

  # unit test with payload = dict() value
  def test_month_with_dict(self):
    with self.assertRaises(ValueError) as cm:
      convert_age_to_months(dict())

    self.assertIn("Not a valid age", cm.exception.args)

  # unit test with payload = list() value
  def test_month_with_list(self):
    with self.assertRaises(ValueError) as cm:
      convert_age_to_months(list())

    self.assertIn("Not a valid age", cm.exception.args)

  # unit test with payload = None value
  def test_month_with_none(self):
    with self.assertRaises(ValueError) as cm:
      convert_age_to_months(None)

    self.assertIn("Not a valid age", cm.exception.args)


#  similar to TestConvertToMonthsMethod
class TestConvertToDaysMethod(unittest.TestCase):
  def test_day_with_int(self):
    pass
    # date: 12/25/2021
    # for age(1) = 1y + days_in_current_year = 365 + 360 = 725
    # self.assertEqual(convert_age_to_days(1), 725)

  # [...]


if __name__ == '__main__':
  unittest.main()