def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

def is_armstrong_number(number):
    temp = number
    num_digits = len(str(number))
    armstrong_sum = 0

    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10

    return armstrong_sum == number

result = max_of_three(45 , 69 , 51)
print(f"The largest number among (45 , 69 , 51) is: {result}")

number_to_check = int(input("Enter number to check : ")) 
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")
