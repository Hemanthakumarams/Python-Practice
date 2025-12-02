#12.Function to find maximum and minimum value in an array using for loop
def find_MinMax(array):
    min=array[0]
    max =array[0]

    for item in array:
        if item > max:
            max = item
        if item < min:
            min = item
    return min,max

array = [10,20,90,50,5,35,20,-3]
min_value,max_value=find_MinMax(array)
print(f"Minimum value = {min_value} and Maximum value = {max_value}")

#12.Function to find maximum and minimum value in an array using while loop
def find_min_max(array):
    max = array[0]
    min = array[0]
    index = 1
    while index <= len(array)-1:
        if array[index] > max:
            max = array[index]
        if array[index] < min:
            min = array[index]
        index += 1
    return max,min
# function call
array = [10,20,90,50,5,35,20]
print(find_min_max(array))


