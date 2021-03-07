""" 
    Title: what_a_book.py
    Author: Charles Clark
    Date: March 3, 2021
    Description: WhatABook program
"""

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
"""The following has been replaced by Lewandowski to interact with Lewandowski's WhatABook database.
config = {
    "user": "root",
    "password": "student",
    "host": "127.0.0.1",
    "database": "whatabook",
}"""
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n ..:: Main Menu ::.. \n")

    print("  1. View Books\n  2. View Store Locations\n  3. My Account\n  4. Exit Program")

    try:
        choice = int(input('  Please choose a menu number: '))

        return choice
    except ValueError:
        print_error()
        sys.exit(0)

def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # get results from cursor object 
    books = _cursor.fetchall()

    print("\n  .. BOOK LISTING ..")
    
    # iterate over the player data set and display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  .. STORE LOCATIONS ..")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_user():
    """ validate users """

    try:
        user_id = int(input('\n  Please enter a customer ID: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer ID\n")
            print_exit()
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid menu number\n")
        print_exit()
        sys.exit(0)

def show_account_menu():
    """ display the users account menu """

    try:
        print("\n  .. Customer Menu ..")
        print("  1. Wishlist\n  2. Add Book\n  3. Main Menu")
        account_option = int(input('  Please choose a menu number: '))

        return account_option
    except ValueError:
        print("\n  Invalid menu number\n")
        print_exit()

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n  .. DISPLAYING WISHLIST ITEMS ..")

    for book in wishlist:
        print("  Book Name: {}\n  Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlist """

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n  .. DISPLAYING AVAILABLE BOOKS ..")

    for book in books_to_add:
        print("  Book Id: {}\n  Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

def print_exit():
  print("\n ....Exiting program....\n")

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor() # cursor for MySQL queries

    print("\n  WhatABook Database Application")

    user_selection = show_menu() # show the main menu 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n  Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n  Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n  No good, try again")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n  No good, try again")
            
        # show the main menu
        user_selection = show_menu()

    print_exit()

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Access denied, sorry")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  We can't seem to find that database, sorry")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()