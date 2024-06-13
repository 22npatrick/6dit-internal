# Imports sqlite3, time, os to be used in the program
import sqlite3, time, os

#Connects to the planet database
conn = sqlite3.connect('Planetdb')
cursor = conn.cursor()

# A function that prints all planets and all there planet ids
def get_all_planets():
        # Execute an SQL statement
    query = "SELECT * FROM planets;"
    cursor.execute(query)
    # Save the result to a variable
    all_planets = cursor.fetchall()
    # Loop over planets, printing out planet information each time
    for a_planet in all_planets:
        print(f"{a_planet[1]} has a planet ID {a_planet[0]}")
        time.sleep(0.3)
    time.sleep(0.65)

# A function that only prints "Offical" planets
def get_only_official_planet():
    # Execute an SQL statement
    query = "SELECT * FROM planets WHERE type != 'Dwarf Planet';"
    cursor.execute(query)
    # Save the result to a variable
    official_planets = cursor.fetchall()
    # Loop over official planets, printing out planet information each time
    for official_planet in official_planets:
        print(f"{official_planet[1]}")
        time.sleep(0.45)
    # Does the use again function
    use_again()

# A function that only prints drawf planets
def get_only_dwarf_planet():
    # Execute an SQL statement
    query = "SELECT * FROM planets WHERE type == 'Dwarf Planet';"
    cursor.execute(query)
    # Save the result to a variable
    dwarf_planets = cursor.fetchall()
    # Loop over dwarf planets, printing out planet information each time
    for dwarf_planet in dwarf_planets:
        print(f"{dwarf_planet[1]}")
        time.sleep(0.65)
    # Does the use again function
    use_again()

# A function that prints who discovered planets, when they discovered planets
# and what planet they discovered
def get_people_who_discover_planets():
    # Execute an SQL statement
    query = "SELECT * FROM planets WHERE discovery_date != 'NULL';"
    cursor.execute(query)
    # Save the result to a variable
    all_planets = cursor.fetchall()
    # Loop over planets, printing out information each time
    for planet in all_planets:
        print(f"{planet[9]} discovered {planet[1]} in {planet[10]}")
        time.sleep(0.75)
    # Does the use again function
    use_again()

# A function that is used when the user inputs a invalid value
def invalid_choice_text():
    print("Invalid choice")
    time.sleep(1.5)
    os.system("cls")
    
# Asks the user what planet they want all the data for
#Prints out the data in readable sentences
def chosen_planet_data():
    while True:
        #Askes the user to input the planet id of what planet they want 
        # to find all the data for
        print("Chose an ID that is in this table")
        print("if you want to know what planet has what id then type the number 0")
        try:
            user_wanted_planet = int(input("Chosen planet's ID: "))
            str_user_wanted_planet = str(user_wanted_planet)
            #Checks if the planet id the user put in is in the table
            query = "SELECT * FROM planets WHERE planet_id = " + str_user_wanted_planet + ";"
            cursor.execute(query)
            test = cursor.fetchall()
            if user_wanted_planet == 0:
                #Does the get all planets function
                get_all_planets()
                print("\n")
            elif len(test) > 0:
                break
            else:
                invalid_choice_text()
                continue
        except ValueError:
            invalid_choice_text()
    all_planets = test
    # Prints the all the data for the chosen plaent in readable sentences
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
    #Does the use again function
    use_again()

#Orders planets by chosen coloum
def order_plantes_by():
    time.sleep(1.5)
    os.system("cls")
    while True:
        # Asks the user what coloum they want to order by 
        print("0 - planet_id\n1 - name\n2 - type\n3 - distance_from_sun\n4 - mass\n5 - diameter\n6 - gravity\n7 - orbital_period\n8 - number_of_moons\n9 - discovered_by\n10 - discovery_date\n")
        try:
            order_by = input("Type the number next to what you want to order by\t>").strip()
            order_by = int(order_by)
        except ValueError:
            invalid_choice_text()
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
            else:
                order_by_x = "discovery_date"
            query = "SELECT * FROM planets ORDER BY " + order_by_x
            # Askes if user wants to order the data by smallest to largest / alphabetical order or largest to smallest / reverse alphabetical order 
            while True:
                order_by_size = input("Do you want to order by smallest to largest/ alphabetical order or largest to smallest/ reverse alphabetical order? (Type ASC for the former option or DESC for the latter)\n>\t").upper().strip()
                if order_by_size == "ASC" or order_by_size == "DESC":
                    query = query + " " + order_by_size + ";"
                    break
                else:
                    print("\nInvalid choice")
                    print("Please try again \n")
                    time.sleep(1.5)
                    os.system("cls")
                    continue
            #Exucutes query 
            cursor.execute(query)
            #Sets results as variable
            all_planets = cursor.fetchall()
            os.system("cls")
            # Loop over planets, printing out information each time
            for planet in all_planets:
                # When ordering by name only prints names
                if order_by == 1:
                    print(f"{planet[1]}")
                else:
                    #Checks if the line needs an extra tab to fit the formating 
                    if len(planet[1]) > 6:
                        print(f"{planet[1]} \t| {planet[order_by]}") 
                    else:
                        print(f"{planet[1]} \t\t| {planet[order_by]}") 
                time.sleep(0.5)
            use_again()
        else:
            print("Invalid option")
            os.system("cls")
            continue

# Askes user what planet they want to delete from the table and deletes it
def delete_planet():
    while True:
        get_all_planets()
        #Askes user what planet they want to delete by askingg for that planet's planet ID
        try:
            choice = int(input("Enter the number of the planet you want to delete: "))
            choice = str(choice)
             #Checks if the planet id the user put in is in the table
            query = "SELECT * FROM planets WHERE planet_id = " + choice + ";"
            cursor.execute(query)
            test = cursor.fetchall()
            if len(test) > 0:
                break
            else:
                invalid_choice_text()
                continue
        except:
            invalid_choice_text()
    #Exucutes the delete
    cursor.execute("DELETE FROM planets WHERE planet_id = " + choice + ";")
    conn.commit()
    print("Planet deleted successfully!")
    #Does use again function
    use_again()

#Allows the user about thier customm planet and them addes it to the database
def create_custom_planet():
    #Askes the user about the name of the planet
    while True:
        name = input("Enter Planet name (has to have less than 11 characters ): ")
        if len(name) > 10 or len(name) == 0:
            invalid_choice_text()
            continue
        else:
            break
    os.system("cls")
    #Askes the user about the type of the planet
    while True:
        print("1 | Terrestrial\n2 | Gas Giant\n3 | Ice Giant\n4 | Dwarf Planet\n ")
        try:
            type = input("Type the number next to what you want your planet type to be by\t>").strip()
            type_choice = int(type)
        except ValueError:
            invalid_choice_text()
            continue
        if type_choice == 1:
            type = "Terrestrial"
            break
        elif type_choice == 2:
            type = "Gas Giant"
            break
        elif type_choice == 3:
            type = "Ice Giant"
            break
        elif type_choice == 4:
            type = "Dwarf Planet"
            break
        else:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about their planet's distance from the sun
    while True:
        try:
            distance_from_sun = float(input("Enter Planet's distance from sun in millions of kilometers (Can be decimal, has to be above 0): "))
            if distance_from_sun <= 0:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about their planet's mass
    while True:
        try:
            mass = float(input("Enter Planet's mass in Earth masses (Can be decimal, has to be above 0): "))
            if mass <= 0:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about their planet's diameter
    while True:
        try:
            diameter = float(input("Enter Planet's diameter in kilometers (Can be decimal, has to be above 0): "))
            if diameter <= 0:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about their planet's gravity
    while True:
        try:
            gravity = float(input("Enter Planet's gravity in m/s²(Can be decimal, has to be above 0): "))
            if gravity <= 0:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about their planet's orbital period
    while True:
        try:
            orbital_period = float(input("Enter Planet's orbital period (How long it takes for the planet to revolve once around the sun) in Earth days(Can be decimal, has to be above 0): "))
            if orbital_period <= 0:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about their planet's number of moons
    while True:
        try:
            number_of_moons = int(input("Enter Planet's number of moons (Has to be at least 0 and a whole number): "))
            if number_of_moons < 0:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about who discovered their planet
    while True:
        discovered_by = input("Enter who disvovered your planet(has to be less that 50 characters ): ")
        if len(discovered_by) > 50 or len(discovered_by) == 0:
            invalid_choice_text()
            continue
        else:
            break
    os.system("cls")
    #Askes the user about what year their planet was discovered
    while True:
        try:
            discovery_year = int(input("Enter Planet's year discoverd (Has to be after the year 1000): "))
            if discovery_year < 1000:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about what month their planet was discovered
    while True:
        try:
            discovery_month = input("Enter Planet's month discoverd (Has to be writen in number form ex 04 for april and 11 november): ")
            if len(discovery_month) != 2:
                invalid_choice_text()
                continue
            discovery_month = int(discovery_month)
            if discovery_month < 1 or discovery_month > 12:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    #Askes the user about what day of the month their planet was discovered
    while True:
        try:
            discovery_day = input("Enter Planet's day discoverd (Has to be writen in number form ex 04 for the 4th and 28 for the 28th): ")
            if len(discovery_day) != 2:
                invalid_choice_text()
                continue
            discovery_day = int(discovery_day)
            if discovery_day < 1 or discovery_day > 31:
                invalid_choice_text()
                continue
            break
        except ValueError:
            invalid_choice_text()
            continue
    os.system("cls")
    # Combines the discovery year, month and day into 1 string
    discovery_date = str(discovery_year) + "-" + str(discovery_month) + "-" + str(discovery_day)
    # Prevent SQL injection by using parameterized queries
    query = "INSERT INTO planets (name, type, distance_from_sun, mass, diameter, gravity, orbital_period, number_of_moons, discovered_by, discovery_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (name, type, distance_from_sun, mass, diameter, gravity, orbital_period, number_of_moons, discovered_by, discovery_date))
    conn.commit()
    print("Planet added successfully!")
    # Does use again function 
    use_again()

# Askes if the user wants to contnue using the program
def use_again():
    print("\n")
    time.sleep(1.5)
    while True:
        # Askes if the user wants to contnue using the program
        use_again = input("Do you want to use the program again? (type yes if yes and no if no)\n>\t").upper().strip()
        # If yes goes back to the menu
        if use_again == "YES":
            os.system("cls")
            time.sleep(0.5)
            menu()
        # If no exits the program
        elif use_again == "NO":
            os.system("cls")
            time.sleep(0.5)
            conn.commit() 
            conn.close()
            exit()
        invalid_choice_text()

#Acts as a menu for where the user can choose to do things
def menu():
    while True:
        #Prints out options for the user to choose
        choice = input("\n Type the number next to the thing you wanted to do\n1. Get Official Planets\n2. Get Dwarf Planets\n3. Get all data for chosen planet\n4. Get who discovered each planet\n5. Order data by chosen category\n6. Create custom planet\n7. Delete planet\n8. Exit\n> ")
        if choice == "1":
            os.system("cls")
            get_only_official_planet()
        elif choice == "2":
            os.system("cls")
            get_only_dwarf_planet()
        elif choice == "3":
            os.system("cls")
            chosen_planet_data()
        elif choice == "4":
            os.system("cls")
            get_people_who_discover_planets()
        elif choice == "5":
            os.system("cls")
            order_plantes_by()
        elif choice == "6":
            os.system("cls")
            create_custom_planet()
        elif choice == "7":
            os.system("cls")
            delete_planet()
        elif choice == "8":
            exit()
        else:
            invalid_choice_text()

#Clears the screen and does the menu function   
os.system("cls")
menu()


         
