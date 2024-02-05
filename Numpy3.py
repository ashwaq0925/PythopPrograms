#SORTING ARRAY ELEMENTS IN ARRAY ASCENDING AND DESCENDING ORDER
import numpy as hs

arr=hs.array([12,23333,544,7892,9887,4737,53737,647])
print("elements of array : ",arr)

arr.sort()
print("sorted array in ascending order : ",arr )

print("\n\n ****ANOTHER PROGRAM****\n\n")

arr2=hs.array([12,23333,544,7892,9887,4737,53737,647])
print("elements of array :",arr2)

arr2.sort()
descarr = arr2[::-1]
print("sorted array in descending order : ",descarr)