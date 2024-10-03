# Module for User class and methods  
import re 
import books 

class User: # A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
    def __init__(self):
        # nested dictionary for users and data
        self.users = {
            'user_1' : '123456',
            'user_2' : '654321'
        }
    
    def get_users(self): # get method for dict of users and data 
        return self.users 
    
    def check_user(self, username): # method to validate username input
        regex = r"^[A-Za-z]\w{4,14}$"
        if re.match(regex, username): # checks if username: starts alphabetically, has only alphanumeric and underscores, and is between 5 and 15 characters long
            return True
        else:
            return False 
        
    def check_library_id(self, library_id): # method to validate library id input
        regex = r"^\d{6}$"  
        if re.match(regex, library_id): # checks if library id input is a 6 digit number
            return True
        else:
            return False
    
    def add_user(self):
        users = self.get_users() 
        while True:
            new_user = input("Enter new username: ")
            self.check_user(new_user) 
            if self.check_user(new_user): # if new username is valid
                print("Valid Username.")
                id_num = input("Enter new Library ID (any 6 digit number): ")
                if not self.check_library_id(id_num):  # if input returns false on validation
                    print("Invalid Library ID")
                else:
                    print("Valid Library ID.")
                    users[new_user] = id_num  # creates new user, with entered username and id number, empty list for borrowing books 
                    print(f"{new_user} added.") 
                    break 
            else:
                print("Invalid Username")
                  
    def view_user(self):  # method to view particular user 
        users = self.get_users()
        while True:
            find_user = input("Enter username you wish to find: ")
            if find_user in users:
                print(f"User found as: {find_user} - ID Number: {users[find_user]}")
                break
            else: 
                print("User not found.")  
                    
    def display_users(self):
        users = self.get_users() # gets dict 'users'
        print("Current Users: ")
        for username, id_num in users.items(): # for loop to iterate through users and information 
            print(f"   {username} - ID: {id_num}")   
