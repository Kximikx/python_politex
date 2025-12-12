def selection_sort_desc(row): # сортує один рядок матриці за спаданням від більшого до меншого
    n = len(row) # Отримаємо довжину рядка тобто скільки елемнтів в ньому 
    for i in range(n): # Шукаєм позицію куди потрібно поставити най більший елемент
        max_index = i # Вважаємо що на даному кроці найбільший елемент знаходиться на позиції i
        # j перебирає елементи з права на ліво 
        for j in range(i + 1, n): #Шукаємо реальний максимальний елемент серед усіх, що праворуч від i
            if row[j] > row[max_index]:# Якщо поточний елемент більший за той який ми вважаємо максимальним то найшли максимум 
                max_index = j # Оновлюємо індекс максимального елемента
        row[i], row[max_index] = row[max_index], row[i] # міняємо його місцями з елементом на позиції
    return row

# Сорвтування кожного рядка за спаданням використовуючи selection_sort_desc і формує нвоу матрицю 
def sort_matrix_rows(matrix):
    sorted_matrix = []
    for row in matrix:
        new_row = selection_sort_desc(row[:])  
        sorted_matrix.append(new_row)
    return sorted_matrix

# потрібно щоб правильно проходити матрицю в циклах.
def compute_fi(matrix):
    n = len(matrix) # Висота 
    m = len(matrix[0]) # ширина 

    fi_values = []

    for j in range(m): # Якщо матриця має 5 стовіпців цикл виконується 5 раз  
        summa = 0 # суму елементів
        count = 0 # скільки елементів ми додали
        for i in range(n): # Тепер ми перебираємо всі елементи у цьому стовпці j  зверху вниз
            if i + j < n - 1: # перевірка чи знаходиться елемент над побічною діагоналлю
                summa += matrix[i][j] # Якщо елемент знаходиться над побічною діагоналлю  додаємо його до суми
                count += 1 # рахуєм скільки елементів  взяли
        if count > 0:
            fi = summa / count # знайти середнє акрфметичне 
            fi_values.append(fi) # Записуємо знайдене fi у список
        else:
            fi_values.append(0) # Якщо над діагоналлю елементів не було записуємо 0
    return fi_values # Повертаємо список усіх знайдених fi

# Функція compute_F перемножує всі значення fi збережені у списку fi_values і вертає відповідь 
def compute_F(fi_values):
    result = 1
    for value in fi_values:
        result *= value
    return result


A = [
    [33, -5, -9, -20, -11],
    [0, -42, 86, 83, 71],
    [-6, -9, 33, 13, 22],
    [52, -5, -7, 53, 19],
    [-3, 98, 72, 68, 0]
]

sorted_A = sort_matrix_rows(A) #иклик функції sort_matrix_rows

fi_values = compute_fi(sorted_A) # у функцію compute_fi передається відсортована матриця

F_value = compute_F(fi_values) # підсумкове значення функції F яке дорівнює добутку всіх fi

print("Відсортована матриця:")
for row in sorted_A:
    print(row)

print("\nЗначення fi(aij):")
for i, val in enumerate(fi_values):
    print("fi стовпця", i, "=", val)

print("\nЗначення F(fi(aij)) =", F_value)
