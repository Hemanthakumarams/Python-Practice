def demonstare_Arithmatic_operators():
    countofMangos,countofApples=10,3

    #Additional operator
    answer = countofMangos + countofApples
    print("Arithmatic operator:")
    print(f"Addition: {countofMangos} + {countofApples} = {answer}")

    #Substract
    answer = countofMangos - countofApples
    print(f"Substraction: {countofMangos} - {countofApples} = {answer}")

    #multiply
    answer = countofMangos * countofApples
    print(f"Multiply: {countofMangos} * {countofApples} = {answer}")
    
    #Division
    answer = countofMangos / countofApples
    print(f"Division: {countofMangos} / {countofApples} = {answer}")

    #Modulus
    answer = countofMangos % countofApples
    print(f"Modulus: {countofMangos} % {countofApples} = {answer}")

    #Floor Division
    answer = countofMangos // countofApples
    print(f"Floor Division: {countofMangos} // {countofApples} = {answer}")

    #Exponential
    answer = countofMangos ** countofApples
    print(f"Exponential: {countofMangos} ** {countofApples} = {answer}")



def demonstrate_relational_operator():
    #Relational Operator
    countofMangos,countofApples=10,3

    #Equal to
    answer = countofMangos == countofApples
    print("Relational Operators:")
    print(f"Equal to: {countofMangos} == {countofApples} -> {answer}")

    #Not equal to
    answer = countofMangos != countofApples
    print(f"Not equal to: {countofMangos} != {countofApples} -> {answer}")

    #Greater than
    answer = countofMangos > countofApples
    print(f"Greater than: {countofMangos} > {countofApples} -> {answer}")

    #Less than
    answer = countofMangos < countofApples
    print(f"Less than: {countofMangos} < {countofApples} -> {answer}")

    #Greater than or equal to
    answer = countofMangos >= countofApples
    print(f"Greater than or equal to: {countofMangos} >= {countofApples} -> {answer}")

    #Less than or equal to
    answer = countofMangos <= countofApples
    print(f"Less than or equal to: {countofMangos} <= {countofApples} -> {answer}")



def demonstrate_logical_operator():
    #Logical Operator
    isReady,isGood = True,False

    #And
    answer = isReady and isGood
    print("Logical Operators:")
    print(f"And: {isReady} and {isGood} -> {answer}")

    #Or
    answer = isReady or isGood
    print(f"Or: {isReady} or {isGood} -> {answer}")

    #Not
    answer = not isReady
    print(f"Not: not {isReady} -> {answer}")



def demonstrate_bitwise_operators():
    #Bitwise operator
    redTeamScore,whiteTeamScore = 5,2

    #And
    answer = redTeamScore & whiteTeamScore
    print("Bitwise Operator:")
    print(f"And: {redTeamScore} & {whiteTeamScore} -> {answer}")

    #Or
    answer = redTeamScore | whiteTeamScore
    print(f"Or: {redTeamScore} | {whiteTeamScore} -> {answer}")

    #xor
    answer = redTeamScore ^ whiteTeamScore
    print(f"xor: {redTeamScore} ^ {whiteTeamScore} -> {answer}")

    #not
    answer = ~redTeamScore 
    print(f"Or: ~{redTeamScore} -> {answer}")
x=demonstrate_bitwise_operators()
print(x)
    # #Left shift
    # answer = redTeamScore << whiteTeamScore
    # print(f"Left Shift: {redTeamScore} >> {whiteTeamScore} -> {answer}")

    # #Right Shift
    # answer = redTeamScore >> whiteTeamScore
    # print(f"Right Shift: {redTeamScore} >> {whiteTeamScore} -> {answer}")



def demonstrate_assignment_operators():
    #Assignment operators
    totalScore = 5

    #Assign
    answer = totalScore
    print("Assignment Operators:")
    print(f"Assign: Total Score = {answer}")

    #Add and Assign
    #totalScore = totalScore + 2
    totalScore += 2
    answer = totalScore
    print(f"Add and Assign: Total Score = {answer}")

    #Substract and Assign
    totalScore = totalScore - 2
    answer = totalScore
    print(f"Substract and Assign: Total Score = {answer}")

    #Multiply and Assign
    totalScore *=2
    answer = totalScore
    print(f"Multiply and Assign: Total Score = {answer}")

    #Divide and Assign
    totalScore /=2
    answer = totalScore
    print(f"Divide Assign: Total Score = {answer}")

    #Modulus and Assign
    totalScore %=2
    answer = totalScore
    print(f"Modulus and Assign: Total Score = {answer}")

    #Floor division and Assign
    totalScore //=2
    answer = totalScore
    print(f" Floor Division and Assign: Total Score = {answer}")

    #Exponential and Assign
    totalScore **=2
    answer = totalScore
    print(f"Exponential and Assign: Total Score = {answer}")



def operators_demonstrations():
    demonstare_Arithmatic_operators()
    demonstrate_relational_operator()
    demonstrate_logical_operator()
    demonstrate_bitwise_operators()
    demonstrate_assignment_operators()


# operators_demonstrations()



# Addition of two numbers
def add_two_numbers(number1,number2):
    sum = number1 + number2
    return sum

#Substract second argument from the first
def substraction_of_two_numbers(number1,number2):
    result = number2 - number1
    return result

#Multiply two intergers
def multiply_two_numbers(number1:int,number2:int) ->int:
    result = number1 * number2
    print(result)

#Division of two float numbers
def division_of_two_numbers(number1:float,number2:float) ->float:
    result = number1 / number2
    return result

#Modulus of two integers
def modulus_of_two_numbers(number1:int,number2:int) ->int:
    result = number1 % number2
    return result

#Average of four numbers
def average_of_numbers(number1,number2,number3,number4):
    result = (number1 + number2 + number3 + number4) / 4
    return result

#Both sum and product of two integers
def addition_multiplication_of_two_numbers(number1,number2):
    sum = number1 + number2
    product = number1 * number2
    return sum,product

#Find area of triangle
def area_of_triangle(base:float,height:float) ->float:
    result = (1/2) * base * height
    return result

#Check whether the given number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Given number is even"
    else:
        return "Given number is odd"

#Swap two numbers using arithmatic operators
def swap_two_numbers(number1,number2):
    print("Before swap:")
    print("Number1=",number1)
    print("Number2=",number2)
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    print("After swap:")
    print("Number1=",number1)
    print("Number2=",number2)

# add_two_numbers(10,20)
# substraction_of_two_numbers(20,30)
# multiply_two_numbers(10,5)
# division_of_two_numbers(10.5,3)
# modulus_of_two_numbers(10,3)
# average_of_numbers(10,20,30,40)
# addition_multiplication_of_two_numbers(20,10)
# area_of_triangle(10,20)
# check_even_or_odd(22)
# swap_two_numbers(15,30)

