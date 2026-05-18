from __future__ import annotations  # щоб типи класів працювали без лапок


class TrieNode:  # вузол префіксного дерева
    def __init__(self) -> None:  # конструктор вузла
        self.children: dict[str, TrieNode] = {}  # діти: символ -> вузол
        self.is_end: bool = False  # чи закінчується тут слово


class Trie:  # клас Trie (префіксне дерево)
    def __init__(self) -> None:  # конструктор Trie
        self.root = TrieNode()  # кореневий вузол (порожній)

    def insert(self, word: str) -> None:  # вставка слова
        if word is None:  # перевірка на None
            raise ValueError("Слово не може бути None")  # помилка

        node = self.root  # стартуємо з кореня
        for ch in word:  # йдемо по символах слова
            if ch not in node.children:  # якщо немає гілки під символ
                node.children[ch] = TrieNode()  # створюємо вузол
            node = node.children[ch]  # переходимо в дочірній вузол
        node.is_end = True  # позначаємо кінець слова

    def search(self, word: str) -> bool:  # пошук слова
        if word is None:  # перевірка на None
            raise ValueError("Слово не може бути None")  # помилка

        node = self.root  # старт з кореня
        for ch in word:  # йдемо по символах
            nxt = node.children.get(ch)  # беремо наступний вузол
            if nxt is None:  # якщо гілки нема
                return False  # слова нема
            node = nxt  # переходимо далі
        return node.is_end  # True лише якщо слово тут закінчується

    def starts_with(self, prefix: str) -> bool:  # перевірка префіксу
        if prefix is None:  # перевірка на None
            raise ValueError("Префікс не може бути None")  # помилка

        node = self.root  # старт з кореня
        for ch in prefix:  # йдемо по символах префіксу
            nxt = node.children.get(ch)  # беремо наступний вузол
            if nxt is None:  # якщо гілки нема
                return False  # такого префіксу нема
            node = nxt  # переходимо далі
        return True  # усі символи префіксу знайдені


def build_trie(patterns: list[str]) -> Trie:  # будує Trie зі списку слів
    if patterns is None:  # перевірка на None
        raise ValueError("Список patterns не може бути None")  # помилка

    t = Trie()  # створюємо Trie
    for p in patterns:  # перебираємо всі слова
        if p is None:  # якщо в списку є None
            raise ValueError("Список patterns не може містити None")  # помилка
        t.insert(p)  # вставляємо слово
    return t  # повертаємо готовий Trie


if __name__ == "__main__":  # запуск як основний файл
    patterns = ["квітка", "квітник", "кіт", "київ"]  # приклад слів
    trie = build_trie(patterns)  # будуємо Trie

    print("Trie створено зі слів:", patterns)  
    print("Пошук слова 'кіт':", trie.search("кіт"))  # перевірка слова
    print("Пошук слова 'кві':", trie.search("кві"))  # це не слово
    print("Префікс 'кві':", trie.starts_with("кві"))  # префікс існує
    print("Префікс 'дні':", trie.starts_with("дні"))  # префікса нема