from LibraryItemClass import LibraryItem
#child class
class Book(LibraryItem):
    def __init__(self,book_title,book_author,book_category,book_id,count,id):

        super().__init__(count ,id)

        self.__title = book_title
        self.__author = book_author
        self.__category = book_category
        self.__id = book_id

    def print_details(self):
        print(self.__title)
        print(self.__author)
        print(self.__category)
        print(self.__id)

    def get_title(self):
        return self.__title
    #method overloading
    def search(self,title,author=None):
        if author:
            print(f"Searching by title and author: {title} ,{author}")
        else:
            print(f"Searching by title: {title}")

    def check_out(self):
        print("Invoking chechout from child class book")