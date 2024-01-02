import sqlite3

#  CRUD - create reed update delete
# db = sqlite3.connect('op36_3.db')
# cursor = db.cursor()

db = sqlite3.connect('op36_3.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    lastname TEXT,
    age INTEGER,
    view INTEGER,
    bitday DATE
)''')

# cursor.execute('''INSERT INTO user VALUES ("beka", 49, 5, '2003-87-99')''')

# Удаление строк с чётными rowid
cursor.execute('''DELETE FROM user WHERE rowid % 2 = 0''')
cursor.execute('''SELECT rowid,* FROM user''')
rows = cursor.fetchall()
for row in rows:
    print(row)

db.commit()
db.close()