def selection_sort_desc(row): 
    n = len(row) 
    for i in range(n): 
        max_index = i 
        for j in range(i + 1, n): 
            if row[j] > row[max_index]:
                max_index = j 
        row[i], row[max_index] = row[max_index], row[i] 
    return row

def sort_matrix_rows(matrix):
    sorted_matrix = []
    for row in matrix:
        new_row = selection_sort_desc(row[:])  
        sorted_matrix.append(new_row)
    return sorted_matrix

def compute_fi(matrix):
    n = len(matrix) 
    m = len(matrix[0]) 

    fi_values = []

    for j in range(m): 
        summa = 0 
        count = 0 
        for i in range(n): 
            if i + j < n - 1: 
                summa += matrix[i][j] 
                count += 1 
        if count > 0:
            fi = summa / count 
            fi_values.append(fi) 
        else:
            fi_values.append(0) 
    return fi_values 


def compute_F(fi_values):
    result = 1
    for value in fi_values:
        result *= value
    return result

if __name__ == "__main__":
    A = [
        [33, -5, -9, -20, -11],
        [0, -42, 86, 83, 71],
        [-6, -9, 33, 13, 22],
        [52, -5, -7, 53, 19],
        [-3, 98, 72, 68, 0],
    ]

    sorted_A = sort_matrix_rows(A) 

    fi_values = compute_fi(sorted_A) 

    F_value = compute_F(fi_values) 

    print("Відсортована матриця:")
    for row in sorted_A:
        print(row)

    print("\nЗначення fi(aij):")
    for i, val in enumerate(fi_values):
        print("fi стовпця", i, "=", val)

    print("\nЗначення F(fi(aij)) =", F_value)
