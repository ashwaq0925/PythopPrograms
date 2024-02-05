import logging

a=int(input("Enter first number"))
b=int(input("enter second number"))


if a>b:
    logging.debug("inside if block")
    print(f'{a} is max')
else:
    logging.debug("inside else block")
    print(f'{b} is min')