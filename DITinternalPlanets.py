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
        time.sleep(0.45)
    use_again()

def get_only_dwarf_planet():
    query = "SELECT * FROM planets where type == 'Dwarf Planet';"
    cursor.execute(query)
    dwarf_planets = cursor.fetchall()
    for dwarf_planet in dwarf_planets:
        print(f"{dwarf_planet[1]}")
        time.sleep(0.65)
    use_again()

def get_all_people_who_discover_planets():
    query = "SELECT * FROM planets where discovery_date != 'NULL';"
    cursor.execute(query)
    all_planets = cursor.fetchall()
    for planet in all_planets:
        print(f"{planet[9]} discovered {planet[1]} in {planet[10]}")
        time.sleep(0.75)
    use_again()


def chosen_planet_data():
    while True:
        print("Chose an ID value from 1 - 13")
        print("if you want to know what planet has what id then type the number 0")
        try:
            user_wanted_planet = input("Chosen planet's ID: ").strip()
            user_wanted_planet = int(user_wanted_planet)
            print("\n")
            if user_wanted_planet > 0 and user_wanted_planet < 14:
                break
            elif user_wanted_planet == 0:
                query = "SELECT * FROM planets;"
                cursor.execute(query)
                all_planets = cursor.fetchall()
                for a_planet in all_planets:
                    print(f"{a_planet[1]} has a planet ID {a_planet[0]}")
                    time.sleep(0.3)
                time.sleep(0.65)
                print("\n")
            else:
                print("Planet ID " + str(user_wanted_planet) + " is not in this table")
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
    use_again()

def order_plantes_by():
    while True:
        print("0 - planet_id\n1 - name\n2 - type\n3 - distance_from_sun\n4 - mass\n5 - diameter\n6 - gravity\n7 - orbital_period\n8 - number_of_moons\n9 - discovered_by\n10 - discovery_date\n11 - distance_rank\n")
        try:
            order_by = input("Type the number next to what you want to order by\t>").strip()
            order_by = int(order_by)
        except ValueError:
            print("Not a valid number")
            time.sleep(1.5)
            os.system("cls")
            continue
        if order_by > -1 or order_by < 12:
            if order_by == 0:
                order_by_x = "planet_id"
            elif order_by == 1:
                order_by_x = "name"
            elif order_by == 2:
                order_by_x = "type"
            elif order_by == 3:
                order_by_x = "distance_from_sun"
            elif order_by == 4:
                order_by_x = "mass"
            elif order_by == 5:
                order_by_x = "diameter"
            elif order_by == 6:
                order_by_x = "gravity"
            elif order_by == 7:
                order_by_x = "orbital_period"
            elif order_by == 8:
                order_by_x = "number_of_moons"
            elif order_by == 9:
                order_by_x = "discovered_by"
            elif order_by == 10:
                order_by_x = "discovery_date"
            else:
                order_by_x = "distance_rank"
            query = ("SELECT * FROM planets ORDER BY " + order_by_x + ";")
            cursor.execute(query)
            all_planets = cursor.fetchall()
            os.system("cls")
            for planet in all_planets:
                if order_by == 1:
                    print(f"{planet[1]}")
                else:
                    print(f"{planet[1]} \t| {planet[order_by]}") 
                time.sleep(0.5)
            use_again()
        else:
            print("Invalid option")
            os.system("cls")
            continue



def use_again():
    print("\n")
    time.sleep(1.5)
    while True:
        use_again = input("Do you want to use the program again? (type yes if yes and no if no)\n>\t").upper().strip()
        if use_again == "YES":
            os.system("cls")
            time.sleep(0.5)
            menu()
        elif use_again == "NO":
            os.system("cls")
            time.sleep(0.5)
            conn.commit()
            conn.close()
            exit()
        print("\nInvalid choice")
        print("Please try again \n")
        time.sleep(0.5)


def menu():
    while True:
        choice = input("\n1. Get Official Planets\n3. Get Dwarf Planets\n3. Get all data for chosen planet\n4. Get who discovered each planet\n5. Order data by chosen category\n6. Exit\n> ")
        if choice == "1":
            get_only_official_planet()
            os.system("cls")
        elif choice == "2":
            get_only_dwarf_planet()
            os.system("cls")
        elif choice == "3":
            chosen_planet_data()
            os.system("cls")
        elif choice == "4":
            get_all_people_who_discover_planets()
            os.system("cls")
        elif choice == "5":
            order_plantes_by()
            os.system("cls")
        elif choice == "6":
            exit()
        else:
            print("Invalid choice")

menu()


         
