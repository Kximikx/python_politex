class Node:  # вузол AVL
    def __init__(self, value, priority, key):  # створення вузла
        self.value = value  # значення
        self.priority = priority  # пріоритет
        self.key = key  # ключ для сортування

        self.left = None  # лівий син
        self.right = None  # правий син
        self.h = 1  # висота вузла


class AvlPriorityQueue:  # черга з пріоритетами на AVL
    def __init__(self):  # конструктор
        self.root = None  # корінь дерева
        self._seq = 0  # лічильник для однакових пріоритетів
        self._n = 0  # кількість елементів

    def __len__(self):  # len(q)
        return self._n  # повертає розмір

    def push(self, value, priority: int):  # вставка в чергу
        key = (int(priority), -self._seq)  # робимо унікальний ключ
        self._seq += 1  # збільшуємо лічильник
        self.root = self._ins(self.root, value, int(priority), key)  # вставляємо в AVL
        self._n += 1  # збільшуємо розмір

    def peek(self):  # подивитись максимум
        if self.root is None:  # якщо порожньо
            raise IndexError("peek from empty priority queue")  # помилка
        m = self._leftmost(self.root)  # шукаємо найвищий пріоритет
        return m.value, m.priority  # повертаємо без видалення

    def pop(self):  # дістати максимум
        if self.root is None:  # якщо порожньо
            raise IndexError("pop from empty priority queue")  # помилка
        m = self._leftmost(self.root)  # беремо вузол з максимумом
        self.root = self._del(self.root, m.key)  # видаляємо його
        self._n -= 1  # зменшуємо розмір
        return m.value, m.priority  # повертаємо значення і пріоритет

    def _h(self, n):  # висота вузла
        return n.h if n else 0  # 0 якщо None

    def _upd(self, n):  # оновити висоту
        n.h = 1 + max(self._h(n.left), self._h(n.right))  # рахуємо висоту

    def _bf(self, n):  # баланс фактор
        return self._h(n.left) - self._h(n.right)  # ліва - права

    def _rot_r(self, y):  # правий поворот
        x = y.left  # беремо лівого
        t2 = x.right  # зберігаємо піддерево
        x.right = y  # робимо y правим
        y.left = t2  # повертаємо t2 вліво
        self._upd(y)  # оновлюємо висоту y
        self._upd(x)  # оновлюємо висоту x
        return x  # новий корінь

    def _rot_l(self, x):  # лівий поворот
        y = x.right  # беремо правого
        t2 = y.left  # зберігаємо піддерево
        y.left = x  # робимо x лівим
        x.right = t2  # повертаємо t2 вправо
        self._upd(x)  # оновлюємо висоту x
        self._upd(y)  # оновлюємо висоту y
        return y  # новий корінь

    def _reb(self, n):  # балансування вузла
        self._upd(n)  # оновлюємо висоту
        b = self._bf(n)  # рахуємо баланс

        if b > 1:  # перекіс вліво
            if self._bf(n.left) < 0:  # ліво-правий випадок
                n.left = self._rot_l(n.left)  # спочатку лівий поворот
            return self._rot_r(n)  # потім правий поворот

        if b < -1:  # перекіс вправо
            if self._bf(n.right) > 0:  # право-лівий випадок
                n.right = self._rot_r(n.right)  # спочатку правий поворот
            return self._rot_l(n)  # потім лівий поворот

        return n  # якщо все ок

    def _ins(self, n, value, priority, key):  # вставка в піддерево
        if n is None:  # якщо місце порожнє
            return Node(value, priority, key)  # створюємо вузол

        if key > n.key:  # якщо пріоритет вищий
            n.left = self._ins(n.left, value, priority, key)  # йдемо вліво
        else:  # інакше
            n.right = self._ins(n.right, value, priority, key)  # йдемо вправо

        return self._reb(n)  # балансуємо

    def _leftmost(self, n):  # знайти максимум (найлівіший)
        cur = n  # старт
        while cur.left is not None:  # поки є лівий
            cur = cur.left  # йдемо вліво
        return cur  # повертаємо вузол

    def _del(self, n, key):  # видалення по ключу
        if n is None:  # якщо порожньо
            return None  # нічого

        if key > n.key:  # ключ більший
            n.left = self._del(n.left, key)  # видаляємо вліво
        elif key < n.key:  # ключ менший
            n.right = self._del(n.right, key)  # видаляємо вправо
        else:  # знайшли вузол
            if n.left is None:  # нема лівого
                return n.right  # повертаємо правого
            if n.right is None:  # нема правого
                return n.left  # повертаємо лівого

            s = self._leftmost(n.right)  # беремо заміну з правого піддерева
            n.value, n.priority, n.key = s.value, s.priority, s.key  # копіюємо дані
            n.right = self._del(n.right, s.key)  # видаляємо дубль

        return self._reb(n) if n else None  # балансуємо і повертаємо