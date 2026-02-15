import unittest

def kth_largest(nums, k):
    if k < 1:
        raise ValueError("k має бути >= 1")
    if len(nums) < k:
        raise ValueError("Розмір масиву має бути не менше k")

    used = [False] * len(nums)  # щоб не брати один і той самий елемент двічі

    current_value = None
    current_index = -1

    # k разів шукаємо наступний максимум
    for _ in range(k):
        max_value = None
        max_index = -1

        for i in range(len(nums)):
            if used[i]:
                continue

            if max_value is None or nums[i] > max_value:
                max_value = nums[i]
                max_index = i

        used[max_index] = True
        current_value = max_value
        current_index = max_index

    return current_value, current_index


class TestKthLargest(unittest.TestCase):
    def test_example_from_task(self):
        nums = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        value, index = kth_largest(nums, k)
        self.assertEqual(value, 22)
        self.assertEqual(index, 2)

    def test_k1_largest(self):
        nums = [5, 1, 10, 3]
        value, index = kth_largest(nums, 1)
        self.assertEqual(value, 10)
        self.assertEqual(index, 2)

    def test_k_equals_len(self):
        nums = [4, 2, 9]
        value, index = kth_largest(nums, 3)  # 3-й найбільший = найменший
        self.assertEqual(value, 2)
        self.assertEqual(index, 1)

    def test_invalid_k_too_large(self):
        nums = [1, 2]
        with self.assertRaises(ValueError):
            kth_largest(nums, 3)

    def test_invalid_k_zero(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            kth_largest(nums, 0)


if __name__ == "__main__":
    unittest.main()
