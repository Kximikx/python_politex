from Lablelvel import kth_largest

def rint(p):
    while True:
        try:
            return int(input(p).strip())
        except ValueError:
            print("Введи ціле число.")

def read_st():
    n = rint("Скільки студентів? ")
    while n <= 0:
        print("Кількість має бути > 0")
        n = rint("Скільки студентів? ")

    st = []
    for i in range(n):
        print("\nСтудент", i + 1)
        nm = input("Ім'я: ").strip()
        sr = input("Прізвище: ").strip()
        sc = rint("Бал: ")
        st.append({"n": nm, "s": sr, "p": sc})
    return st

def kth_st(st, k):
    arr = [x["p"] for x in st]
    val, idx = kth_largest(arr, k)
    return st[idx], val, idx

if __name__ == "__main__":
    st = read_st()

    k = rint("\nЯкий по рахунку найбільший бал знайти? ")
    while k < 1 or k > len(st):
        print("Неправильне k")
        k = rint("Введи k ще раз: ")

    x, val, idx = kth_st(st, k)

    print("\nРезультат:")
    print(f"{k}-й найбільший бал: {val}")
    print(f"Студент: {x['n']} {x['s']}")
    print(f"Індекс: {idx}")