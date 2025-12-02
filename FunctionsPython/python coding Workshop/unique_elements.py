#16.Function to print unique elements in an array
def print_unique_elements(array):
    for read_index in range(0,len(array),1):
        isDuplicate = False
        for compare_index in range(0,len(array),1):
            if read_index == compare_index:
                continue

            if array[read_index] == array[compare_index]:
                isDuplicate = True
                break
        if isDuplicate == False:
            print(array[read_index])
array = [1,4,2,3,1,4,7,5,6,4]
# array = [1,2,3,2,4,1]

print_unique_elements(array)