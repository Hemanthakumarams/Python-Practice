from LibraryItemClass import LibraryItem
#child class
class Magzine(LibraryItem):
    def __init__(self, count, id ,name ,publisher ,issue_number):
        super().__init__(count, id)

        self.name = name
        self.publisher = publisher
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue number = {self.issue_number}")

    def check_out(self):
        print("Invoking chechout method in LibraryItem")