#2.Function swapnumbers to swap two variables value
def swap_two_numbers(number1,number2):
    print(f"Before swap: number1 = {number1} and number2 = {number2}")
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    print("After swap:number1 = {number1} and number2 = {number2}")
# swap_two_numbers(10,20)
# swap_two_numbers(10.8,25.7)
# swap_two_numbers("Hello","world")   string not works in this method

#2.Function swapnumbers to swap two variables value(method-2)
def swap_values(value1,value2):
    print(f"Before swap: value1 = {value1} and value2 = {value2} ")

    temp = value1
    value1 = value2
    value2 = temp
    
    print(f"After swap: value1 = {value1} and value2 = {value2}")
#function call
swap_values("hello","world")
swap_values(True,False)
swap_values(24.5,86.9)

#2.Function swapnumbers to swap two variables value(method-3)
def swap_values_using_return(value1,value2):
    return value2,value1
#invocation
item1 = "hello"
item2 = "namaste"
print(f"Before swap: value1 = {item1} and value2 = {item2} ")
item1 , item2 = swap_values_using_return(item1,item2)
print(f"After swap: value1 = {item1} and value2 = {item2}")
