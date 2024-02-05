#FINDING LARGEST NUMBER BY USER INPUT
import numpy as np

values =input("enter 5 elements of array : ")
lenarr = np.array([int(x) for x in values.split()[:5]])
#lenarr = np.array([12,34,56,78,999,123,456,789,909])
print("elements of array : ", lenarr)

if len(lenarr) < 1:
    print("please,enter atleast one value")
else:
    largest =lenarr[0]
    larposition = 0

largest =lenarr[0]
for i in range(1, len(lenarr) ):
    if (largest < lenarr[i]):
        largest =lenarr[i]
        larposition = i

print("largest number : ",largest)
print("index position : ",larposition)