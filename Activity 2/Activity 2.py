#LIST
list = [12,85,96,74,58]

#for loop
print("Iterating over a list:")
for item in list:
    print(item,end=" ")

#while loop
print("\nIterating over a list using a while loop:")
index = 0
while index < len(list):
    print(list[index],end=" ")
    index += 1



#DICTIONARY
dict = {'name': 'Rakshit' , 'age': 20, 'city': 'Jammu'}

#Items
print("\nIterating over a dictionary:")
for key, value in dict.items():
    print(key ,":",value)

#Keys
print("\nIterating over keys in the dictionary:")
for key in dict.keys():
    print(key)

#Values
print("\nIterating over values in the dictionary:")
for value in dict.values():
    print(value)
