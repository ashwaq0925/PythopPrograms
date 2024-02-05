#MULTIPLY MATRICES BY TAKING USER INPUT

import numpy as np

def matrix_input(rows,cols):
    matrix=[]
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f'Enter values for elements at position((i +1),(j + 1) : '))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)


rows1 = int(input("enter the number of rows for the first matrix : "))
cols1 =int(input("enter the number of cols for the first matrix :"))

rows2 = int(input("enter the number of rows for the second matrix : "))
cols2= int(input("enter the number of cols for the second matrix : "))

if(cols1!=rows2):
    print("Multipication is not possible ")
else:
    matrix1 = matrix_input(rows1,cols1)
    matrix2 = matrix_input(rows2,cols2)

    result = np.dot(matrix1,matrix2)

    print("\n result matrix",result)