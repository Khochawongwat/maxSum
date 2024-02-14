import unittest
from maxsum import maxSubArraySum

class TestMaxSubArraySum(unittest.TestCase):
    def test_maxSubArraySum(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr)-1), 15)

        arr = [2, 3, 4, 5, 7]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr) - 1), 21)

        arr = [-2, -3, 4, -1, -2, 1, 5, -3]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr)-1), 7)

        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr)-1), -1)

        arr = [5]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr)-1), 5)
        
        arr = [0, -1, 2, -1, 3, -2, 4]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr)-1), 6)

        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr)-1), 6)

        arr = [2, -3, 4, -1, -2, 1, 5, -3]
        self.assertEqual(maxSubArraySum(arr, 0, len(arr)-1), 7)

if __name__ == '__main__':
    unittest.main()