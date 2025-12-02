# # x=10
# # print(x)


# def hello():
#     x= 1

#     while(True):
#         if x==5:
#             print("hello")
#             return
        
#         if x == 4:
#             break

#         x += 1

#     print("hi")

# hello()

# x=10
# y=10
# if x==y:
#     print("yes")
# else:
#     print("no")





# import sys
# nums = list(map(int, sys.stdin.readline().strip().split()))
# target = int(sys.stdin.readline().strip())
def search_element(nums,target):
    #case1:If list is empty
    if len(nums) == 0:
        return "List is Empty"

    # case2: search the elements
    for number in range(0,len(nums)):
        if nums[number] == target:
            return number
    
    #case3:if target is not found
    return -1
    
nums = [1,1,3,0,5,3,5,4,2]
target = 0

# print(search_element(nums, target), end="")



def search_element(nums,target):
    #case1:If list is empty
    if len(nums) == 0:
        return "List is Empty"

    # case2: search the elements
    index = 0
    while index < len(nums):
        if nums[index] == target:
            return index
        index += 1
    
    #case3:if target is not found
    return -1
    
nums = [1,1,3,0,5,3,5,4,2]
target = 5

# print(search_element(nums, target), end="")







class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    def show(self):
        pass

# x = D()
# x.show()


s = "xyx"
result = []

# Single characters
for ch in s:
    result.append(ch)

# Pairs (with repetition)
for i in s:
    for j in s:
        result.append(i+j)

# Include empty string
result.append("")

# print(",".join(result))



def palindrome(n,s):
    list = []
    for x in s:
        for y in s:
            list.append(x+y)

    print((",".join(list)))


# palindrome(4,"hema")



# Function for combinations with repetition
def combinations_with_repetition(s, length, prefix=""):
    if length == 0:
        print(prefix)
        return
    for ch in s:
        combinations_with_repetition(s, length - 1, prefix + ch)

# Function for permutations without repetition
def permutations_without_repetition(s, prefix=""):
    if len(s) == 0:
        print(prefix)
        return
    for i in range(len(s)):
        # pick character at index i, remove it, and recurse
        remaining = s[:i] + s[i+1:]
        permutations_without_repetition(remaining, prefix + s[i])


# Example usage
s = "ABCA"

# print("Combinations with repetition (length=2):")
# combinations_with_repetition(s, 3)

# print("\nPermutations without repetition:")
# permutations_without_repetition(s)

my_set = set()
my_set.add(10)
my_set.add(12)
my_set.add(14)
my_set.add(10)
# print(set)




def generate_with_repetition(s, prefix="", length=0, max_length=None):
    
    if length > 0:
        l.add(prefix)

    if length == max_length:   # stop when max length reached
        return l

    for i in range(len(s)):
        generate_with_repetition(s, prefix + s[i], length + 1, max_length)

# Example usage
s = "ABC"
l = set([])

# res = generate_with_repetition(s, max_length=len(s))
# # my_set = set(l)
# print(l)




def generate_with_repetition(s, prefix="", length=0, max_length=None, results=None):
    if results is None:
        results = []

    if length > 0:
        results.append(prefix)

    if length == max_length:   # stop when max length reached
        return results

    for i in range(len(s)):
        generate_with_repetition(s, prefix + s[i], length + 1, max_length, results)

    return results


# Example usage
# s = "ABC"
# res = generate_with_repetition(s, max_length=len(s))
# my_set = set(res)

# print("All with repetition:", res)
# print("Unique (set):", my_set)




def weird_or_not(n):
    if n % 2 != 0:
        print("Weird")
        
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not weird")
        
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
        
    elif n % 2 == 0 and n >20:
        print("Not Weird")

# if __name__ == '__main__':
    # n = int(input().strip())
    # weird_or_not(n)





def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

# print(fact(5))


def fact(n):
    print(f"Recursive function invoked with a number: {n}")
    if n <= 0:
        return n
    print("First recursive cal get invoked")
    result1 =fact(n-1) 
    print(f"Result1 value = {result1}")

    print("Second recursive call get invoked")
    result2 = fact(n-2)
    print(f"Result2 value = {result2}")

    answer = result1 + result2
    print(f"Answer value = {answer}")
    return answer

output = (fact(5))
print(output)