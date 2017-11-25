from list import *
import unittest

class unitTestList(unittest.TestCase):

	def test_isEmptyList(self):
		self.assertEqual(EmptyList().isEmptyList(), True)
		self.assertEqual(EmptyList().add(Integer(3)).isEmptyList(), False)
		self.assertTrue(not EmptyList().add(Integer(7)).isEmptyList())
		self.assertFalse(EmptyList().add(Integer(7)).isEmptyList())
		self.assertFalse(Integer(5).isEmptyList())

	def test_tail(self):
		self.assertTrue(EmptyList().add(Integer(4)).tail().isEmptyList())
		self.assertFalse(EmptyList().add(Integer(17)).add(Integer(9)).tail().isEmptyList())
		self.assertTrue(EmptyList().add(Integer(17)).add(Integer(9)).tail().tail().isEmptyList())

	def test_value(self):
		self.assertEqual(Integer(3).value(), 3)
		self.assertNotEqual(Integer(3), 3)

	def test_head(self):
		self.assertTrue(EmptyList().add(Integer(17)).add(Integer(9)).head().value() == 9)
		self.assertFalse(EmptyList().add(Integer(17)).add(Integer(9)).head().value() == 17)

if __name__ == '__main__':
	unittest.main()