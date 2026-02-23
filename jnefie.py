def kth_largest(nums, k):
    if k < 1:
        raise ValueError("k має бути >= 1")

    n = len(nums)
    if n < k:
        raise ValueError("Розмір масиву має бути не менше k")

    used = [False] * n

    m = n - k + 1  # (n - k + 1)-й найменший

    current_value = None
    current_index = -1

    if k <= m:
        for _ in range(k):
            max_value = None
            max_index = -1

            for i in range(n):
                if used[i]:
                    continue
                if max_value is None or nums[i] > max_value:
                    max_value = nums[i]
                    max_index = i

            used[max_index] = True
            current_value = max_value
            current_index = max_index

        return current_value, current_index

    else:
        for _ in range(m):
            min_value = None
            min_index = -1

            for i in range(n):
                if used[i]:
                    continue
                if min_value is None or nums[i] < min_value:
                    min_value = nums[i]
                    min_index = i

            used[min_index] = True
            current_value = min_value
            current_index = min_index

        return current_value, current_index
