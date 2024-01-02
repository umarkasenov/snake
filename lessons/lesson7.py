# # SQL - язык структурированных запросов
# # база данных -
# # СУБД- система управления базами данных
# # NOsql:SQL
# # posgreSQL,mySQL, SQLite3-2
#
# import sqlite3
#
# # CRUD - create reed update delete
# db = sqlite3.connect('op36_3.db')
# cursor = db.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS user (
# lastname TEXT,
# age INTEGER,
# view INTEGER,
# bitday DATE
# )''')
#
# # CREATE - INSERT INTO
# # cursor.execute('''INSERT INTO user VALUES ("beka",49,5,'2003-87-99')''')
#
# # UPDATE-UPDATE
# cursor.execute('''UPDATE user SET age=99 WHERE rowid!=2 ''')
#
#
#
# # REED-SELECT,fech
# cursor.execute('''SELECT rowid,* FROM user''')
# a=cursor.fetchall()
# for i in a:
#     print(i)
#
#
# db.commit()
# db.close()
#


import sqlite3

# CRUD - create reed update delete
db = sqlite3.connect('op36_3.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
lastname TEXT,
age INTEGER,
view INTEGER,
bitday DATE
)''')

# CREATE - INSERT INTO
cursor.execute('''INSERT INTO user VALUES ("beka", 49, 5, '2003-87-99')''')

# UPDATE - UPDATE
cursor.execute('''UPDATE user SET age=99 WHERE rowid!=2 ''')

# READ - SELECT, fetch
cursor.execute('''SELECT rowid, * FROM user''')
result = cursor.fetchall()
for row in result:
    print(row)

db.commit()
db.close()
