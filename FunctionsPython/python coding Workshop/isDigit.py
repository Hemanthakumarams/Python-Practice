#4.Function isDigit or isNumber to return true if it is a digit
def isDigit(number):
    isDigit = True
    for character in number:
        if character >= "0" and character <= "9":  # "0"--> take it as ASCII value| 0--> int value
            continue
        else:
            isDigit = False
            break
    return isDigit

#function invokation
result = isDigit("12212344")
if result:
    print("Yes, Given input is number")
else:
    print("No,Given input is not a number")