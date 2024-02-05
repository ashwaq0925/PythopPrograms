#write a function to find factorial of anumber

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)


    number = int(input("enter any number"))
    result = factorial(number)
    print(f'factorial of {number} is {result}')