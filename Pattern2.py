#PYTHON PROGRAM TO PRINT RIGHT HALF PYRAMID

def pattern(n):
    for i in range(1,n+1):
        print(" "*(n-1) + "$"*i)
n=int(input("enter number of rows : "))
pattern(n)