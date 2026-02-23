from Lablelvel import kth_largest
import unittest

# Тести щоб поняти чи програа прцює правильно 
class TestKthLargest(unittest.TestCase):
    def test_example_from_task(self):
        nums = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        value, index = kth_largest(nums, k) # фУНКЦІЯ 
        self.assertEqual(value, 22) # перевіряєм значення 
        self.assertEqual(index, 2)  # перевіряєм іендекс 

     # Перевірка для k = 1
    def test_k1_largest(self):
        nums = [5, 1, 10, 3]
        value, index = kth_largest(nums, 1)
        self.assertEqual(value, 10)
        self.assertEqual(index, 2)

    # Перевірка коли k дорівнює довжині масиву
    def test_k_equals_len(self):
        nums = [4, 2, 9]
        value, index = kth_largest(nums, 3)  
        self.assertEqual(value, 2)
        self.assertEqual(index, 1)

    # Помилка якщо k бліьше чим елементів в масиві 
    def test_invalid_k_too_large(self):
        nums = [1, 2]
        with self.assertRaises(ValueError):
            kth_largest(nums, 3)
    
    # Помилка k = 0
    def test_invalid_k_zero(self):
        nums = [1, 2, 3]
        with self.assertRaises(ValueError):
            kth_largest(nums, 0)