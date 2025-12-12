def count_numbers_without_five(start, end): #Оглошення функції та вхідні данні 
    count = 0 #Присвоїня зміної 0

    for num in range(start, end + 1):# Проходить всі числа від почаьку до кінця 
        n = num #Змінна
        if n < 0: # Перевірка чи немає мінуса 
            n = -n

        has_five = False # Перевірка чи немає 5

        while n > 0: # Повторює комнди поки n буде більше 0
            digit = n % 10 # поточна цифра яку перевіряємо.
            if digit == 5:
                has_five = True # якщо найшли 5 то команда зупиняється 
                break
            n = n // 10 

        if not has_five: # Якщо тут немає 5 зараховуєм 
            count = count + 1 # Якщо  числі немає цифри 5 то збільшуєм на 1

    return count # Повернення результату 



print(count_numbers_without_five(1, 9)) # Виклик фунцкції вище яка перевііряє числа від 1 до 9     
print(count_numbers_without_five(4, 17)) # аналогічно як у 26 стрічці   
