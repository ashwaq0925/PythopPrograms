#program to find the prime number
n = int(input(" enter a number : "))
if n>1:
    for i in range(2, n//2):
        if n%2==0:
            print("it is not a prime number : ", n)
        else:
            print("it is a prime number : ",n)
else:
    print("enter a valid number  ",n )


print("\n------------ANOTHER PROGRAM-----------------------\n")


# def isPrime(num):
#     for n in range(2,int(num **0.5) +1 ):
#         if num%n==0:
#             print("Number is not prime : ",num)
#         else:
#             print("Number is prime :" ,num)
#
# print(isPrime(int(input("enter a number : "))))

print("----------------ANOTHER PROGRAM---------------------------")
def is_prime(num):
    # If the number is less than or equal to 1, it's not prime
    if num <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            # If the number has a factor, it's not prime
            return False
    # If no factors were found, the number is prime
    return True

# Test the function with a few examples
for num in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")