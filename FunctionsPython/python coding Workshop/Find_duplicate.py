def find_duplicate_elements(array:list)->int:
    dictionary = {}
    #case1: if array is epmty
    if len(array) == 0:
        print("Given array is Empty")
        return dictionary
    
    #case2: if array has only one element
    if len(array) == 1:
        print("Given array has only one element")
        return dictionary
    
    #case3:if array has duplicate elements
    for element in array:
        if element not in dictionary:
            dictionary[element] = 1
            continue

        if element in dictionary:
            dictionary[element] += 1

    #case4:if array does not have duplicate elements
    result = False
    for item in dictionary.values():
        if item <= 1:
            result = False
        else:
            result = True
            break
    print(dictionary)
    return result

#function invocation
# array = []
# array = [2]
# array = [1,2,2,3,3,4,1,4,5,6,3,1,2]
array = [1,2,3,4,"a","a"]
# array = [1,2,3,4]
output = find_duplicate_elements(array)
if output:
    print("Given array has duplicate elements")
else:
    print("Given array does not have duplicate elements")




#Without using extra space
def find_duplicate_without_extra_memory(array:list)->list:
    pass