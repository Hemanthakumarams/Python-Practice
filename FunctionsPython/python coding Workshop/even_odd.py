#3.Function isEven return True otherwise False
def isEven_or_odd(number:int) ->bool:
    if number % 2 == 0:
        return True
    else:
        return False
result = isEven_or_odd(4)
print(result)