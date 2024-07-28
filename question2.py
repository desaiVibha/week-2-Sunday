#Question 2: Write a program that takes a number from the user and get the sum of the digits present in the number
""" Get the number
Declare a variable to store the sum and set it to 0
Repeat the next two steps till the number is not 0
Get the rightmost digit of the number with help of the remainder ‘%’ operator by dividing it by 10 and adding it to the sum.
Divide the number by 10 with help of ‘/’ operator to remove the rightmost digit.
Print or return the sum 
Time Complexity: O(log N)
Auxiliary Space: O(1)"""
n=int(input("Enter the number to find out the sum of its digits: "))
def getSum(n): 
    sum = 0
    while (n != 0): 
        sum = sum + int(n % 10) #extracting last digit and adding it to the sum
        n = int(n/10) #removing the rightmost digit from the number
    return sum
print(getSum(n))