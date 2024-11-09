tuple  = (2,3,4,5,6,7,8,9,0,1,235,45,31,94,904,325,987,1433,42374)
sum = 0
for i in tuple :
    sum = sum + i
print("The sum of all the numbers in the tuple is : ", sum)
total_numbers = len(tuple)
avg = sum / total_numbers
print("the average of all numbers are : " , avg)