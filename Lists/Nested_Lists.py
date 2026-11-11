# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(f'original matrix: {mat}')
print(f'2row and 3 columns from the matrix: {mat[1][2]}')

# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.

matrix=[]
print('Enter 3 number seperated by space for each row')

for i in range(3):
    rows=list(map(int,input(f"enter numbers for row {i+1} : ").split()))
    matrix.append(rows)
print(f'3*3 matrix is : {matrix}')



# transpose matrix using list comprehension

trans2=[[matrix[j][i] for j in range(3)] for i in range(3)]

print(f'matrix transpose using list comprehension: {trans2}')

# trasnpose of matrix using zip()

trans3 = [list(row) for row in zip(*matrix)]
print(f'matrix transpose using zip(): {trans3}')