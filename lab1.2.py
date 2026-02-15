import unittest

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1
    pos = n - 1  # куди ставимо наступний найбільший квадрат

    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]

        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1

        pos -= 1

    return result


class TestSortedSquares(unittest.TestCase):
    def test_example_1(self):
        nums = [-4, -2, 0, 1, 3]
        expected = [0, 1, 4, 9, 16]
        self.assertEqual(sorted_squares(nums), expected)

    def test_example_2(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(sorted_squares(nums), expected)


if __name__ == "__main__":
    unittest.main()