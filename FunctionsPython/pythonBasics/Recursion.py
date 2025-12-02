#1. Print numbers from 1 to N using recursion.
def print_numbers(n:int):
    
    if n == 0:
        return
    print_numbers(n-1)
    print(n)
print_numbers(19)


#2. Calculate the sum of first N natural numbers using recursion.
def sum_of_natural_numbers(n:int):
    if n == 0:
        return 0
    else:
        add = n + sum_of_natural_numbers(n-1)
        return add
sum = sum_of_natural_numbers(20)
print(sum)


#3. Find the factorial of a number using recursion.
def factorial_of_number(number:int):
    if number == 0:
        return 1
    else:
        result = number * factorial_of_number(number - 1)
        return result 
factorial = factorial_of_number(6)
print(factorial)


#4. Reverse a string using recursion.
def reverse_string(string:str)->str:
    if len(string) == 0:
        return string
    else:

        reverse=reverse_string(string[1:]) + string[0]
        print(reverse)
        return reverse
reversed_string=reverse_string("Hello")
print("Reversed String :",reversed_string)


#5. Check if a number is a power of 2 using recursion.
def power_of_two_or_not(n):
    if n == 1:
        return "Yes,Given number is power of 2"
    elif n == 0 or n % 2 != 0:
        return "No,Given number is not power of 2"
    else:
        return power_of_two_or_not(n // 2)
result = power_of_two_or_not(128)
print(result)


