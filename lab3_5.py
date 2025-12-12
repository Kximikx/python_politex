def count_numbers_not_divisible_by_five(start, end):
    count = 0  

    print(f"Діапазон від {start} до {end}:")
    print("Числа, які не діляться на 5 без остачі:", end=" ")

    num = start
    while num <= end: 
        if num % 5 != 0:   
            count += 1
            print(num, end=" ")
        num += 1

    print()
    print(f"Кількість чисел, які не діляться на 5 без остачі: {count}")
    print("-" * 40)


count_numbers_not_divisible_by_five(1, 9)
