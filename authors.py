# module for Authors class and methods
import re 

class Author: # A class representing book authors with attributes like name and biography.
    def __init__(self): 
        self.authors = {
            'F. Scott Fitzgerald' : 'F. Scott Fitzgerald (1896-1940) was an American novelist, essayist, and short story writer.', 
            'Alice Walker' : 'Alice Walker (born February 9, 1944, Eatonton, Georgia, U.S.) is an American writer whose novels, short stories, and poems are noted for their insightful treatment of African American culture.',
            'J. K. Rowling' : 'J.K. Rowling (born July 31, 1965, Yate, near Bristol, England) is a British author, creator of the popular and critically acclaimed Harry Potter series, about a young sorcerer in training.'
        } 
        
    def get_authors(self): # get method to access authors dict
        return self.authors
    
    def check_name(self, name): # validate if user enters a name 
        regex = r'^[A-Z][a-z]*\.?\s[A-Z][a-z]*\.?$'    # checks for '.' in name as well 
        if re.match(regex, name):
            return True
        else:
            return False 
    
    def new_author(self):   # method to add author 
        authors = self.get_authors()
        while True:
            new_author = input("Enter Name of author: ") 
            if self.check_name(new_author):  # if user input is validated
                new_bio = input("Enter a short biography about the author: ")  # ask user to enter short bio about author 
                authors[new_author] = new_bio   # adds author and bio to  dict 
                print(f"{new_author} added to list of authors.") 
                break 
            else:
                print("Invalid name.") 
    
    def view_author(self):  # method to search and view details of particular author 
        authors = self.get_authors()
        while True:
            find_author = input("Enter the name of the author you wish to find: ") 
            if find_author in authors:
                print(f"{find_author} - Biography: {authors[find_author]}") 
                break
            else: 
                print("Author not found.") 
     
    def display_authors(self):  # method to display all authors and bios 
        authors = self.get_authors()
        print("Current authors: ")
        for name, bio in authors.items():
            print(f"{name} - {bio}")   