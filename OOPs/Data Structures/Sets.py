enrolled_students_name = {"Hemanth","Jayanth","Adarsh","Manju"}
Paid_Students = {"Hemanth","Adarsh","Karthik"}
def students_data_analysis():
    #Students who enrolled in the course and also paid the fees
    #They must be present in both the list
    enrolled_and_Paid = enrolled_students_name & Paid_Students
    print("List of all enrolled and Paid students:")
    print(enrolled_and_Paid)

    #All students list
    all_students = enrolled_students_name | Paid_Students
    print("All Students list:")
    print(all_students)

    #unpaid students list
    un_paid_students = enrolled_students_name - Paid_Students
    print("Unpaid Students list:")
    print(un_paid_students)

    #Paid studentes but not enrolled
    yet_to_enrolled_but_paid = Paid_Students - enrolled_students_name
    print("Fees paid but not enrolled students list")
    print(yet_to_enrolled_but_paid)

    call_from_customer_care = enrolled_students_name ^ Paid_Students
    print("Student who either not paid or not enrolled students list:")
    print(call_from_customer_care)

if __name__ == "__main__":
    print("Welcome To Algorithms365")
    students_data_analysis()