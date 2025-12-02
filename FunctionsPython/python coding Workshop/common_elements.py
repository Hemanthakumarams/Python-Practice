#17.Function to print intersection or common elements of 2 integers in 2 array
def print_common_elements(array1,array2):
    for array1_index in range(0,len(array1),1):
        isFound = False
        for array2_index in range(0,len(array2),1):
            if array1[array1_index] == array2[array2_index]:
                isFound = True
                break
        if isFound:
            print(array1[array1_index])
#invocation
array1 = [1,2,3,4,7,9,8]
array2 =[1,2,7,8,6]
print_common_elements(array1,array2)