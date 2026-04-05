import unittest
from islands import islands, label_islands, island_sizes


class TestIslands(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(islands([]), 0)
        self.assertEqual(label_islands([]), (0, []))
        self.assertEqual(island_sizes([]), [])

    def test_one_cell_0(self):
        g = [[0]]
        self.assertEqual(islands(g), 0)
        self.assertEqual(label_islands(g), (0, [[0]]))
        self.assertEqual(island_sizes(g), [])

    def test_one_cell_1(self):
        g = [[1]]
        self.assertEqual(islands(g), 1)
        k, lab = label_islands(g)
        self.assertEqual(k, 1)
        self.assertEqual(lab, [[1]])
        self.assertEqual(island_sizes(g), [1])

    def test_example_5_islands_count_and_sizes(self):
        g = [
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 1, 1],
        ]
        self.assertEqual(islands(g), 5)

        k, lab = label_islands(g)
        self.assertEqual(k, 5)

        # розміри островів не залежать від того, які саме id їм дали
        s = sorted(island_sizes(g))
        self.assertEqual(s, [1, 1, 2, 3, 5])

        # усі мітки мають бути 0..k
        for row in lab:
            for x in row:
                self.assertTrue(0 <= x <= k)

    def test_diag_changes_result(self):
        g = [
            [1, 0],
            [0, 1],
        ]
        # без діагоналі це 2 острови
        self.assertEqual(islands(g), 2)
        self.assertEqual(label_islands(g, diag=False)[0], 2)

        # з діагоналлю це 1 острів
        self.assertEqual(label_islands(g, diag=True)[0], 1)

    def test_all_connected(self):
        g = [
            [1, 1],
            [1, 1],
        ]
        self.assertEqual(islands(g), 1)
        self.assertEqual(island_sizes(g), [4])


if __name__ == "__main__":
    unittest.main()