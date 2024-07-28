# Question 5: Write a program where you are given strings and your task is to concatenate them and return the concatenated string
def remove(string):
    return string.replace(" ", "") 
string = input("Input a series of strings to remove whitespaces from it: ")
print(remove(string))