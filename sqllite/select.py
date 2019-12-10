import sqlite3

connection: sqlite3.Connection = sqlite3.connect("example.db")
cursor: sqlite3.Cursor = connection.cursor()

# 一条数据
print("fetch one")
t = ("RHAT",)
sql_select = """
    SELECT * FROM stocks WHERE symbol=?
    """
cursor.execute(sql_select, t)
print(cursor.fetchone())


# 查询得到多条数据
sql_select = """
    SELECT * FROM stocks ORDER BY price
    """

print("fetch all:")
cursor.execute(sql_select)
print(cursor.fetchall())

print("for each row:")
for row in cursor.execute(sql_select):
    print(row)

