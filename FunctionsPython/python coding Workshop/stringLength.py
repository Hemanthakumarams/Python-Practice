#7.Function to find the length of the string 
def string_length(string):
    counter = 0
    if string != None:
        for character in string:
            counter += 1
    return counter
#invocation
input1 = None
length=string_length(input1)
print(f"Length of the {input1} is {length}")

input2 = "Algorithm365"
length=string_length(input2)
print(f"Length of the {input2} is {length}")

input3 = "425637"
length=string_length(input3)
print(f"Length of the {input3} is {length}")


#7.Function to find the length of the string using built-in function
def length_of_string(string):
    if string != None:
        length = len(string)     #len() is a built-in function
    else:
        length = "None is not Support"
    return length
#invocation
result = length_of_string(None)
print(result)

result = length_of_string("hello")
print(result)

result = length_of_string("1221")
print(result)