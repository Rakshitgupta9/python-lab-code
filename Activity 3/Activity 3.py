str = "Welcome to Python world"

# Count the number of alphabets in the given string.
print("Number of alphabets in the string: ",len(str))

# To extract characters in the given, range from the given string
start = 3
end = 10
print("Characters in the range ",start," - ",end," : ",str[start:end])

# Check if the string is alphanumeric or not.
check = str.isalnum()
if check==True:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")
