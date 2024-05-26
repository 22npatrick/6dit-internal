import sqlite3
conn = sqlite3.connect('Planetdb')
cursor = conn.cursor()
cursor.execute('SELECT * FROM planets;')
results = cursor.fetchall()
print(results)
conn.commit()
conn.close()