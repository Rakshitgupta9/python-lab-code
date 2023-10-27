# Function to create a student record
def create_student_record():
    student_record = {}
    student_record['name'] = input("Enter student's name: ")
    student_record['roll_number'] = input("Enter student's roll number: ")
    student_record['age'] = input("Enter student's age: ")
    student_record['grade'] = input("Enter student's grade: ")
    return student_record

# Function to search for a student record by name
def search_student_by_name(student_records, name):
    for record in student_records:
        if record['name'].lower() == name.lower():
            return record
    return None

# Main program
student_records = []

while True:
    print("\nOptions:")
    print("1. Add a student record")
    print("2. Search for a student record")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        student_record = create_student_record()
        student_records.append(student_record)
        print("Student record added successfully!")
    elif choice == '2':
        search_name = input("Enter the name of the student you want to search for: ")
        found_student = search_student_by_name(student_records, search_name)
        if found_student:
            print("Student record found:")
            print("Name: " + found_student['name'])
            print("Roll Number: " + found_student['roll_number'])
            print("Age: " + found_student['age'])
            print("Grade: " + found_student['grade'])
        else:
            print("Student record not found.")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

print("Program exited.")
