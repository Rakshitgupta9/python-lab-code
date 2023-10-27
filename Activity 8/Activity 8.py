def ctof(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def ftoc(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = ctof(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = ftoc(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Goodbye!")
