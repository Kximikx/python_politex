def count_numbers_without_five(start, end):  # Оголошення функції та вхідні дані
    count = 0  # Присвоєння змінної 0

    print(f"Діапазон від {start} до {end}:")  # показує діапазон
    print("Числа без цифри 5:", end=" ")

    for num in range(start, end + 1):  # Проходить всі числа від початку до кінця
        n = num  # Копія числа
        if n < 0:  # Перевірка чи немає мінуса
            n = -n

        has_five = False  # Початково вважаємо, що 5 немає

        while n > 0:  # Повторює команди поки n більше 0
            digit = n % 10  # поточна цифра, яку перевіряємо
            if digit == 5:
                has_five = True  # якщо знайдена 5, припиняємо перевірку
                break
            n = n // 10

        if not has_five:  # Якщо в числі немає цифри 5
            count = count + 1  # додаємо до лічильника
            print(num, end=" ")  # виводимо число на екран

    print()  # перенос рядка після списку чисел
    print(f"Кількість чисел без 5: {count}")
    print("-" * 40)  # роздільна лінія між результатами
    return count  # Повернення результату


# Виклик функції
count_numbers_without_five(1, 9)
count_numbers_without_five(4, 17)
