#Linear Search
def linear_search(list,search):
    for i in range(len(list)):
        if list[i]==search:
            print("Element is found at index ",i)
            break
    else:
        print("Element not found")

#Binary Search
def binary_searh(list,search):
    left=0
    right=len(list)-1
    while left<=right:
        mid=left+(right-left)//2
        if list[mid]== search:
            print("Element found at the index -",mid)
            break
        elif list[mid]<search:
            left=mid+1
        else:
            right=mid-1
    else:
        print('Element not found')

#Linear Search
list=[24,26,95,45,69,88,12]
print("Given List is - ",list)
number=int(input("Enter the number to find in the list : "))
linear_search(list,number)

#Binary Search
list1=[12,24,35,42,50,69,88]
print("Given List is - ",list1)
number1=int(input("Enter the number to find in the list : "))
binary_searh(list1,number1)
