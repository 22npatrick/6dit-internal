import sqlite3, time, os
conn = sqlite3.connect('Planetdb')
cursor = conn.cursor()

def get_only_official_planet():
    # Execute an SQL statement
    query = "SELECT * FROM planets where type != 'Dwarf Planet';"
    cursor.execute(query)
    official_planets = cursor.fetchall()
    for official_planet in official_planets:
        print(f"{official_planet[1]}")
        time.sleep(0.75)

def get_only_dwarf_planet():
    query = "SELECT * FROM planets where type == 'Dwarf Planet';"
    cursor.execute(query)
    dwarf_planets = cursor.fetchall()
    for dwarf_planet in dwarf_planets:
        print(f"{dwarf_planet[1]}")
        time.sleep(0.75)

def get_all_people_who_discover_planets():
    query = "SELECT * FROM planets where discovery_date != 'NULL';"
    cursor.execute(query)
    all_planets = cursor.fetchall()
    for planet in all_planets:
        print(f"{planet[9]} discovered {planet[1]} in {planet[10]}")
        time.sleep(0.75)


def chosen_planet_data():
    while True:
        print("Chose and ID value from 1 - 13")
        try:
            user_wanted_planet = int(input("Chosen planet's ID: "))
            if user_wanted_planet > 0 and user_wanted_planet < 14:
                break
            else:
                print("Planet ID " + str(user_wanted_planet) + " is not in this table")
                print("Please type a different value")
        except ValueError:
            print("Not a planet ID")
            time.sleep(0.75)
            continue
    cursor.execute("SELECT * FROM planets WHERE planet_id=?", (user_wanted_planet,))
    all_planets = cursor.fetchall()
    for all_planet in all_planets:
            print(f"{all_planet[1]}'s planet type is {all_planet[2]}, it's {all_planet[3]} million km away from the sun")
            time.sleep(2)
            print(f"it's mass in earth masses is {all_planet[4]}, the diameter of this planet is {all_planet[5]}km")
            time.sleep(2)
            print(f"it has a gravity of {all_planet[6]} in m/s² and takes {all_planet[7]} earth days to orbit around the sun")
            time.sleep(2)
            if all_planet[9] == "known since ancient times":
                print(f"it has {all_planet[8]} moon(s), it's existence has been {all_planet[9]}")
            else:
                print(f"it has {all_planet[8]} moon(s), was discorved by {all_planet[9]} and was discovered in {all_planet[10]}")
            time.sleep(2)
            print(f'out of the other planets in the data set this planet was ranked {all_planet[11]} out of 13 in terms of proximity to the sun ')
            time.sleep(2)

#MENU select screen
while True:
    choice = input("\n1. Get Official Planets\n3. Get Dwarf Planets\n3. Get all data for chosen planet\n4. Get who discovered each planet\n5. Exit\n> ")
    if choice == "1":
        get_only_official_planet()
    elif choice == "2":
        get_only_dwarf_planet()
    elif choice == "3":
        chosen_planet_data()
    elif choice == "4":
        get_all_people_who_discover_planets()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
conn.commit()
conn.close()
