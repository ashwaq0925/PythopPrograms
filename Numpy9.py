# creating matrices 2*2 and 3*3

import numpy as np

materix1 = np.array([[1,2],
                    [5,9]])
#print("2*2 matrix : \n", materix1)


matrix2 = np.array([[1,2,3],
                   [2,6,8],
                   [8,5,2]])

#print("3*3 matrix : \n", matrix2)

matrix3 = np.array([[1,2],
                    [3,4]])

matrix4 = np.array([[10,30,20],
                    [50,85,63],
                    [23,32,21]])

result1 = np.dot(materix1,matrix3)
result2 = np.dot(matrix2,matrix4)

print("matrix1 * matrix3 : \n",result1)
print("matrix2 * matrix4 : \n",result2)