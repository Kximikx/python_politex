import unittest
from lab4 import AvlPriorityQueue


class TestAvlPriorityQueue(unittest.TestCase):
    def test_push_peek_pop_order(self):
        q = AvlPriorityQueue()
        q.push("a", 3)
        q.push("b", 1)
        q.push("c", 5)
        q.push("d", 2)

        self.assertEqual(q.peek(), ("c", 5))
        self.assertEqual(q.pop(), ("c", 5))
        self.assertEqual(q.pop(), ("a", 3))
        self.assertEqual(q.pop(), ("d", 2))
        self.assertEqual(q.pop(), ("b", 1))
        self.assertEqual(len(q), 0)

    def test_equal_priorities_fifo(self):
        q = AvlPriorityQueue()
        q.push("x1", 10)
        q.push("x2", 10)
        q.push("x3", 10)

        self.assertEqual(q.pop(), ("x1", 10))
        self.assertEqual(q.pop(), ("x2", 10))
        self.assertEqual(q.pop(), ("x3", 10))

    def test_peek_no_remove(self):
        q = AvlPriorityQueue()
        q.push(1, 4)
        q.push(2, 9)

        self.assertEqual(q.peek(), (2, 9))
        self.assertEqual(len(q), 2)
        self.assertEqual(q.peek(), (2, 9))

    def test_pop_empty(self):
        q = AvlPriorityQueue()
        with self.assertRaises(IndexError):
            q.pop()

    def test_peek_empty(self):
        q = AvlPriorityQueue()
        with self.assertRaises(IndexError):
            q.peek()

    def test_many_operations(self):
        q = AvlPriorityQueue()
        data = [(i, i % 7) for i in range(100)]
        for v, p in data:
            q.push(v, p)

        top = q.peek()
        self.assertEqual(top[1], 6)

        last_p = 10**9
        while len(q) > 0:
            _, p = q.pop()
            self.assertLessEqual(p, last_p)
            last_p = p


if __name__ == "__main__":
    unittest.main()