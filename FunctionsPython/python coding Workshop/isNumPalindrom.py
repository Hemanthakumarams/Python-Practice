def isNumPalindrom(x):
    if x < 0 or (x % 10 == 0 and x != 0 ):
        return False
    
    reversed = 0
    while x > reversed:
        reversed = reversed * 10 + x % 10
        x //= 10
    return x == reversed or x == reversed // 10
result = isNumPalindrom(1281)
if result:
    print("Yes!!, Given number is palindrome")
else:
    print("Given number is not a palindrome")