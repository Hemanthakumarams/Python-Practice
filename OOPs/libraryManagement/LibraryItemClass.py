#we need to import this module for abstraction
from abc import ABC ,abstractmethod
#parent class-->abstract class
class LibraryItem(ABC):
    def __init__(self,count,id):
        self.count = count
        self.id = id

    def display_info(self):
        print(f"Count = {self.count}")
        print(f"Id = {self.id}")
        
    @abstractmethod
    def check_out(self):
        pass