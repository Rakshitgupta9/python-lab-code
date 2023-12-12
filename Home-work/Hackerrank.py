#1
print("Hello, World!")

	


	
#2	
n = int(input().strip())

if n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")






#3
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)




#4
a = int(input())
b = int(input())
print(a//b)
print(a/b)







#5
n = int(input())
for i in range(n):
    print(i**2)
	




	
	
#6
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap=True
    return leap
year = int(input())
print(is_leap(year))








#7
n = int(input())
for i in range(1,n+1):
    print(i,end="")








#8
x = int(input())
y = int(input())
z = int(input())
n = int(input())
cord=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                cord.append([i,j,k])
print(cord)







#9
n = int(input())
arr = map(int, input().split())
arr=sorted(arr, reverse=True)
unique=list(set(arr))
print(unique[1])









#10
n = int(input())
list=[]
for i in range(n):
    op=input().split()
    
    if op[0]=="insert":
        i,e=map(int,[op[1], op[2]])
        list.insert(i,e)
    elif op[0]=="print":
        print(list)
    elif op[0]=="remove":
        e=int(op[1])
        list.remove(e)
    elif op[0]=="append":
        e=int(op[1])
        list.append(e)
    elif op[0]=="sort":
        list.sort()
    elif op[0]=="pop":
        list.pop()
    elif op[0]=="reverse":
        list.reverse()
		
		







#11
n = int(input())
integer_list = map(int, input().split())

tup=tuple(integer_list)
print(hash(tup))








#12
def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a


line = input()
result = split_and_join(line)
print(result)
    
	
	







#13
py=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    py.append([name,score])
sc=[]
name=[]
for j in py:
    sc.append(j[1])
sc=sorted(list(set(sc)))
for j in py:
    if j[1]==sc[1]:
        name.append(j[0])
name.sort()
for i in name:
    print(i)
	






	
	
	
	
	
#14
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
std=student_marks[query_name]
avg=0
for i in std:
    avg+=i
avg=avg/len(std)
print("%.2f" %avg)









#15
n = int(input())
l = []

for i in range(n):
    x = input()
    if '.' in x:
        try:
            float_value = float(x)
            l.append("True")
        except ValueError:
            l.append("False")
    else:
        l.append("False")

for i in l:
    print(i)
	








#16
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
first_name = input()
last_name = input()
print_full_name(first_name, last_name)
	







#17
def mutate_string(string, position, character):
    string=string[:position]+character+string[position+len(character):]
    return string
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)









#18
def count_substring(string, sub_string):
    oc=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            oc += 1
    return oc
string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)








#19
s = input()
print(any(str.isalnum() for str in s))
print(any(str.isalpha() for str in s))
print(any(str.isdigit() for str in s))
print(any(str.islower() for str in s))
print(any(str.isupper() for str in s))









#20
import textwrap
def wrap(string, max_width):
    word=textwrap.wrap(string, width=max_width)
    result="\n".join(word)
    return result
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)









#21
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")
n = int(input())
print_formatted(n)







#22
def swap_case(s):
    new=""
    for i in s:
        if i.isupper():
            new+=i.lower()
        else:
            new+=i.upper()
    return new
s = input()
result = swap_case(s)
print(result)








#23
i=input()
eval(i)






#24
x, k = map(int, input().split())
polynomial = input()
result = eval(polynomial.replace('x', str(x)))
if result==k:
    print(True)
else:
    print(False)
	
	
	
	

#25
def solve(s):
    l=s.split(' ')
    l1=[]
    for i in l:
        i=i.capitalize()
        l1.append(i)
    s=" ".join(l1)
    return s
