from BookClass import Book

class Ebook(Book):
    def __init__(self,file_formate,book_title,book_author,book_category,book_id,count,id):
        super().__init__(book_title,book_author,book_category,book_id,count,id)
        
        self.file_formate = file_formate

    def display_info(self):
        super().display_info()
        print(f"File formate = {self.file_formate}")