#FINDING NUMBERS IN ARRAY IS EVEN OR ODD
import numpy as np
evenArr = np.array([12,34,56,32,11,67,86,22,34,7,5,13])
print("the numbers in array are even;" ,evenArr)

for i in evenArr:
    if(i % 2==0):
        print(i,end = ' ')


print("\n\n****ANOTHER PROGRAM****\n\n")

oddArr =np.array([12,34,56,32,11,67,86,22,34,7,5,13])
print("the numbers in array are odd : ",oddArr)

for i in oddArr:
    if(i % 2!= 0):
        print( i,end=' ')

