import sqlite3

connection: sqlite3.Connection = sqlite3.connect("example.db")
cursor: sqlite3.Cursor = connection.cursor()

sql_create = """
    CREATE TABLE stocks (
        date text,
        trans text,
        symbol text,
        qty real,
        price real
    )"""
sql_insert = """
    INSERT INTO stocks VALUES (
        "2006-01-05",
        "BUY",
        "RHAT",
        100,
        35.14
    )"""

cursor.execute(sql_create)
cursor.execute(sql_insert)
connection.commit()
connection.close()