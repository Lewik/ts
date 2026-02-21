import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'clan.db')

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.executescript('''
    CREATE TABLE IF NOT EXISTS snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        snapshot_id INTEGER NOT NULL,
        position INTEGER NOT NULL,
        name TEXT NOT NULL,
        help INTEGER NOT NULL,
        level INTEGER NOT NULL,
        FOREIGN KEY (snapshot_id) REFERENCES snapshots(id)
    );
''')

c.execute("INSERT INTO snapshots (date) VALUES (?)", ('2026-02-12',))
s1 = c.lastrowid

feb12 = [
    (1, 'Buryat', 5, 13001),
    (2, 'Boss', 1, 12177),
    (3, 'Vjifxx', 33, 11258),
    (4, 'Lewik', 37, 10897),
    (5, 'Sveta', 13, 10542),
    (6, 'Irina', 32, 10176),
    (7, '2z2z', 11, 6595),
    (8, 'rebz9777', 3, 5832),
    (9, 'Syava', 1, 4760),
    (10, 'yaroslav', 16, 4662),
    (11, 'lilia', 0, 4478),
    (12, 'nadya', 36, 3746),
    (13, '123', 17, 3735),
    (14, 'Ippoon', 15, 3029),
    (15, 'Danil83', 5, 2714),
    (16, 'Mary', 0, 2564),
    (17, 'BelikD', 6, 2445),
    (18, 'Ymar', 0, 1662),
    (19, 'nnigga', 2, 889),
    (20, '123', 20, 665),
    (21, 'sarma', 3, 530),
    (22, '122', 0, 509),
    (23, 'Alex', 7, 412),
    (24, 'Din', 11, 344),
    (25, 'Daminor', 0, 319),
    (26, 'ludmila', 0, 313),
    (27, 'lii', 0, 304),
    (28, 'артемас', 2, 266),
    (29, 'Lecter', 2, 254),
    (30, 'keti', 0, 253),
    (31, 'Volodya', 10, 239),
    (32, 'Sergey', 3, 209),
    (33, 'ааааа', 0, 188),
    (34, 'Iliya', 0, 167),
    (35, 'Marina', 0, 149),
    (36, 'nata', 0, 75),
    (37, 'ksenia', 0, 59),
    (38, 'Zaza', 0, 50),
    (39, 'Alex', 0, 48),
    (40, 'Annushka', 0, 37),
    (41, 'PANIKER', 0, 28),
    # position 42 not visible in screenshots
    (43, '11111111', 0, 27),
    (44, '468', 0, 26),
    (45, 'ggg', 0, 26),
    (46, 'Evaku2017', 0, 25),
    (47, '123', 0, 24),
    (48, 'Lona', 0, 21),
]

c.executemany(
    "INSERT INTO members (snapshot_id, position, name, help, level) VALUES (?, ?, ?, ?, ?)",
    [(s1, *m) for m in feb12]
)

c.execute("INSERT INTO snapshots (date) VALUES (?)", ('2026-02-21',))
s2 = c.lastrowid

feb21 = [
    (1, 'Buryat', 7, 13066),
    (2, 'Boss', 3, 12177),
    (3, 'Vjifxx', 33, 11523),
    (4, 'Lewik', 45, 11158),
    (5, 'Sveta', 0, 10542),
    (6, 'Irina', 14, 10295),
    (7, '2222', 2, 6789),
    (8, 'rebz9777', 0, 5832),
    (9, 'Syava', 0, 4955),
    (10, 'yaroslav', 2, 4895),
    (11, 'lilia', 0, 4487),
    (12, '123', 3, 3793),
    (13, 'nadya', 0, 3785),
    (14, 'Danil83', 4, 2721),
    (15, 'Mary', 0, 2585),
    (16, 'BelikD', 10, 2528),
    (17, 'Ymar', 0, 1897),
    (18, 'sarma', 4, 912),
    (19, 'nnigga', 10, 831),
    (20, 'Korol', 2, 739),
    (21, '123', 11, 715),
    (22, 'Din', 17, 625),
    (23, 'Daminor', 37, 618),
    (24, '122', 0, 512),
    (25, 'Alex', 0, 499),
    (26, 'ludmila', 0, 315),
    (27, 'lii', 0, 315),
    (28, 'Volodya', 0, 292),
    (29, 'Marina', 0, 279),
    (30, 'keti', 0, 270),
    (31, 'артемас', 0, 266),
    (32, 'Lecter', 0, 254),
    (33, 'Sergey', 2, 245),
    (34, 'ааааа', 0, 193),
    (35, 'nata', 0, 75),
    (36, 'Lona', 0, 64),
    (37, 'ksenia', 0, 59),
    (38, 'Zaza', 0, 50),
    (39, 'Alex', 0, 48),
    (40, 'Annushka', 0, 37),
    (41, 'PANIKER', 0, 34),
    (42, '468', 0, 29),
    (43, 'esa', 0, 28),
    (44, '11111111', 0, 27),
    (45, 'ggg', 0, 26),
    (46, 'Evaku2017', 0, 25),
    (47, '123', 0, 24),
]

c.executemany(
    "INSERT INTO members (snapshot_id, position, name, help, level) VALUES (?, ?, ?, ?, ?)",
    [(s2, *m) for m in feb21]
)

conn.commit()
conn.close()

print(f"Database created: {DB_PATH}")
print(f"2026-02-12: {len(feb12)} members")
print(f"2026-02-21: {len(feb21)} members")
