class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedQueue:
    def __init__(self, initial=None):
        self.head = None
        self.tail = None
        self._size = 0

        if initial:
            for item in initial:
                self.enqueue(item)

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:  
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:  
            self.tail = None
        self._size -= 1
        return value

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

if __name__ == "__main__":
    queue = SinglyLinkedQueue(["Олег", "Марія", "Іван", "Софія", "Андрій"])

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
            queue.enqueue(name)
            print(f"покупець {name} став у чергу")

        elif choice == "2":
            served = queue.dequeue()
            if served is None:
                print("черга порожня")
            else:
                print("обслуговано покупця:", served)

        elif choice == "3":
            if queue.is_empty():
                print("черга порожня")
            else:
                print("поточна черга:")
                for i, person in enumerate(queue, start=1):
                    print(f"{i} - {person}")

        elif choice == "4":
            print("роботу завершено")
            break

        else:
            print("щось не так")
