import unittest
from run import evaluate, conv_ans, val_inputs

class TestConvert(unittest.TestCase):
	def test_correct(self):
		inputs = [1,4,3,6]
		res = {
			"1": 1,
			"4": 2,
			"3": 3,
			"6": 4
		}
		self.assertEqual(conv_ans(inputs), res)

class TestEvaluate(unittest.TestCase):
	def test_correct(self):
		ans = [2, 0, 4, 8]
		guess = "2048"
		self.assertEqual(evaluate(guess, ans), [4, 0])

	def test_one_a(self):
		ans = [2, 0, 4, 8]
		guess = "2179"
		self.assertEqual(evaluate(guess, ans), [1, 0])

	def test_two_b(self):
		ans = [2, 0, 4, 8]
		guess = "9214"
		self.assertEqual(evaluate(guess, ans), [0, 2])

if __name__ == '__main__':
    unittest.main()