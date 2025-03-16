def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2  
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = list(map(int, input("Enter sorted elements separated by space: ").split()))
x = int(input("Enter the element to search: "))

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print("Element not found")
