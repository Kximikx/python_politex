import unittest  # бібліотека тестів

from lab9 import Trie, build_trie  # імпорт класу і функції


class TestTrie(unittest.TestCase):  # тести для Trie
    def test_insert_and_search(self) -> None:  # тест вставки і пошуку
        t = Trie()  # створюємо Trie
        t.insert("apple")  # вставляємо слово
        self.assertTrue(t.search("apple"))  # слово має знайтись
        self.assertFalse(t.search("app"))  # префікс не є словом
        self.assertFalse(t.search("apples"))  # інше слово не знайдеться

    def test_starts_with(self) -> None:  # тест префіксів
        t = Trie()  # створюємо Trie
        t.insert("apple")  # вставляємо слово
        self.assertTrue(t.starts_with("app"))  # префікс є
        self.assertTrue(t.starts_with("apple"))  # префікс = слово
        self.assertFalse(t.starts_with("apx"))  # префікса нема

    def test_multiple_words(self) -> None:  # кілька слів
        t = Trie()  # Trie
        t.insert("car")  # слово 1
        t.insert("cat")  # слово 2
        t.insert("dog")  # слово 3

        self.assertTrue(t.search("car"))  # car є
        self.assertTrue(t.search("cat"))  # cat є
        self.assertTrue(t.search("dog"))  # dog є
        self.assertFalse(t.search("do"))  # do нема як слово
        self.assertTrue(t.starts_with("ca"))  # ca є як префікс
        self.assertFalse(t.starts_with("da"))  # da нема

    def test_empty_string(self) -> None:  # порожній рядок
        t = Trie()  # Trie
        t.insert("")  # вставляємо порожній рядок
        self.assertTrue(t.search(""))  # має знайтись
        self.assertTrue(t.starts_with(""))  # порожній префікс завжди існує

    def test_build_trie(self) -> None:  # тест build_trie
        patterns = ["ab", "abc", "bca"]  # список слів
        t = build_trie(patterns)  # будуємо Trie

        self.assertTrue(t.search("ab"))  # ab є
        self.assertTrue(t.search("abc"))  # abc є
        self.assertTrue(t.search("bca"))  # bca є
        self.assertFalse(t.search("a"))  # a нема як слово
        self.assertTrue(t.starts_with("a"))  # але префікс a є
        self.assertTrue(t.starts_with("ab"))  # ab є
        self.assertFalse(t.starts_with("ac"))  # ac нема

    def test_none_inputs(self) -> None:  # тест на None
        t = Trie()  # Trie
        with self.assertRaises(ValueError):  # чекаємо помилку
            t.insert(None)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):  # чекаємо помилку
            t.search(None)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):  # чекаємо помилку
            t.starts_with(None)  # type: ignore[arg-type]

        with self.assertRaises(ValueError):  # чекаємо помилку
            build_trie(None)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):  # чекаємо помилку
            build_trie(["a", None])  # type: ignore[list-item]


if __name__ == "__main__":  # запуск тестів напряму
    unittest.main()  # запускаємо unittest