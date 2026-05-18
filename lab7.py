import os  # робота з шляхами до файлів
import webbrowser  # відкривати HTML у браузері
from collections import deque  # deque як черга для BFS в алгоритмі потоку

INF = 10**18  # дуже велика місткість для "без обмежень"


class MF:  # простий клас максимального потоку (Dinic)
    def __init__(self, n):  # конструктор, n = кількість вершин
        self.n = n  # зберігаємо кількість вершин
        self.g = [[] for _ in range(n)]  # список суміжності для ребер

    def add(self, u, v, c):  # додати ребро u->v з місткістю c
        self.g[u].append([v, c, len(self.g[v])])  # пряме ребро (куди, місткість, індекс зворотного)
        self.g[v].append([u, 0, len(self.g[u]) - 1])  # зворотне ребро (для резидуальної мережі)

    def _bfs(self, s, t):  # BFS по рівнях для Dinic
        self.lv = [-1] * self.n  # масив рівнів вершин
        q = deque([s])  # черга BFS зі стартом s
        self.lv[s] = 0  # рівень джерела = 0
        while q:  # поки є вершини в черзі
            u = q.popleft()  # беремо вершину
            for v, cap, rev in self.g[u]:  # перебираємо ребра з u
                if cap > 0 and self.lv[v] == -1:  # якщо є резидуальна місткість і v ще не в рівнях
                    self.lv[v] = self.lv[u] + 1  # задаємо рівень сусіда
                    q.append(v)  # додаємо сусіда в чергу
        return self.lv[t] != -1  # чи досяжний стік t

    def _dfs(self, u, t, f):  # DFS для пошуку блокуючого потоку
        if u == t:  # якщо дійшли до стоку
            return f  # повертаємо, скільки можемо проштовхнути
        for i in range(self.it[u], len(self.g[u])):  # перебираємо ребра з u з поточного індексу
            self.it[u] = i  # оновлюємо вказівник (щоб не переглядати заново)
            v, cap, rev = self.g[u][i]  # беремо ребро
            if cap > 0 and self.lv[v] == self.lv[u] + 1:  # тільки по рівневому графу
                pushed = self._dfs(v, t, min(f, cap))  # пробуємо проштовхнути далі
                if pushed:  # якщо щось проштовхнули
                    self.g[u][i][1] -= pushed  # зменшуємо місткість прямого ребра
                    self.g[v][rev][1] += pushed  # збільшуємо місткість зворотного ребра
                    return pushed  # повертаємо величину потоку
        return 0  # якщо не змогли проштовхнути

    def run(self, s, t):  # порахувати максимальний потік s->t
        flow = 0  # накопичений потік
        while self._bfs(s, t):  # поки стік досяжний у резидуальному графі
            self.it = [0] * self.n  # вказівники для DFS з кожної вершини
            while True:  # шукаємо додаткові шляхи
                pushed = self._dfs(s, t, INF)  # пробуємо проштовхнути максимум
                if pushed == 0:  # якщо більше не проштовхується
                    break  # виходимо з внутрішнього циклу
                flow += pushed  # додаємо до відповіді
        return flow  # повертаємо максимальний потік


def _split_list(line):  # розбити рядок "F1, F2, F3" у список
    parts = [x.strip() for x in line.split(",")]  # ділимо по комі і чистимо пробіли
    return [x for x in parts if x]  # прибираємо порожні елементи


def read_roads(path):  # читає roads.csv
    with open(path, "r", encoding="utf-8-sig", newline="") as f:  # відкриваємо файл
        raw = f.read().splitlines()  # читаємо всі рядки

    if len(raw) < 2:  # якщо немає двох перших рядків
        raise ValueError("roads.csv має мати 2 перші рядки: ферми і магазини")  # помилка формату

    farms = _split_list(raw[0])  # перший рядок — ферми
    shops = _split_list(raw[1])  # другий рядок — магазини

    edges = []  # список доріг
    for line in raw[2:]:  # далі йдуть дороги
        if not line.strip():  # пропускаємо порожні рядки
            continue  # переходимо далі
        row = [x.strip() for x in line.split(",")]  # u, v, cap
        if len(row) < 3:  # якщо рядок неповний
            continue  # пропускаємо
        u = row[0]  # звідки
        v = row[1]  # куди
        cap = int(row[2])  # місткість (скільки машин на день)
        edges.append((u, v, cap))  # додаємо дорогу в список

    return farms, shops, edges  # повертаємо дані


def max_cars(path):  # рахує максимальну кількість машин (max flow)
    farms, shops, edges = read_roads(path)  # читаємо дані з CSV

    nodes = set()  # множина всіх вершин
    for x in farms:  # додаємо ферми
        nodes.add(x)  # як вершини
    for x in shops:  # додаємо магазини
        nodes.add(x)  # як вершини
    for u, v, _ in edges:  # додаємо всі вершини з доріг
        nodes.add(u)  # u
        nodes.add(v)  # v

    SS = "__SS__"  # назва супер-джерела
    TT = "__TT__"  # назва супер-стоку
    nodes.add(SS)  # додаємо супер-джерело
    nodes.add(TT)  # додаємо супер-стік

    idx = {name: i for i, name in enumerate(sorted(nodes))}  # індексація вершин у числа 0..n-1
    mf = MF(len(idx))  # створюємо об’єкт максимального потоку

    for u, v, cap in edges:  # додаємо всі дороги як ребра
        mf.add(idx[u], idx[v], cap)  # u->v з місткістю cap

    for f in farms:  # з’єднуємо супер-джерело з фермами
        mf.add(idx[SS], idx[f], INF)  # SS->ферма з дуже великою місткістю

    for s in shops:  # з’єднуємо магазини з супер-стоком
        mf.add(idx[s], idx[TT], INF)  # магазин->TT з дуже великою місткістю

    ans = mf.run(idx[SS], idx[TT])  # обчислюємо max flow
    return ans, farms, shops, edges  # повертаємо результат і дані для звіту


def make_html(ans, farms, shops, edges):  # генерує HTML-звіт
    farms_html = "".join(f"<span class='pill'>{x}</span>" for x in farms) or "<span class='muted'>нема</span>"  # ферми як бейджі
    shops_html = "".join(f"<span class='pill pill2'>{x}</span>" for x in shops) or "<span class='muted'>нема</span>"  # магазини як бейджі

    rows = []  # рядки таблиці доріг
    for u, v, c in edges:  # перебираємо дороги
        rows.append(f"<tr><td>{u}</td><td class='arrow'>→</td><td>{v}</td><td class='cap'>{c}</td></tr>")  # HTML-рядок

    rows_html = "\n".join(rows) if rows else "<tr><td colspan='4' class='muted'>Нема доріг у файлі</td></tr>"  # якщо доріг нема

    return f"""<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Квітка — Максимальний потік</title>
<style>
  :root {{
    --bg1:#0b1020; --bg2:#0f1b3a;
    --card:#111a33cc; --stroke:#26325d;
    --text:#e9eefc; --muted:#aab5de;
    --accent:#7c5cff; --accent2:#00d4ff; --good:#38d996;
  }}
  body {{
    margin:0; font-family: Arial, sans-serif; color:var(--text);
    background: radial-gradient(1200px 600px at 20% 10%, #1a2a6c55, transparent 60%),
                radial-gradient(900px 500px at 90% 30%, #00d4ff33, transparent 55%),
                linear-gradient(180deg, var(--bg1), var(--bg2));
  }}
  .wrap {{ max-width: 980px; margin: 32px auto; padding: 0 16px; }}
  .hero {{ display:flex; gap:16px; flex-wrap:wrap; align-items:stretch; }}
  .card {{
    background: var(--card);
    border: 1px solid var(--stroke);
    border-radius: 16px;
    box-shadow: 0 12px 30px #00000055;
    padding: 18px;
  }}
  .big {{
    flex: 1 1 320px;
    position: relative;
    overflow: hidden;
  }}
  .big:before {{
    content:"";
    position:absolute; inset:-40px;
    background: conic-gradient(from 180deg, var(--accent), var(--accent2), var(--accent));
    filter: blur(40px);
    opacity:.25;
  }}
  .big > * {{ position: relative; }}
  h1 {{ margin: 0 0 6px 0; font-size: 26px; }}
  .sub {{ color: var(--muted); margin: 0 0 14px 0; }}
  .kpi {{
    display:flex; align-items:baseline; gap:10px;
    background:#0b122acc; border:1px solid #1f2a52;
    padding:14px 16px; border-radius:14px;
  }}
  .kpi .num {{ font-size: 44px; font-weight: 800; letter-spacing: .5px; }}
  .kpi .lbl {{ color: var(--muted); }}
  .badge {{
    display:inline-block; font-size:12px; padding:6px 10px;
    border-radius:999px; border:1px solid #2b3a73;
    background:#0b122a99; color: var(--muted);
  }}
  .grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:16px; }}
  @media (max-width: 760px) {{ .grid {{ grid-template-columns: 1fr; }} }}
  .title {{ font-weight: 700; margin:0 0 10px 0; }}
  .pill {{
    display:inline-block; padding:7px 10px; margin:6px 6px 0 0;
    border-radius: 999px; border:1px solid #2c3b76;
    background:#0b122acc;
  }}
  .pill2 {{ border-color:#1f6070; }}
  table {{
    width:100%; border-collapse: collapse; overflow:hidden;
    border-radius: 14px; border:1px solid #25315b;
    background:#0b122acc;
  }}
  th, td {{ padding:10px 10px; border-bottom:1px solid #202a50; text-align:left; }}
  th {{ color: var(--muted); font-weight:600; background:#0b122a; }}
  tr:last-child td {{ border-bottom:none; }}
  .arrow {{ width:34px; text-align:center; color: var(--muted); }}
  .cap {{ font-weight:700; color: var(--good); }}
  .muted {{ color: var(--muted); }}
  .foot {{ margin-top: 18px; color: var(--muted); font-size: 13px; }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <div class="card big">
        <span class="badge">Алгоритм: Максимальний потік</span>
        <h1>Компанія «Квітка» — доставка квітів</h1>
        <p class="sub">Максимальна кількість машин за день з ферм до магазинів з урахуванням пропускних здатностей доріг.</p>
        <div class="kpi">
          <div class="num">{ans}</div>
          <div class="lbl">машин / день</div>
        </div>
        <div class="foot">
        </div>
      </div>

      <div class="card" style="flex:1 1 240px">
        <p class="title">Ферми</p>
        <div>{farms_html}</div>
        <p class="title" style="margin-top:16px">Магазини</p>
        <div>{shops_html}</div>
      </div>
    </div>

    <div class="grid">
      <div class="card">
        <p class="title">Дороги (u → v) і місткість</p>
        <table>
          <thead>
            <tr><th>Звідки</th><th></th><th>Куди</th><th>Місткість</th></tr>
          </thead>
          <tbody>
            {rows_html}
          </tbody>
        </table>
      </div>

      <div class="card">
        <p class="title">Пояснення</p>
        <p class="muted">
          Кожна дорога має місткість — максимум машин за день. Максимальний потік знаходить найбільший можливий обсяг доставки,
          який не перевищує жодної місткості.
        </p>
      </div>
    </div>
  </div>
</body>
</html>
"""


def make_report():  # створює HTML-файл і відкриває його
    path = os.path.join(os.path.dirname(__file__), "roads.csv")  # шлях до roads.csv поряд із цим файлом
    ans, farms, shops, edges = max_cars(path)  # рахуємо відповідь і беремо дані
    html = make_html(ans, farms, shops, edges)  # генеруємо HTML-сторінку
    out_path = os.path.join(os.path.dirname(__file__), "report.html")  # шлях для звіту
    with open(out_path, "w", encoding="utf-8") as f:  # відкриваємо report.html на запис
        f.write(html)  # записуємо HTML у файл
    webbrowser.open("file://" + os.path.abspath(out_path))  # відкриваємо звіт у браузері
    return ans, out_path  # повертаємо відповідь і шлях


if __name__ == "__main__":  # якщо запускаємо файл напряму
    ans, out_path = make_report()  # створюємо звіт і отримуємо результат
    print(ans)  # друкуємо число (максимум машин)
    print("Звіт створено:", out_path)  # показуємо де лежить report.html