# names = ["Alice","Bob","Charlie"]
# for index,name in enumerate(names,start=1):
#     print(f"Index {index} : {name}")

# for number in range(10):
#         if number == 3:
#             continue
#         print(number)

# count = 0
# while (count <=10):
#     if count == 3:
#         count+=1
#         continue
#     print(count)
#     count+=1


#1. Write a Python program using a for loop to print numbers from 1 to 10.
for number in range(1,11):
    print(number)


#2. Write a Python function using a while loop to count down from 5 to 1.
def count_down(count):
    while (count >= 1):
        print(count)
        count-=1
# count_down(5)


#3. Write a Python function that asks for user input until the word 'exit' is entered.
def user_input():
    while True:
        String = input("Enter a String : ")
        if (String == "exit"):
            print("Bye...")
            break
            
# user_input()


#4. Create a Python function using a for loop and range() to print even numbers from 2 to 20.
def even_numbers():
    print("Even numbers:")
    for number in range(2,21):
        if number % 2 == 0:
            print(number)

# even_numbers()


#5. Write a program that iterates over a list of names and prints each with a serial number using enumerate().
numbers = ["one","two","three","four","five","six"]
for index,number in enumerate(numbers,start=1):
    print(f"{index} --> {number}")


#6. Simulate a do-while loop in Python that asks for a number until the user enters a negative number.
while True:
    number = int(input("Enter a number : "))
    if number < 0:
        print("You entered negetive number")
        break


#7. Create a Python program that uses a nested loop to print the multiplication table from 1 to 5.
for a in range(1,6):
    print(f"Multiplication table of {a}")
    for b in range(1,11):
        print(f"{a} x {b} = {a*b}")


#8. Write a Python function that breaks the loop when the input number is divisible by 7.
def divisible_by_seven_break():
    while True:
        number = int(input("Enter a number : "))
        if number % 7 == 0:
            print(f"Number {number} is divisible by 7")
            break
# divisible_by_seven_break()


#9. Write a Python program using continue to skip numbers divisible by 3 from 1 to 15.
for number in range(1,16):
    if number % 3 == 0:
        continue
    print(number)


#10. Write a Python program to iterate over two lists using zip() and print the paired elements.
goats = ["Virat","Rohith","ABd","Rahul","Gayle"]
jesry_number = [18,45,17,1,333]
for player,number in zip(goats,jesry_number):
    print(f"{player} Jersy number is {number}")
