#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

def is_string_unique_char_array(s):
  """ only support ASCII, use extra array of 128 chars for this version"""
  char_counts = [0] * 128
  if s is None: return False
  for i in s:
    i_ord = ord(i)
    if i_ord > 127:
        raise ValueError("char %s out of range" % i)
    char_counts[i_ord] += 1
    if char_counts[i_ord] > 1:
      return False
  return True

class TestUniqueStringArray(unittest.TestCase):

  def testNoneValue(self):
    self.assertFalse(is_string_unique_char_array(None))

  def testEmptyString(self):
    self.assertTrue(is_string_unique_char_array(''))

  def testRepeatingChar(self):
    self.assertFalse(is_string_unique_char_array('aabcdef'))

  def testRepeatingCharEnd(self):
    self.assertFalse(is_string_unique_char_array("abcdefga"))

  def testUniqueCharString(self):
    self.assertTrue(is_string_unique_char_array("abcde12345"))

  def testStringNotASCII(self):
      with self.assertRaises(ValueError):
        is_string_unique_char_array('カタカナ')

if __name__ == '__main__':
  unittest.main()

