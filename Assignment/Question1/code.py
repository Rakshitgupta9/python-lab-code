# Initialize the dictionary with the given set of key-value pairs
country_data = {
    "IN": {"name": "India", "capital": "Delhi", "population": 1320000000},
    "US": {"name": "America", "capital": "Washington", "population": 320000000},
    "AU": {"name": "Australia", "capital": "Canberra", "population": 24000000},
    "CA": {"name": "Canada", "capital": "Ottawa", "population": 940000},
}

# Function to view country data
def view_country_data():
    print("Country Codes : "," ".join(country_data.keys()))
    country_code = input("Enter country code: ")
    if country_code in country_data:
        country = country_data[country_code]
        print("Country name is:", country["name"])
        print("Country capital is:", country["capital"])
        print("Country population is:", country["population"])
    else:
        print("There is no country for country code", country_code)

# Function to add a country
def add_country():
    country_code = input("Enter country code: ")
    if country_code in country_data:
        print("Country code already exists.")
        return
    country_name = input("Enter country name: ")
    capital = input("Enter capital city: ")
    population = int(input("Enter population: "))
    country_data[country_code] = {"name": country_name, "capital": capital, "population": population}
    print(country_name, "added to the list")

# Function to delete a country
def delete_country():
    country_code = input("Enter country code to delete: ")
    if country_code in country_data:
        country_name = country_data[country_code]["name"]
        del country_data[country_code]
        print(country_name, "has been deleted.")
    else:
        print("Country code not found.")

# Main program loop
while True:
    print("\n--------------------------")
    print("SELECT AN OPTION:")
    print("view: View country names")
    print("add: Add a country")
    print("del: Delete a country")
    print("exit: Exit the program")
    print("--------------------------\n")
    choice = input("Your choice: ")

    if choice == "view":
        view_country_data()
    elif choice == "add":
        add_country()
    elif choice == "del":
        delete_country()
    elif choice == "exit":
        break
    else:
        print("Invalid choice. Please choose from 'view', 'add', 'del', or 'exit'.")

print("Exiting the program")
