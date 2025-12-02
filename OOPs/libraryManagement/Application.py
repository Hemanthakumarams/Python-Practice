from StudentClass import Student
from BookClass import Book
from EmployeeClass import Employee
from BookManagement import BookManagement
from MagzineClass import Magzine
from EBookClass import Ebook

def main():
    demo = 5

    new_student = Student()

    new_student.Name = "Hemanth"
    new_student.Age = 23
    new_student._Hometown = "Shivamogge"

    print(f"Student name {new_student.get_name()}")
    print(f"Student age {new_student.get_age()}")

    second_student = Student("Karthi",21,"MA","Bengaluru")

    print(f"Student name {second_student.get_name()}")
    print(f"Student age {second_student.get_age()}")

    book = Book("Wings of Fire","APJ","Autobiography",1,50,123)
    book.print_details()
    book.display_info()

    eBook = Ebook('PDF',"Wings of Fire","APJ","Autobiography",1,50,123)
    eBook.display_info()
    
    magzine1 = Magzine(100,124,'PCS tech week','Algo365',15)
    magzine1.display_info()

    #method overloading in python using default arguments
    book.search("PCS")
    book.search("DSA","Algo365")

    book_management = BookManagement()

    book_management.check_out(new_student,book)
    book_management.return_book(second_student,book)

def abstractDemo():
    book2 = Book("Wings of Fire","APJ","Autobiography",1,50,123)
    book2.display_info()
    book2.check_out()

    magzine2 = Magzine(100,124,'PCS tech week','Algo365',15)
    magzine2.display_info()
    magzine2.check_out()


if __name__ == "__main__":
    # main()
    abstractDemo()