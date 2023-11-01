# 1. WAP for performing type conversions
# Integer to float
integer_num = 42
float_num = float(integer_num)
print("Integer to float:", integer_num, "->", float_num)
# Float to integer
float_num = 3.14
integer_num = int(float_num)
print("Float to integer:", float_num, "->", integer_num)
# String to integer
string_num = "123"
integer_num = int(string_num)
print("String to integer:", "'", string_num, "'", "->", integer_num)
# String to float
string_num = "3.14"
float_num = float(string_num)
print("String to float:", "'", string_num, "'", "->", float_num)
# Integer to string
integer_num = 42
string_num = str(integer_num)
print("Integer to string:", integer_num, "->", "'", string_num, "'")
# Float to string
float_num = 3.14
string_num = str(float_num)
print("Float to string:", float_num, "->", "'", string_num, "'")
# String to boolean
string_bool = "True"
boolean_val = bool(string_bool)
print("String to boolean:", "'", string_bool, "'", "->", boolean_val)
# Boolean to string
boolean_val = True
string_bool = str(boolean_val)
print("Boolean to string:", boolean_val, "->", "'", string_bool, "'")








#2. WAP to swap two numbers without using temp variable
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Before swapping: First number = ",num1,"Second number = ",num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After swapping: First number = ",num1,"Second number = ",num2)







#3. WAP to build a mini calculator
while True:
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("Result: ", result)
    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print("Result: ", result)
    elif choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print("Result: ", result)
    elif choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
        print("Result: ", result)
    elif choice == "5":
        break
    else:
        print("Invalid option")








#4. String Slicing and string operations
str = "Hello, World!"
substring = str[7:12]
print(substring)
str += " How are you?"
print(str)
length = len(str)
print(length)
print("Uppercase:", str.upper())
print("Lowercase:", str.lower())








#5. WAP to perform following operation a string:   1. find the length     2. lowercase the string    3. uppercase the string    
# 4. slicing method    5. find the index of character from the string      6. count a character’s occurrence
str = "I'm from Miet"
length = len(str)
print("1. Length of the string:", length)
lowercase_string = str.lower()
print("2. Lowercase string:", lowercase_string)
uppercase_string = str.upper()
print("3. Uppercase string:", uppercase_string)
sliced_string = str[2:8]
print("4. Sliced string:", sliced_string)
char_to_find = "r"
char_index = str.index(char_to_find)
print("5. Index of 'r' in the string:", char_index)
char_to_count = "m"
char_count = str.count(char_to_count)
print("6. Occurrence of 'm' in the string:", char_count)






#6. WAP to swap two numbers by using bitwise without 3rd operator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Original numbers: num1 =", num1, "num2 =", num2)
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print("Swapped numbers: num1 =", num1, "num2 =", num2)






#7. Perform Following operations on matrix    i. Iterate each element     ii. Add each element    iii. Add even numbers in the matrix   iv. Add numbers on even indexes
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]
]
print("i. Iterate each element:")
for row in matrix:
    for element in row:
        print(element, end=" ")
print("\n\nii. Add each element:")
a = 0
for row in matrix:
    for element in row:
        a += element
print("Sum of all elements:", a)
print("\niii. Add even numbers in the matrix:")
a = 0
for row in matrix:
    for element in row:
        if element % 2 == 0:
            a += element
print("Sum of even numbers:", a)
print("\niv. Add numbers on even indexes:")
a = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i + j) % 2 == 0:
            a += matrix[i][j]
print("Sum of numbers on even indexes:", a)







#8. WAP toggle the Kth bit by using bitwise operator
num = int(input("Enter a number: "))
k = int(input("Enter the position (K) of the bit to toggle: "))
print("Original number:", num)
mask = 1 << k+1
result = num ^ mask
print("The", k, "th bit has been toggled. Result:", result)






#9. WAP to unset the rightmost set bit by bit manipulation
a=int(input("Enter the number : "))
a=a&(a-1)
print("The number after unsetting the rightmost set bit", a)






#10. WAP to convert lowercase character to uppercase using bit opertaor
char = input('Enter a lower case letter: ')
a=ord(char)
a=a&(~(1<<5))
print(chr(a))







#11. Write a program to find area parameter of circle square and rectangle by user choice
def circle():
    r=int(input("Enter radius of Circle :"))
    area=3.14*r*r
    Parameter=2*3.14*r
    print("Area of circle with radius,",r,":",area,"\n")
    print("Parameter of circle with radius,",r,":",Parameter,"\n")
def square():
    side=int(input("Enter length of Side for Square :"))
    area=side**2
    perimeter=4*side
    print("Area of Square with side,",side,":",area,"\n")
    print("Parameter of Square with side,",side,":",perimeter,"\n")
def rectangle():
    l=int(input("Enter Length of Rectangle :"))
    b=int(input("Enter Breadth of Rectangle :"))
    area=l*b
    perimeter=(2*(l+b))
    print("Area of Rectangle with length,",l,"and breadth,",b,":",area,"\n")
    print("Parameter of Rectangle with length,",l,"and breadth,",b,":",perimeter,"\n")
while True:
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle ")
    print("4. Exit \n")
    ch=int(input("Enter Your choice : "))
    if ch==1:
        circle()
    elif ch==2:
        square()
    elif ch==3:
        rectangle()
    elif ch==4:
        break
    else:
        print("Invalid Choice")
    








#12. WAP to find whether a string contains vowels or not
#for loop
str = input("Enter the string: ")
flag = 0
for i in str:
    if i in "aeiouAEIOU":
        flag = 1
        break 
if flag == 1:
    print("It contains a vowel")
else:
    print("It doesn't contain any vowel")

#while loop
str = input("Enter the string: ")
flag = 0
index = 0
while index < len(str):
    if str[index] in "aeiouAEIOU":
        flag = 1
        break  
    index += 1
if flag == 1:
    print("It contains a vowel")
else:
    print("It doesn't contain any vowel")








#13 WAP to count the number of vowels
str = input("Enter the string: ")
flag = 0
index = 0
while index < len(str):
    if str[index] in "aeiouAEIOU":
        flag += 1
    index += 1
print("Number of Vowels in",str,"=",flag)
















"""
14.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of country stamps.
Find the total number of distinct country stamps?

Input Format :
The first line contains an integer N, the total numbe of country stamps.
The next N lines contains the name of the country where the stamp is from.

Output Format!
Output the total number of distinct country stamps on a single line
"""
n=int(input("Enter The Total number of country stamps : "))
country_stamp=set()
for i in range(0,n):
    country_name=input("Enter the "+ str(i+1) +" country stamp Name : ")
    country_stamp.add(country_name.upper())
print("Total Number Of Distinct Country Stamps : ",len(country_stamp))









#15. Given a list, the task is to write a Python Program to find the Index containing String?
list=['Rakshit',75,50,'Gupta','Py',69,88,'Miet']
for i,item in enumerate(list):
    if isinstance(item, str):
        print(i,end=" ")
    







"""
16. wap to print the following pattern
    * * *
    * * *
    * * *
    * * *
"""
for i in range(0,4):
    print("* * *")

r=4
c=3
for i in range(r):
    for j in range(c):
        print("*", end=" ")
    print()







#17. find runner up score in a list
n = int(input("Enter the number of participants: "))
scores = list(map(int, input("Enter the scores separated by space: ").split(",")))
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
runner_up_score = unique_scores[1]
print("Runner-up score:", runner_up_score)







#18. merge two dictonaries
dict1={"a":85,"b":89}
dict2={"b":69,"c":78}
dict={**dict1,**dict2}
print(dict)







#19. find longest word in the list
list=[]
n=int(input("Enter Number of elements for list : "))
for i in range(n):
    element = input("Enter Elements : ")
    list.append(element)   
longest=""
for j in list:
    if(len(j)>len(longest)):
        longest=j
print("The longest string is ",longest," and it's length is ",len(longest))
