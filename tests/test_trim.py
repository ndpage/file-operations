import unittest
import trim.trim as trim

class TrimTests(unittest.TestCase):
  def test_equal(self):
    self.assertEqual(trim.file('test1.txt'),'test1.txt')
  
  def test_simple(self):
    self.assertEqual(trim.file('test1 (2017-23-23).txt'),'test1.txt')
  
  def test_wspace(self):
    self.assertEqual(trim.file('test  1.txt'),'test  1.txt')
  
  def test_paren(self):
    self.assertEqual(trim.file('test (1) (2017-23-23jfasdlkjflsdf).txt'),'test (1).txt')


if __name__ == '__main__':
    unittest.main()