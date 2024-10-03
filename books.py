# module for Books class and methods
import users # imports dictionary of users and data from 'users.py' 

class Book: # A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.
    def __init__(self): 
        self.library = {
            'The Great Gatsby' : {'F. Scott Fitzgerald' : ['Fiction', '1925', 'Available']},
            'The Color Purple' : {'Alice Walker' : ['Fiction', '1982', 'Available']},
            'Harry Potter' : {'J. K. Rowling' : ['Fantasy', '2000', 'Available']}
        }
        
    def get_library(self):  # getter method to access library 
        return self.library 
    
    # need to figure these 2 methods out : 
    def set_borrowed(self, title): # set method to change title to 'Borrowed'  
        library = self.get_library() 
        for author, lst in library[title].items():
            library[title][author][2] = 'Borrowed'
    
    def set_available(self, title): # set method to change title to 'Available' 
        library = self.get_library()
        for author, lst in library[title].items():
            library[title][author][2] = 'Available' 
    
    def add_book(self): # add a book to library 
        # user inputs data of book to add to library
        library = self.get_library()   # gets dicitonary 'library' to add book to 
        title = input("Enter Title of book to add: ")
        author = input("Enter author of book to add: ")
        genre = input("Enter the genre of the book to add: ") 
        publication_date = input("Enter publication date of book: ")     
        status = 'Available' 
        library[title] = {author.title() : [genre, publication_date, status]} # adds inputs to library dictionary, status auto set to 'Available'   
        print(f"{title} added to collection of books.") 
    # Complete ^    
    
    def borrow_book(self): # borrow a book from library     
        library = self.get_library()
        username = users.User().get_users() # instance of User to add book to 'borrowed books' list
        while True:
            title = input("Enter the title of the book you wish to borrow: ")  # title of book to borrow  
            if title in library:
                for name, lst in library[title].items():
                    if library[title][name][2] == 'Borrowed':
                        print("Sorry, but that title is already being borrowed.")
                    else:
                        self.set_borrowed(title)
                        print(f"{title} is now being borrowed.")
                        break
                break 
            else:
                print("Title not found in library.") 
                    
    def return_book(self): # return book, change status
        library = self.get_library() 
        username = users.User().get_users()
        while True:
            title = input("Enter title of book to return: ")
            if title in library:
                for name, lst in library[title].items():
                    if library[title][name][2] == 'Available':
                        print(f"{title} has already been returned and is Available.")
                    else: 
                        self.set_available(title)
                        print(f"{title} has been returned.")
                        break
                break 
            else:
                print("Title not found in library.")
            
    
    def search_book(self): # Search for book by title or author 
        library = self.get_library()
        title = input("Enter the title of the book you wish to find: ") 
        if title in library:
            for name, lst in library[title].items():
                print(f"'{title}', by {name}: Genre - {lst[0]}, Published - {lst[1]}, Status - {lst[2]}") 
        else:
            print("Sorry, that title is not in our library.")
    # Complete ^ 
    
    def display_books(self): # display all books and status 
        library = self.get_library()  # get library data 
        print("Current Library:")
        for titles, authors in library.items():  # for loop to loop through book data 
            for names, lists in authors.items():
                print(f"   '{titles}', by {names}: Genre - {lists[0]}, Published - {lists[1]}, Status - {lists[2]}")  
    # complete ^      


