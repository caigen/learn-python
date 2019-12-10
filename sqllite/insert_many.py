import sqlite3

connection: sqlite3.Connection = sqlite3.connect("example.db")
cursor: sqlite3.Cursor = connection.cursor()

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
sql_insert_many = """
    INSERT INTO stocks VALUES (?,?,?,?,?)
    """
cursor = connection.cursor()
cursor.executemany(sql_insert_many, purchases)
connection.commit()