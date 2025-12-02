from abc import ABC,abstractmethod

#interface for borrowable items
class Borrowable(ABC):
    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

# interface for reservable items
class Reservable(ABC):
    @abstractmethod
    def reserve(self):
        pass

#class implementing both interfaces
class Book(Borrowable,Reservable):
    def __init__(self,title):
        self.title = title

    def check_out(self):
        print(f"Checking out book: {self.title}")
    
    def return_item(self):
        print(f"Returning book: {self.title}")

    def reserve(self):
        print(f"Reserve: {self.title}")

#examle usage
book = Book("Python Crash Course")
book.check_out()
book.return_item()
book.reserve()