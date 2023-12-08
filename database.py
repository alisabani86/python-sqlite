import sqlite3

conn = sqlite3.connect('my_database.db')

c = conn.cursor()

c.execute('''
    CREATE TABLE Users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

c.execute('''
    CREATE TABLE Orders(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product TEXT,
        amount REAL,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES Users(id)
    )
''')

users = [(1, 'John Doe', 'john@example.com'),
         (2, 'Jane Smith', 'jane@example.com'),
         (3, 'adam', 'adam@example.com')]
orders = [
    (1, 1, 'Product 1', 19.99, '2023-01-04'),
    (2, 1, 'Product 2', 29.99, '2023-02-03'),
    (3, 2, 'Product 3', 15.99, '2023-03-02'),
    (4, 2, 'Product 4', 25.99, '2023-04-01'),
    (5, 1, 'Product 5', 30.99, '2023-05-02'),
    (6, 1, 'Product 1', 19.99, '2023-06-01'),
    (7, 1, 'Product 2', 29.99, '2023-07-02'),
    (8, 2, 'Product 3', 15.99, '2023-08-01'),
    (9, 2, 'Product 4', 25.99, '2023-09-02'),
    (10, 1, 'Product 5', 30.99, '2023-10-01'),
    (11, 1, 'Product 1', 19.99, '2023-11-02'),
    (12, 1, 'Product 2', 29.99, '2023-12-01'),
    (13, 3, 'Product 3', 15.99, '2023-01-02'),
    (14, 3, 'Product 4', 25.99, '2023-02-01'),
    (15, 1, 'Product 5', 30.99, '2023-03-02'),
    (16, 1, 'Product 1', 19.99, '2023-04-01'),
    (17, 1, 'Product 2', 29.99, '2023-05-02'),
    (18, 2, 'Product 3', 15.99, '2023-06-01'),
    (19, 2, 'Product 4', 25.99, '2023-07-02'),
    (20, 1, 'Product 5', 30.99, '2023-08-01'),
]

c.executemany('INSERT INTO Users VALUES (?,?,?)', users)
c.executemany('INSERT INTO Orders VALUES (?,?,?,?,?)', orders)

conn.commit()
conn.close()