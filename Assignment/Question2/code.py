import re

# Function to accept full name
def get_full_name():
    while True:
        full_name = input("Type your full name: ")
        if len(full_name.split()) < 2:
            print("Please enter your full name!")
        else:
            return full_name

# Function to accept password
def get_password():
    while True:
        password = input("Type your password: ")
        if (
            len(password) < 8
            or not re.search(r'\d', password)
            or not re.search(r'[A-Z]', password)
        ):
            print("Password must be of 8 or more characters in length with at least 1 digit and 1 capital letter")
        else:
            return password

# Function to extract the first name
def extract_first_name(full_name):
    return full_name.split()[0]

# Main program
full_name = get_full_name()
password = get_password()
first_name = extract_first_name(full_name)

print(f"Hello {first_name}")
print("Thank you for joining us!")

