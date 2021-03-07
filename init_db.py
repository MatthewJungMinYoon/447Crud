import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO studs (name, studID, marks) VALUES (?, ?, ?)",
            ('Joe', 21, 90)
            )

cur.execute("INSERT INTO studs (name, studID, marks) VALUES (?, ?, ?)",
            ('Jian', 22, 92)
            )

cur.execute("INSERT INTO studs (name, studID, marks) VALUES (?, ?, ?)",
            ('Chris', 23, 90)
            )

cur.execute("INSERT INTO studs (name, studID, marks) VALUES (?, ?, ?)",
            ('Sai', 24, 95)
            )

cur.execute("INSERT INTO studs (name, studID, marks) VALUES (?, ?, ?)",
            ('Andrew', 25, 100)
            )
         
cur.execute("INSERT INTO studs (name, studID, marks) VALUES (?, ?, ?)",
            ('Lynn', 26, 90)
            )

cur.execute("INSERT INTO studs (name, studID, marks) VALUES (?, ?, ?)",
            ('Robert', 27, 85)
            )            
connection.commit()
connection.close()