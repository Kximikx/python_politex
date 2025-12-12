start = 1
end = 9

count = 0  # Лічильник чисел без цифри 5

print(f"Діапазон від {start} до {end}:")
print("Числа без цифри 5:", end=" ")

num = start  # Початкове число

while num <= end:  # Поки не досягнемо кінця діапазону
    n = num
    if n < 0:
        n = -n

    has_five = False  # Перевірка на наявність цифри 5

    while n > 0:
        digit = n % 10
        if digit == 5:
            has_five = True
            break
        n = n // 10

    if not has_five:  # Якщо цифри 5 немає
        count = count + 1
        print(num, end=" ")

    num = num + 1  # Переходимо до наступного числа

print()
print(f"Кількість чисел без 5: {count}")
print("-" * 40)
