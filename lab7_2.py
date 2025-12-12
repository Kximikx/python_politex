from collections import deque

queue = deque(["Олег", "Марія", "Іван", "Софія", "Андрій"])

print("""
        1 – додати покупця
        2 – обслужити покупця
        3 – показати чергу
        4 – вихід
        """)

while True:
    choice = input("твій вибір: ")

    if choice == "1":
        name = input("ім'я покупця: ")
        queue.append(name)
        print(f"покупець {name} став у чергу")


    elif choice == "2":
        if len(queue) == 0:
            print("черга порожня")
        else:
            served = queue.popleft()
            print("обслуговано покупця:", served)

    elif choice == "3":
        if len(queue) == 0:
            print("черга порожня")
        else:
            print("поточна черга:")
            for i, person in enumerate(queue):
                print(f"{i + 1} - {person}")

    elif choice == "4":
        print("роботу завершено")
        break

    else:
        print("щось не так")