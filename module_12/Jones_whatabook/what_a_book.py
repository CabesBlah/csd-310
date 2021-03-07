# Title: what_a_book.py
# Author: Keegan Jones
# Date: 2/22/2021
# Description: WhatABook program, Python/MySQL

# Code to Connect to whatabook Database
# Import Statements
import sys
import mysql.connector
from mysql.connector import errorcode

# Database Config Object
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True 
}

def display_mainMenu():
    print("\n\tWelcome to the WhatABook Application!")
    print("\n\t\t--Main Menu --\n")

    print("\t\t1. View Books\n")
    print("\t\t2. View Store Locations\n")
    print("\t\t3. My Account\n")
    print("\t\t4. Exit Program\n")

    choice = 0

    try: 
        choice = int(input('Please make a selection.'))
        return choice

    except ValueError:
        print("\n This is an invalid selection, please try again.\n")
    

    return choice



def display_books(_cursor):
    #inner join query to get book info from book table
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    #fetch the results of above query cursor object
    books = _cursor.fetchall()

    print("\n\t-- DISPLAYING BOOK LISTINGS --")

    # iterate over the book data set and display the results
    for book in books:
        print("\tBook Name: {}\n\tAuthor: {}\n\tDetails: {}\n".format(book[0], book[1], book[2]))
             

def display_locations(_cursor):
    _cursor.execute("SELECT store_id, locale FROM store")
    
    locations = _cursor.fetchall()

    print("\n\t-- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("\tLocale: {}\n".format(location[1]))


# validate user id to login
def validate_user():
    user_id = 0
    try:
        user_id = int(input("\n\tPlease enter your customer ID\n"))

        if user_id < 0 or user_id > 3: 
            print("The number you entered is not a valid customer number.\n")
            print("Please try again.")
        return user_id        

    except ValueError:
        print("The number you entered is not a valid customer number.\n")
        print("Please try again.")
    finally:
        user_id = 0
   
# display the users account menu
def display_accountMenu():
    try:
        print("\n\t-- Customer Menu --")
        print("\n\t1. Whishlist")
        print("\n\t2. Add Book")
        print("\n\t3. Main Menu\n")
        
        account_option = int(input("Please make a selection: "))
        return account_option
        
    except ValueError:
        print("You have made an invalid selection, please try again.")


def display_customerWishlist(_cursor, _user_id):
    # query the database to get the list of books on the users wishlist

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id = user.user_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id " +
                    "WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()

    print("\n\t-- DISPLAYING WISHLIST ITEMS --")
    
    for book in wishlist:
        print("\tBook Name: {}\n\t\tAuthor: {}\n".format(book[4], book[5]))


def books_to_add(_cursor, _user_id):
# query the database for books not on the users wishlist, that they can add to the wishlist

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n\t\t--DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("\n\tBook Id: {}\n\tBook Name: {}\n".format(book[0], book[1]))
        

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # try/catch for handling potential MySQL database errors   

    # connect to the WhatABook database
    db = mysql.connector.connect(**config) 
    cursor = db.cursor() # cursor for MySQL queries

    # show the main menu
    user_selection = display_mainMenu()  

    while user_selection != 4:

        # if select 1, call the display_books method and display 
        if user_selection == 1:
            display_books(cursor)

        # if select 2, call the show_locations method and display
        elif user_selection == 2:
            display_locations(cursor)

        # if select 3, call the validate_user method to validate the user_id 
        elif user_selection == 3:
            my_user_id = validate_user()
            # call the display_accountMenu() 
            account_option = display_accountMenu()

            while account_option != 3:

                # if select 1, call the display_customerWishlist() method to display wishlist
                if account_option == 1:
                    display_customerWishlist(cursor, my_user_id)

                # if select 2, call the show_books_to_add function to show books that can be added to wishlist
                elif account_option == 2:

                    # show the books not currently on the users wishlist
                    books_to_add(cursor, my_user_id)

                    # get the input book_id 
                    book_id = int(input("\n\tPlease enter the id of the book you want to add to your wishlist: "))
                    
                    # add the selected book to the wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # commit the changes to the database 
                    db.commit() 


                # show the account menu 
                account_option = display_accountMenu()

        # if the input is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n\tInvalid option, please try again.")
            
        # show the main menu
        user_selection = display_mainMenu()

    print("\n\n\tProgram terminated...")

except mysql.connector.Error as err:
    # error handling 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n\tThe supplied username or password is invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n\tThe specified database does not exist.")

    else:
        print(err)

finally:
    #close connection to database

    db.close()
