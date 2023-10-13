#normal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print("Original matrix")
for row in matrix:
    print(row)
    
k = int(input("Enter the row you want to reverse: "))

for i in range(k - 1, len(matrix), k):
    matrix[i] = matrix[i][::-1]

print("After reversing every", k, "th row, the matrix is:")
for row in matrix:
    print(row)
