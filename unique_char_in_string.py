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

def is_string_unique_char(s):
  """ check if string contains only unique char, does not use any extra data structure but O(n^2) """
  if s is None: return False
  for i, j in enumerate(s):
    if ord(j) > 127: raise ValueError("char %s out of range" % j)  
    for k in xrange(i, len(s) - 1):
      if k + 1 < len(s) and s[k + 1] == j: return False
  return True    

class TestUniqueStringArray(unittest.TestCase):

  def testNoneValue(self):
    self.assertFalse(is_string_unique_char_array(None))
    self.assertFalse(is_string_unique_char(None))

  def testEmptyString(self):
    self.assertTrue(is_string_unique_char_array(''))
    self.assertTrue(is_string_unique_char(''))

  def testRepeatingChar(self):
    self.assertFalse(is_string_unique_char_array('aabcdef'))
    self.assertFalse(is_string_unique_char('aabcdef'))

  def testRepeatingCharEnd(self):
    self.assertFalse(is_string_unique_char_array("abcdefga"))
    self.assertFalse(is_string_unique_char("abcdefga"))

  def testUniqueCharString(self):
    self.assertTrue(is_string_unique_char_array("abcde12345"))
    self.assertTrue(is_string_unique_char("abcde12345"))

  def testStringNotASCII(self):
      with self.assertRaises(ValueError):
        is_string_unique_char_array('カタカナ')
        is_string_unique_char('カタカナ')

if __name__ == '__main__':
  unittest.main()

