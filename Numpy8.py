#FINDING THE SAMLLEST NUMBER
import numpy as np

smallest=input("enter the values : " )

lenarr=np.array([int(x) for x in  smallest.split()])

print("elenents of array :" ,lenarr)

print("the smallest number is :",min(lenarr))