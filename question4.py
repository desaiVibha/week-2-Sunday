# Question 4: Write a program where you are given two strings S1 and S2. 
# You need to return a string which is the concatenation of both the given  strings.
s1=input("Enter a string: ")
s2=input("Enter another string to concatenate with the previous string:")
def strConcat(s1, s2):
    s3=s1+s2
    return s3
print(strConcat(s1,s2))