#10.Function to return sum of all elements in an array or list
def sum_of_items_in_array(array):
    sum = 0
    for item in array:
        sum += item
    return sum
# #invokation
input1 = [10,20,30,40]
print(f"Sum of items = {sum_of_items_in_array(input1)}")


#Function to return sum of all elements in an array or list another method
def sum_of_items_in_array(array):
    sum = 0
    length = len(array)
    for item in range(0,length):
        sum += array[item]
    return sum
#invokation
input1 = [15,20,25,30]
print(f"Sum of items = {sum_of_items_in_array(input1)}")