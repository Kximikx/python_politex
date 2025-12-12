def bubble_sort(customers): #Створюється функція bubble_sort
    n = len(customers) # Кількість елемнтів в списку customers 
    for i in range(n - 1): # після кожного повного проходу по списку один найбільший елемент займає свою кінцеву позицію
        for j in range(n - i - 1): # порівнюється меншbq елемент бо найбільший уже сплив в кінець списку
            if customers[j][1] > customers[j + 1][1]: # Якщо час поточного більший ніж наступного  треба міняти їх місцями
                customers[j], customers[j + 1] = customers[j + 1], customers[j] # Елементи міняються місцями щоб менший час піднімався вгору списку
    return customers 


customers = [
    ("Олег", 5),
    ("Марія", 2),
    ("Іван", 9),
    ("Андрій", 1),
    ("Софія", 4)
]

print("Початковий список покупців:")
for c in customers:
    print(c)

# Сортуємо за часом прибуття
sorted_customers = bubble_sort(customers)

print("\nПокупці, відсортовані методом бульбашки (за часом прибуття):")
for c in sorted_customers:
    print(c)

# Моделюємо обслуговування
print("\nОбслуговування покупців у порядку прибуття:")
for customer in sorted_customers:
    print("Обслуговано:", customer[0])
