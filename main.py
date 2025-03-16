def small(num, left= None, right= None):
    if left is None and right is None:
        (left, right)= (0, len(num) - 1)

    if left > right:
        return left
    mid= left + (right - left)// 2
    
    if num[mid]== mid:
        return small(num, mid+1, right)
    else:
        return small(num, left, mid-1)
    
if __name__== "__main__":
    num= [0, 1, 2, 6, 9, 11, 15]
    print("The smallent element is ", small(num))