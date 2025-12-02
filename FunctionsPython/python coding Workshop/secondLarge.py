#15.Function to get second largest element in an integer array
def second_largest(list:list)->int:
    largest = list[0]
    second_largest = list[0]

    for element in list:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest and element != second_largest:
            second_largest = element
        elif largest == second_largest and element < largest:
            second_largest = element
    return second_largest
# list = [-1,-2,-3,-4,-5]
list = [10,20,30,40,50]
# list = [4,3,6,1,9,7,8]
# list = [10,9,8,7,6,5]
# print(second_largest(list))

#Another method
def get_second_largest(list):
    first_max = float('-inf')      #float('-inf')-->It will set variable to lowest possible value
    second_max = float('-inf')

    for element in list:
        if element > first_max:
            second_max = first_max
            first_max = element
        elif element > second_max:
            second_max = element
    return second_max
# list = [-7,-3,-1,-4,-5]
# list = [10,20,30,40,50]
# list = [4,3,6,1,9,7,8]
# list = [10,9,8,7,6,5]
print(get_second_largest(list))
        