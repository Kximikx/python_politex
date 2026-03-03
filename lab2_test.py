import unittest
from lab2_banana import min_k


class T(unittest.TestCase):
    def test_1(self):
        a = [3, 6, 7, 11]
        h = 8
        self.assertEqual(min_k(a, h), 4)

    def test_2(self):
        a = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(min_k(a, h), 30)

    def test_3(self):
        a = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(min_k(a, h), 23)


if __name__ == "__main__":
    unittest.main()