#ARITHMETIC OPERATIONS USING NUMPY
import numpy as np

operation =input("Enter operation ('add =1 ','substract =2 ','multiply=3','divide=4')")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number"))
def calculator(operation ,num1,num2):
     if operation == '1':
         result =np.add(num1,num2)
     elif operation == '2':
         result =np.subtract(num1,num2)
     elif operation == '3':
         result =np.multiply(num1,num2)
     elif operation == '4':
          if num2==0:
              return "error : cannot be divide by zero"
          result = np.divide(num1,num2)
     else:
         return "error: Invalid operation"

     return result

result = calculator(operation,num1,num2)
print("Result : ",result)

