import unittest
from lab8 import max_wire_length


class TestMaxWireLength(unittest.TestCase):
    def test_example_1(self):
        w = 2
        h = [3, 3, 3]
        self.assertAlmostEqual(max_wire_length(w, h), 5.656854249, places=6)

    def test_example_2(self):
        w = 100
        h = [1, 1, 1, 1]
        self.assertAlmostEqual(max_wire_length(w, h), 300.0, places=6)

    def test_example_3(self):
        w = 4
        h = [100, 2, 100, 2, 100]
        self.assertAlmostEqual(max_wire_length(w, h), 396.32, places=2)

    def test_example_4(self):
        w = 4
        h = [
            56, 18, 17, 94, 23, 7, 21, 94, 29, 54,
            44, 26, 86, 79, 4, 15, 5, 91, 25, 17,
            88, 66, 28, 2, 95, 97, 60, 93, 40, 70,
            75, 48, 38, 51, 34, 52, 87, 8, 62, 77,
            35, 52, 3, 93, 34, 57, 51, 11, 39, 72
        ]
        self.assertAlmostEqual(max_wire_length(w, h), 2738.18, places=2)

    def test_empty_heights(self):
        self.assertEqual(max_wire_length(5, []), 0.0)

    def test_bad_w(self):
        with self.assertRaises(ValueError):
            max_wire_length(0, [1, 2, 3])

    def test_bad_heights(self):
        with self.assertRaises(ValueError):
            max_wire_length(2, [3, 0, 3])


if __name__ == "__main__":
    unittest.main()