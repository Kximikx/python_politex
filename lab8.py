import math  # підключаємо math для математичних функцій


def max_wire_length(w, max_heights):  # функція рахує максимально можливу довжину дроту
    if w <= 0:  # якщо відстань некоректна
        raise ValueError("w має бути > 0")  # кидаємо помилку
    if not max_heights:  # якщо список висот порожній
        return 0.0  # дріт не потрібен

    n = len(max_heights)  # кількість опор
    if any(h < 1 for h in max_heights):  # якщо є некоректна максимальна висота
        raise ValueError("усі max_heights мають бути >= 1")  # кидаємо помилку

    max_h = max(max_heights)  # найбільша можлива висота серед усіх опор
    neg_inf = float("-inf")  # значення для "недосяжного" стану

    dp_prev = [neg_inf] * (max_h + 1)  # dp для попередньої опори

    for h in range(1, max_heights[0] + 1):  # всі можливі висоти першої опори
        dp_prev[h] = 0.0  # довжина до першої опори = 0

    for i in range(1, n):  # йдемо по опорах з другої до останньої
        dp_cur = [neg_inf] * (max_h + 1)  # dp для поточної опори

        for h in range(1, max_heights[i] + 1):  # висота поточної опори
            best = neg_inf  # найкраще значення для цієї висоти
            for hp in range(1, max_heights[i - 1] + 1):  # висота попередньої опори
                if dp_prev[hp] == neg_inf:  # якщо попередній стан недосяжний
                    continue  # пропускаємо
                seg = math.hypot(w, h - hp)  # довжина між опорами
                val = dp_prev[hp] + seg  # загальна довжина
                if val > best:  # беремо максимум
                    best = val
            dp_cur[h] = best  # записуємо максимум

        dp_prev = dp_cur  # переходимо до наступної опори

    ans = max(dp_prev[1 : max_heights[-1] + 1])  # максимум для останньої опори
    return float(ans)  # повертаємо відповідь


def solve():  # читання вводу і друк відповіді
    w = int(input().strip())  # відстань між опорами
    max_heights = list(map(int, input().split()))  # максимальні висоти опор
    ans = max_wire_length(w, max_heights)  # рахуємо відповідь
    print(f"{ans:.2f}")  # друк з 2 знаками після коми


if __name__ == "__main__":  # запуск напряму
    solve()  # виклик solve()