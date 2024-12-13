def two_sum(arr,target):
    array_length=len(arr)
    for i in range(array_length):
        for j in range(i+1,array_length):
            if arr[i]+arr[j]==target:
                return True
    return False
arr=[1,2,3]
target=int(input("enter a target: "))
if two_sum(arr,target):
    print("True")
else:
    print("False")
                 
