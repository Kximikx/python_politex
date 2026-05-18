from collections import deque  # deque потрібен як швидка черга для BFS


def _bfs_z_batkamy(g, start):  # BFS від start зберігаємо батька для відновлення шляху
    q = deque([start])  # черга, стартуємо зі start
    vis = set([start])  # множина відвіданих вершин
    batko = {start: None}  # batko[v] = з якої вершини прийшли у v

    while q:  # поки є вершини для обробки
        x = q.popleft()  # беремо вершину з початку черги
        for y in g.get(x, []):  # перебираємо сусідів (куди можна піти по трубі)
            if y not in vis:  # якщо сусід ще не відвіданий
                vis.add(y)  # позначаємо відвіданим
                batko[y] = x  # запам'ятовуємо звідки прийшли
                q.append(y)  # додаємо сусіда в чергу

    return vis, batko  # повертаємо всі досяжні вершини і "батьків"


def _vidnovyty_shlyah(batko, target):  # відновлює шлях від start до target по словнику batko
    if target not in batko:  # якщо target не досяжний
        return None  # шляху немає
    path = []  # список для шляху
    cur = target  # починаємо з кінця
    while cur is not None:  # йдемо назад до старту
        path.append(cur)  # додаємо вершину
        cur = batko[cur]  # переходимо до її батька
    path.reverse()  # розвертаємо, щоб було від старту до target
    return path  # повертаємо шлях


def pereviryty_postachannya(mista, skhovyshcha, aktyvni_truby):  # повертає проблемні міста для кожного сховища
    g = {}  # граф: вершина -> список сусідів (напрям u -> v)

    def dodaty_vuzol(x):  # допоміжна: додає вершину в граф
        if x not in g:  # якщо вершини ще немає
            g[x] = []  # створюємо порожній список сусідів

    for c in mista:  # додаємо всі міста
        dodaty_vuzol(c)  # як вершини графа
    for s in skhovyshcha:  # додаємо всі сховища
        dodaty_vuzol(s)  # як вершини графа

    for u, v in aktyvni_truby:  # додаємо активні труби
        dodaty_vuzol(u)  # гарантуємо, що u є в графі
        dodaty_vuzol(v)  # гарантуємо, що v є в графі
        g[u].append(v)  # додаємо орієнтоване ребро u -> v

    res = []  # результат: список проблем по сховищах

    for st in skhovyshcha:  # перевіряємо кожне сховище окремо
        vis, _ = _bfs_z_batkamy(g, st)  # знаходимо всі вершини, досяжні зі st
        nedostupni = [c for c in mista if c not in vis]  # міста, куди шлях не знайдено
        if nedostupni:  # якщо є проблеми
            res.append([st, nedostupni])  # додаємо у форматі [сховище, [міста]]

    return res  # якщо все ок, res буде []


def vizualnyi_zvit(mista, skhovyshcha, aktyvni_truby):  # друкує в консоль досяжність і маршрути
    g = {}  # граф: вершина -> список сусідів

    def dodaty_vuzol(x):  # додає вершину
        if x not in g:  # якщо її ще нема
            g[x] = []  # створюємо список сусідів

    for c in mista:  # додаємо міста
        dodaty_vuzol(c)  # у граф
    for s in skhovyshcha:  # додаємо сховища
        dodaty_vuzol(s)  # у граф

    for u, v in aktyvni_truby:  # додаємо труби
        dodaty_vuzol(u)  # u існує
        dodaty_vuzol(v)  # v існує
        g[u].append(v)  # ребро u -> v

    for st in skhovyshcha:  # звіт для кожного сховища
        vis, batko = _bfs_z_batkamy(g, st)  # BFS + батьки для шляхів
        dostupni = [c for c in mista if c in vis]  # міста, куди можна подати газ
        nedostupni = [c for c in mista if c not in vis]  # міста без газу зі st

        print("ГАЗОСХОВИЩЕ:", st)  # виводимо назву сховища
        print("ДОСЯЖНІ МІСТА:", ", ".join(dostupni) if dostupni else "-")  # список досяжних
        print("НЕДОСЯЖНІ МІСТА:", ", ".join(nedostupni) if nedostupni else "-")  # список недосяжних

        if dostupni:  # якщо є досяжні міста
            print("МАРШРУТИ:")  # заголовок маршрутів
            for c in dostupni:  # для кожного досяжного міста
                p = _vidnovyty_shlyah(batko, c)  # відновлюємо шлях
                if p is not None:  # якщо шлях існує
                    print("  " + " -> ".join(p))  # друкуємо шлях стрілками

        print()  # порожній рядок для розділення


def zapisaty_txt(res, filename="gas_report.txt"):  # створює txt файл зі звітом "нема газу"
    bad_cities = set()  # множина міст, де немає газу хоча б з одного сховища
    for st, cities in res:  # перебираємо проблеми по сховищах
        for c in cities:  # перебираємо недосяжні міста
            bad_cities.add(c)  # додаємо місто в множину

    with open(filename, "w", encoding="utf-8") as f:  # відкриваємо файл на запис
        if not res:  # якщо проблем нема
            f.write("Газ є у всіх містах (з усіх сховищ).\n")  # пишемо що все ок
        else:  # якщо проблеми є
            f.write("Нема газу.\n")  # заголовок
            f.write("Міста, в яких немає газу (хоча б з одного сховища):\n")  # пояснення
            for c in sorted(bad_cities):  # сортуємо для красивого виводу
                f.write(c + "\n")  # записуємо місто в файл


if __name__ == "__main__":  # запуск як основна програма
    mista = ["Львів", "Стрий", "Долина"]  # список міст
    skhovyshcha = ["Сховище_1", "Сховище_2"]  # список газосховищ
    aktyvni_truby = [  # активні труби (напрям важливий)
        ["Сховище_1", "Львів"],  # труба Сховище_1 -> Львів
        ["Львів", "Стрий"],  # труба Львів -> Стрий
        ["Долина", "Львів"],  # труба Долина -> Львів
        ["Сховище_1", "Сховище_2"],  # труба Сховище_1 -> Сховище_2
    ]

    vidpovid = pereviryty_postachannya(mista, skhovyshcha, aktyvni_truby)  # знаходимо недосяжні міста
    print("РЕЗУЛЬТАТ:", vidpovid)  # друкуємо відповідь по умові

    print("\nВІЗУАЛЬНИЙ ЗВІТ:\n")  # заголовок для візуалу
    vizualnyi_zvit(mista, skhovyshcha, aktyvni_truby)  # друкуємо досяжність і маршрути

    zapisaty_txt(vidpovid, "gas_report.txt")  # створюємо txt звіт
    print("Звіт збережено у файл gas_report.txt")  # повідомляємо про файл