#13.Function search number in sorted integer array
def search(array , key):
    leftIndex = 0
    rightIndex = len(array)-1
    found = False

    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2

        if array[midIndex] == key:
            found = True
            break
        
        if array[midIndex] > key:
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1
    return found
#function Invocation
array = [1,3,4,5,8,9,10,30]
key = 6
result = search(array,key)
if result:
    print("Number is found")
else:
    print("Number is not found")