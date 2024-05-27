import sqlite3
conn = sqlite3.connect('Planetdb')
cursor = conn.cursor()

def get_only_official_planet():
    # Execute an SQL statement
    query = "SELECT * FROM planets where type != 'Dwarf Planet';"
    cursor.execute(query)
    official_planets = cursor.fetchall()
    for official_planet in official_planets:
        print(f"{official_planet[1]} is a {official_planet[2]}.")

def get_all_planets():
    cursor.execute('SELECT * FROM planets;')
    results = cursor.fetchall()
    print(results)

while True:
    choice = input("\n1. Get official planets\n2. Get all data\n3. Exit\n> ")
    if choice == "1":
        get_only_official_planet()
    elif choice == "2":
        get_all_planets()
    elif choice == "3":
        break
conn.commit()
conn.close()

