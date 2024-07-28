#Question 1: Write a program which takes a number from user and print all odd numbers in between 2 and N, but print 2 first
#Time complexity:O(n)
#Space complexity:O(1)
num = int(input("Enter the number:"))
# iterating each number in list
for i in range(2, num+1):
    # checking condition
    if(i==2):
        print(i)
    elif (i % 2 != 0):
        print(i)