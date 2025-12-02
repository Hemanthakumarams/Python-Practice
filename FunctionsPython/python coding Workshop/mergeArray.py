#14.Function to merge two array and return combined output in first array
def merge_two_array(array1:list,array2:list)->list:
    array1 = array1 + array2
    return array1
#invocation
array1 = [10,20,30]
array2 = [40,50]
print(merge_two_array(array1,array2))



#Another method
def mergeList(list1:list,list2:list)->list:
    for item in list2:
        list1.append(item)     #append->add the item at the end of the list
#invocation
list1 = [1,2,3,4]
list2 = [5,6,7]
mergeList(list1,list2)
print(list1)