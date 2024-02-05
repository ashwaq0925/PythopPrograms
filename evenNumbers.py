# print("Natural numbers ")
# for i in range(1,101):
#     print(2 * i)



start_no=int(input("Enter the STARTING NUMBER :" ))
end_no=int(input("Enter the ENDING NUMBER : "))

for num in range(start_no ,end_no + 1):
    count = 0
    for i in range(2 ,(num //2 + 1 )):
        if(num % i == 0):
            count= count +1
            break
    if(count==0 and num != 0):
        print("%d" %num, end =' ' )

