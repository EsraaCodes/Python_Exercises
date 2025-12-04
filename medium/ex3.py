class Book:
    def __init__ (self,title,author,year,is_checked_out=False):
           self.title=title
           self.author=author
           self.year=year
           self.is_checked_out=is_checked_out
    def checkout(self):
          self.is_checked_out=True
    def return_book(self):
          self.is_checked_out=False
    def __str__(self):
          return f"{self.title} by {self.author} (Checked Out:{self.is_checked_out})"
class Library:
      def __init__(self,name):
            self.name=name
            self.books=[]
      def add_book(self,book):
            self.books.append(book)
      def list_books(self):
            for book in self.books:
                  print(book)
      def find_books(self,title):
            for book in self.books:
                  if book.title.lower()==title.lower():
                        return book
            return None
      def available_books(self):
            available=[]
            for book in self.books:
                   if not book.is_checked_out:
                     available.append(book)
            return available

b1=Book("1984","George Orwell",1949)
b2=Book("The alchemist","Paulo Coelho",1988)
lib=Library("City Library")
lib.add_book(b1)
lib.add_book(b2)
lib.list_books()
b1.checkout()
lib.list_books()
found=lib.find_books("1984")
print(found)
available=lib.available_books()
for book in available:
    print(f"Available: {book}") 

