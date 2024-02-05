#PATTERN PROGRAM TO PRINT HALF PYRAMID
def pattern(n):
    for i in range(1, n+1):
        print("*" * i)

n = int(input("Enter the number of rows: "))
pattern(n)

#PATTERN PROGRAM TO PRINT HALF PYRAMID REVERSE ORDER
def pattern(n):
    for i in range(n):
        print("*" *(n-i))
pattern(n)