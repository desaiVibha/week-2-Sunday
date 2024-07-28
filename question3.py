#You are provided an array of integers and you have to increment all array elements by 1 and then print whole array.
def arrayInc(arr):
    for i in range(0, len(arr)):
        arr[i]=arr[i]+1
    return arr
print(arrayInc([1,2,3,4,5]))
    
