import time
import unittest
from calculate import convert_days, convert_months

class TestConvertToMonthsMethod(unittest.TestCase):
  def current_month(self):
    return time.localtime(time.time()).tm_mon


  def test_month_with_int(self):
    self.assertEqual(convert_months(1), 1 * 12 + self.current_month())
    self.assertEqual(convert_months(2), 2 * 12 + self.current_month())
    self.assertEqual(convert_months(4), 4 * 12 + self.current_month())
    self.assertEqual(convert_months(12), 12 * 12 + self.current_month())
    self.assertEqual(convert_months(100), 100 * 12 + self.current_month())


  def test_month_with_float(self):
    self.assertEqual(convert_months(0.5), self.current_month())
    self.assertEqual(convert_months(4.5), 4 * 12 + self.current_month())


  def test_month_with_zero(self):
    self.assertEqual(convert_months(0), self.current_month())


  def test_month_with_huge_number(self):
    self.assertEqual(convert_months(999999999), 12000000000)


  def test_month_with_number_string(self):
    self.assertEqual(convert_months('4'), 60)


  def test_month_with_negative_number(self):
    self.assertTrue(convert_months(-4) < 0)
    self.assertEqual(convert_months(-0.4), 0)


  def test_month_with_boolean(self):
      self.assertEqual(convert_months(True), 'Not a valid age')


  def test_month_with_characters(self):
    with self.assertRaises(ValueError) as cm:
      convert_months('abc')

    self.assertIn("invalid literal for int() with base 10: 'abc'", cm.exception.args)


  def test_month_with_no_input(self):
    with self.assertRaises(TypeError) as cm:
      convert_months()

    self.assertIn("convert_months() missing 1 required positional argument: 'age'", cm.exception.args)


  def test_month_with_dict(self):
    with self.assertRaises(TypeError) as cm:
      convert_months(dict())

    self.assertIn("int() argument must be a string, a bytes-like object or a number, not 'dict'", cm.exception.args)


  def test_month_with_list(self):
    with self.assertRaises(TypeError) as cm:
      convert_months(list())

    self.assertIn("int() argument must be a string, a bytes-like object or a number, not 'list'", cm.exception.args)


  def test_month_with_none(self):
    with self.assertRaises(TypeError) as cm:
      convert_months(None)

    self.assertIn("int() argument must be a string, a bytes-like object or a number, not 'NoneType'", cm.exception.args)


# class TestConvertToDaysMethod(unittest.TestCase):
#   def test_day_with_int(self):
#     self.assertEqual(convert_days(4), 60)

#   def test_day_with_float(self):
#     self.assertEqual(convert_days(4.5), 60)

#   def test_day_with_zero(self):
#     self.assertEqual(convert_days(0), 60)

#   def test_day_with_huge_number(self):
#     self.assertEqual(convert_days(999999999), 60)

#   def test_day_with_negative_number(self):
#     self.assertEqual(convert_days(-4), 60)

#   def test_day_with_no_input(self):
#     self.assertEqual(convert_days(), 60)

#   def test_day_with_number_string(self):
#     self.assertEqual(convert_days('4'), 60)

#   def test_day_with_characters(self):
#     self.assertEqual(convert_days('abc'), 60)

#   def test_day_with_dict(self):
#     self.assertEqual(convert_days(dict()), 60)

#   def test_day_with_list(self):
#     self.assertEqual(convert_days(list()), 60)

#   def test_day_with_none(self):
#     self.assertEqual(convert_days(None), 60)

#   def test_day_with_boolean(self):
#     self.assertEqual(convert_days(True), 60)

#   def test_day_in_unhappy(self):
#     self.assertFalse(convert_days(None), 60)

if __name__ == '__main__':
  unittest.main()