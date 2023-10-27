# Initialize an empty list to store the contact information as tuples
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    email = input("Enter the contact's email: ")
    phone = input("Enter the contact's phone number: ")
    contact = (name, email, phone)
    contacts.append(contact)
    print("Contact added successfully!")

# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, 1):
            name, email, phone = contact
            print(f"{i}. Name: {name}, Email: {email}, Phone: {phone}")

# Main menu
while True:
    print("\nOptions:")
    print("1. Add a new contact")
    print("2. Display all contacts")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        print("Program exited.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
