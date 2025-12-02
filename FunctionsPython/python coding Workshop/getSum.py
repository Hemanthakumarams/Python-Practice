#1.Function getSum to get sum of numbers
def get_sum(number1,number2):
    result = number1 + number2
    return result

#function call
sum = get_sum(10,30)
print(f"Sum of two numbers : {sum}")

sum1 = get_sum(10.5,23.89)
print(f"Sum of two numbers : {sum1}")

sum2 = get_sum("Hemanth","Kumar")
print(f"Sum of two values : {sum2}")

sum3 = get_sum(False,True)
print(f"Sum of two numbers : {sum3}")