#1.	Write a Python program to check if a number is positive, negative, or zero.
def positive_or_negetive_or_zero():
    number = 10

    if (number > 0):
        print("Number is positive")

    elif (number < 0):
        print("Number is negetive")

    else:
        print("Number is zero")
        
positive_or_negetive_or_zero()

#2.	Given a student’s score, write a program to print “Pass” if score ≥ 40, otherwise print “Fail”.
def student_result(marks):
    if (marks >= 90) :
        print("Distinction")
    elif (marks >=60):
        print("First Class")
    elif (marks >= 50):
        print("Second Class")
    elif (marks >= 40 ):
        print("Pass")
    else:
        print("Fail")

student_result(76)

#3.	Write a program that checks if a given year is a leap year.
def leapYear_or_not(year:int) ->str:
    if year % 4 == 0 or year % 40 == 0 or year % 400 ==0:
        print(f"Yes! {year} is a leap year")
    else:
        print(f"No! {year} is not a leap year")

leapYear_or_not(1900)


#4.	Given 3 integers, write a program to find the largest number using if-elif-else.
def largest_number(number1:int,number2:int,number3:int) ->int:
    if (number1 > number2) and (number1 > number3):
        print(f"Largest number is {number1}")
    
    elif (number2 > number3):
        print(f"Largest number is {number2}")
    
    else:
        print(f"Largest number is {number3}")
    
largest_number(2000,40,380)

#5.	Evaluate if a candidate passes technical round using:coding_skill ≥ 4,problem_solving ≥ 4,cs_fundamentals ≥ 4,(Use and operator)

def interview_selection(coding_skill,problem_solving,cs_fundamentals):
    if coding_skill >= 4 and problem_solving >=4 and cs_fundamentals >= 4:
        print("Congratulations! you are selected")
    
    else:
        print("You are not selected!")

interview_selection(4,5,4)


#6.	Check if a candidate meets communication and CGPA criteria:CGPA ≥ 7.0,	communication ≥ 3

def interview_qualifications(communication,CGPA):
    if communication >= 3 and CGPA >= 7.0:
        print("You are shortlisted for next round!")
    
    else:
        print("You are not sortlisted!")

interview_qualifications(4,7.5)


#7.	Based on inputs, decide hiring decision using nested if:Check technical first, then CGPA & communication

def interview_process(technical_skills,communication_skill,CGPA):
    if technical_skills >=4:
        if communication_skill >=3 and CGPA >= 7:
            print("Congratulations! you are selected")
        
        else:
            print("You are not selected")
        
    else:
        print("You are not selected in technical round")

interview_process(4,7,9)


#8.	Write a program to check if a number is divisible by both 3 and 5 using and.
def divisible_or_not(number):
    if number % 3 == 0 and number % 5 == 0:
        print(f"Yes number {number} is both divisible by 3 and 5 ")

    elif number % 3 == 0:
        print(f"Number {number} is divisible by 3.But not divisible by 5")

    elif number % 5 == 0:
        print(f"Number {number} is divisible by 5.But not divisible by 3")
    else:
        print(f"Number {number} is not divisible by 3 and 5")
divisible_or_not(33)


#9.print “Fast-Track” if CGPA greater than 9 or communication greater than or equal to 4
def or_operator_example(CGPA,communication_skill):
    if CGPA > 9 or communication_skill >= 4:
        print("Fast-Track")

or_operator_example(9,4)

#10.Write a program using not to check if a person is not eligible for a scholarship (i.e., CGPA < 6)
def not_operator_example(CGPA):
    if not (CGPA < 6):
        print("You are selected for scholership!!")
    else:
        print("You are not selected for scholership!!")
not_operator_example(5)

#Scholership Eligibility criteria
def scholership_eligibility(internals_marks,CGPA):
    if internals_marks >= 35 :
        print("Pass in internals")
        if CGPA >= 8:
            print("CGPA also satisfies")
            print("You are eligible for scholership!!")
        
        else:
            print("But CGPA is less than 8")
            print("So you are not eligible for scholership")
    
    else:
        print("You are not passed in internals test")
        print("So you are not eligible for scholership")

scholership_eligibility(39,9)


#Either marks in English or Maths greate than 90 print Merit
def marks_in_English_Maths(English_marks,Maths_marks):
    if English_marks >=90 or Maths_marks >=90:
        print("Merit")

marks_in_English_Maths(80,89)

#If we enter a number then get week
def get_week_str(day:int) ->str:
    match(day):
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid input"
        
get_week_str(5)
