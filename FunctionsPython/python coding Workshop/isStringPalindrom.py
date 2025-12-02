#11.Function to return given string is palindrom or not
def isPalindrom(string):
    start = 0
    end = len(string)-1
    result =True

    while start < end:
        if string[start] != string[end]:
            result = False
            break
        start += 1
        end -= 1
    return result
#Function call
input1 = "malayalam"
input2 = "namaste"
input3 = "mom"
result = isPalindrom(input2)
if result:
    print("Given string is palindrom")
else:
    print("Given string is not palindrom")

#11.Function to return given string is palindrom or not method-2
def palindrom_or_not(string):
    rev_string = string[::-1]

    if string == rev_string:
        print("Given string is palindrom")
    else:
        print("Given string is not palindrom")
#function call
input1 = "racecar"
input2 = "namaste"
input3 = "dad"
palindrom_or_not(input1)
palindrom_or_not(input2)
palindrom_or_not(input3)