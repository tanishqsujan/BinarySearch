def binarysearch(arr, l, r, x):
    while l <= r:
        mid= l + (r-1) //2
        if arr[mid]== x:
            return mid
        elif arr[mid] < x:
            l= mid + 1
        else:
            r= mid - 1
            
    return -1

arr= [10,22,35,40,53,69]
x= 53

result= binarysearch(arr, 0, len(arr), x)

if result!= -1:
    print("Element {} is present in index {}".format(x, result))
else:
    print("Element not found")
