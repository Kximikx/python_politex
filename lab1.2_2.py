import unittest

def kth_largest(nums, k): # Прийнятя двох функцій nums список чисел k яке за велечиною число треьа знайти 
    # k не може бути меншим за 1
    # Якщо k неправильне програма зупиняється і вимводитьс япомсилка 
    if k < 1:
        raise ValueError("k має бути >= 1")
    # Перевіряємо, чи в масиві достатньо елементів.
    if len(nums) < k:
        raise ValueError("Розмір масиву має бути не менше k")

    used = [False] * len(nums) # Створення списку used з значаенням False 

    # Зберігання лементів None пусто -1 індекса немає 
    current_value = None
    current_index = -1

    # пошук максимуму k разів щоб найти най більший k 
    for _ in range(k):
        # Зберігаємо поточний елемент 
        max_value = None
        max_index = -1
        
        # Перебираєм всі масиви nums якщо елемент використали пропускаєм його
        for i in range(len(nums)):
            if used[i]:
                continue
            
            # Оновлюєм максимум і запам'ятовуємо його індекс
            if max_value is None or nums[i] > max_value:
                max_value = nums[i]
                max_index = i
        # Позначаєм знайджений індекс як знайдений щоб не використовувати його знов 
        used[max_index] = True
        # Запам'ятовуєм значення та його індекс 
        current_value = max_value
        current_index = max_index

    # Повертаєм k найбільший елемент і його індекс у масив
    return current_value, current_index

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


if __name__ == "__main__":
    unittest.main()
