import unittest
from lab6 import check_delivery


class TestGasDelivery(unittest.TestCase):
    def test_all_ok(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipes = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            ["Стрий", "Долина"],
        ]
        self.assertEqual(check_delivery(cities, storages, pipes), [])

    def test_unreachable_some(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipes = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            # до "Долина" шляху немає
        ]
        self.assertEqual(check_delivery(cities, storages, pipes), [["Сховище_1", ["Долина"]]])

    def test_two_storages(self):
        cities = ["A", "B", "C"]
        storages = ["S1", "S2"]
        pipes = [
            ["S1", "A"],
            ["A", "B"],
            ["S2", "A"],
            # S2 не може дійти до C
            ["B", "C"],  # C досяжне для S1 через A->B->C
        ]
        # тут і S1, і S2 можуть дійти до C, бо S2 -> A -> B -> C існує
        self.assertEqual(check_delivery(cities, storages, pipes), [])

        pipes2 = [
            ["S1", "A"],
            ["A", "B"],
            ["B", "C"],
            ["S2", "A"],
            # прибрали B->C, тепер C недосяжне
        ]
        self.assertEqual(check_delivery(cities, storages, pipes2), [["S2", ["C"]], ["S1", ["C"]]])

    def test_direction_matters(self):
        cities = ["Львів", "Стрий"]
        storages = ["Сховище_1"]
        pipes = [
            ["Львів", "Сховище_1"],  # напрям навпаки
            ["Львів", "Стрий"],
        ]
        self.assertEqual(check_delivery(cities, storages, pipes), [["Сховище_1", ["Львів", "Стрий"]]])


if __name__ == "__main__":
    unittest.main()