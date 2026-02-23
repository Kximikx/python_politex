import unittest

def extreme(nums, t, used, find_max):
    current_value = None
    current_index = -1

    for _ in range(t):
        best_value = None
        best_index = -1

        for i in range(len(nums)):
            if used[i]:
                continue

            if best_value is None:
                best_value = nums[i]
                best_index = i
            else:
                if find_max:
                    if nums[i] > best_value:
                        best_value = nums[i]
                        best_index = i
                else:
                    if nums[i] < best_value:
                        best_value = nums[i]
                        best_index = i

        used[best_index] = True # Позначення заданого елемента як використаног 
        current_value = best_value
        current_index = best_index

    return current_value, current_index


def kth_largest(nums, k):
    if k < 1:
        raise ValueError("k має бути >= 1")
    if len(nums) < k:
        raise ValueError("Розмір масиву має бути не менше k")

    n = len(nums)
    m = n - k + 1
    used = [False] * n

    if k <= m:
        return extreme(nums, k, used, True)
    else:
        return extreme(nums, m, used, False)

if __name__ == "__main__":
    nums = [15, 7, 22, 9, 36, 2, 42, 18]
    k = 3
    value, index = kth_largest(nums, k)
    print(f"Вхідний масив: {nums} Задане k: {k} Знайдений {k}-й найбільший елемент: {value} "
          f"Позиція {k}-го найбільшого елемента в масиві: {index}")
    unittest.main()
