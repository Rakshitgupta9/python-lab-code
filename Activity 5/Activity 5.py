# #normal
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]

# print("Original matrix")
# for row in matrix:
#     print(row)
    
# k = int(input("Enter the row you want to reverse: "))

# for i in range(k - 1, len(matrix), k):
#     matrix[i] = matrix[i][::-1]

# print("After reversing every", k, "th row, the matrix is:")
# for row in matrix:
#     print(row)




# #with functions
# def reverse_matrix(matrix,k):
#     for i in range(k-1,len(matrix),k):
#         matrix[i] = matrix[i][::-1]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]

# print("Original matrix")
# for row in matrix:
#     print(row)

# k = int(input("Enter the row you want to reverse: "))
# reverse_matrix(matrix,k)

# print("After reversing every", k, "th row, the matrix is:")
# for row in matrix:
#     print(row)




# # Get the dimensions of the matrix from the user
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# # Initialize an empty matrix
# matrix = []

# # Get input values from the user and populate the matrix
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         value = int
#         (input(f"Enter the value at row {i+1}, column {j+1}: "))
#         row.append(value)
#     matrix.append(row)

# # Display the matrix
# print("Matrix:")
# for row in matrix:
#     print(row)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print("Original matrix")
for row in matrix:
    print(row)

s = 0

for r in matrix:
    for i,c in enumerate(r):
        print(i,c)


print("\nSum of the even index in the matrix is ",s)



