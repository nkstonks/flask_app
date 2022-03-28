import sqlite3

connection = sqlite3.connect("auth.db")
# print(connection.total_changes)

cursor = connection.cursor()

# cursor.execute("CREATE TABLE auth (username TEXT, password TEXT)")

credentials = cursor.execute("SELECT username, password FROM auth").fetchall()
print(credentials)