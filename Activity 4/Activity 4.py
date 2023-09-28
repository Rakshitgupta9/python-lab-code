# linear search
list = [12,89,24,56,45,25,36,69,41]
value = 25
for i in range(len(list)):
    if list[i] == value:
        print("Linear Search: ",value," found at index ",i)
        break
else:
    print("Linear Search: ",value," not found in the list")



#binary search 
list1 = [12,18,23,35,65,78,88,99,100]
value1 = 23
left, right = 0, len(list1) - 1
while left <= right:
    mid = left + (right - left) // 2
    if list1[mid] == value1:
        print("Binary Search: ",value1," found at index ",mid)
        break
    elif list1[mid] < value1:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Binary Search: ",value1," not found in the list")
