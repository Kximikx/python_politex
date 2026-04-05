import unittest
from lab3_2_3 import BinaryTree, invert_binary_tree


def ser(t):
    if t is None:
        return [None]
    return [t.v] + ser(t.l) + ser(t.r)


class TestInvert(unittest.TestCase):
    def test_example(self):
        r = BinaryTree(1)
        r.l = BinaryTree(2)
        r.r = BinaryTree(3)
        r.l.l = BinaryTree(4)
        r.l.r = BinaryTree(5)
        r.r.l = BinaryTree(6)
        r.r.r = BinaryTree(7)

        inv = invert_binary_tree(r)

        e = BinaryTree(1)
        e.l = BinaryTree(3)
        e.r = BinaryTree(2)
        e.l.l = BinaryTree(7)
        e.l.r = BinaryTree(6)
        e.r.l = BinaryTree(5)
        e.r.r = BinaryTree(4)

        self.assertEqual(ser(inv), ser(e))

    def test_one(self):
        r = BinaryTree(10)
        self.assertEqual(ser(invert_binary_tree(r)), [10, None, None])

    def test_none(self):
        self.assertIsNone(invert_binary_tree(None))


if __name__ == "__main__":
    unittest.main()