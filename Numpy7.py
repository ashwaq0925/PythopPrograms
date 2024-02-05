#PROGRAM FOR EVEN OR ODD USING USERINPUT
import numpy as np
evenodd =input("enter the 5 values : ")
lenarr=np.array([int (x) for x in evenodd.split()])
#lenarr =np.array([11,22,33,44,55,13,17,23])
evenarrsum = 0
oddarrsum = 0
print("elements of array : ", lenarr)

if len(lenarr) < 1:
    print("please,enter atleast one value")
else:
    largest =lenarr[0]


for i in range(len(lenarr)):
   if (lenarr[i] % 2==0):
       evenarrsum += lenarr[i]
   else:
       oddarrsum +=lenarr[i]



print("the sum of even numbers : ",evenarrsum)
print("the sum of odd numbers : ",oddarrsum)

