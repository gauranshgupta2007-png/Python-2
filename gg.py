class Library:
    def __init__(self,author,book_name,available = True):
     self.author = author
     self.book_name = book_name
     self.available = True
  
    def checkout(self):
      if self.available:
        self.available = False
        print("book checked out")
      else:
        print("book not available")
        
    def return_book(self):
     self.available = True
     print ("book returned")
  
    def display_book(self):
        status = "available" if self.available else "not available"
        print (f"book name:{self.book_name}, author:{self.author}, status:{status}")  
               
book1 = Library("python programming","Gauransh Gupta")
book2 = Library("data structure","anish SHirsat")

book1.display_book()
book1.checkout()
book1.display_book()

book1.return_book()
book1.display_book()
              
