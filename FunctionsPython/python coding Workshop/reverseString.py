#9.Function to reverse string
def reverse_string(string):
    length = len(string)
    reversed_string = ""
    for end in range(length-1,-1,-1):
        reversed_string += string[end]
    return reversed_string
#invokation
input1 = "Algorithm"
print(f"String = {input1}")
print(f"Reversed string = {reverse_string(input1)}")


#Another method of reverse string
def reverse(string):
    if string != None:
        return string[::-1]
    else:
        return "None is not supported"
#invokation
input1 = None
print(f"String = {input1}")
print(f"Reversed string = {reverse(input1)}")

input1 = "Algorithm"
print(f"String = {input1}")
print(f"Reversed string = {reverse(input1)}")

input1 = "12345"
print(f"String = {input1}")
print(f"Reversed string = {reverse(input1)}")