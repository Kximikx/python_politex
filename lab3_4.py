def count_numbers_without_five(start, end):
    count = 0  

    print(f"Діапазон від {start} до {end}:")
    print("Числа без цифри 5:", end=" ")

    num = start
    while num <= end: 
        n = num if num >= 0 else -num  
        has_five = False
        while n > 0 and not has_five: 
            if n % 10 == 5:
                has_five = True
            n //= 10
        if not has_five:  
            count += 1
            print(num, end=" ")
        num += 1

    print()
    print(f"Кількість чисел кратних 5: {count}")
    print("-" * 40)


count_numbers_without_five(1, 9)
