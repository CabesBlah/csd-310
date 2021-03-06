#Caleb Lewandowski
#March 5, 2021
#Module 12 Assignment
#Purpose: To handle the user interface that communicates with the WhatABook database.

#Import classes.
import mysql.connector
from mysql.connector import errorcode
import user
import book
import store

#Create dictionary config.
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#Create database object.
db = None

def main():
    #Connect to database.
    global db
    db = connect_to_database()

    #Create cursor.
    cursor = db.cursor()

    #Welcome user.
    print("Welcome to WhatABook.")

    #Start main menu.
    show_main_menu(cursor)

    #Disconnect from database.
    db.close()

    #Depart user.
    print("\nGoodbye.")

#Connects to the database.
def connect_to_database():
    db = None
    try:
        db = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist.")
        else:
            print(err)
        db.close()
        exit()
    return db

#Displays main menu.
def show_main_menu(cursor):
    while True:
        #Get input.
        print("Enter 1 to view books.")
        print("Enter 2 to view store locations.")
        print("Enter 3 to login to your account.")
        print("Enter -1 to exit program.")
        print("> ", end = "")

        response = input()

        #Determine if input is an integer.
        number = None
        if is_integer(response):
            number = int(response)
        else:
            print("That is not an integer.")
            continue
        
        #Make decision based on input.
        if number == 1:
            #Display list of books.
            print("\nAvailable Books:")
            show_books(get_books(cursor))
            print()
        elif number == 2:
            #Display list of stores.
            print("\nStores:")
            show_stores(get_stores(cursor))
            print()
        elif number == 3:
            #Display account login menu.
            show_account_login_menu(cursor)
        elif number == -1:
            #Exit main menu.
            break
        else:
            #Display invalid response.
            print("That is not a valid response.")

#Displays account login menu.
def show_account_login_menu(cursor):
    while True:
        #Get input.
        print("Enter your user id.")
        print("Enter -1 to cancel login.")
        print("> ", end = "")
        response = input()

        #Determine if input is an integer.
        number = None
        if is_integer(response):
            number = int(response)
        else:
            print("That is not an integer.")
            continue
        
        #Determine if user wants to exit login menu.
        if number == -1:
            print("Login canceled.")
            break
        
        #Determine if input points to existing user.
        user = get_user(cursor, number)
        if user == None:
            print("That is not a valid user id.")
            continue
        
        #Display wish list menu.
        show_wish_list_menu(cursor, user)
        break

#Displays wish list menu.
def show_wish_list_menu(cursor, user):
    #Welcome user by name.
    print("Welcome, {} {}.".format(user.first_name, user.last_name))
    
    while True:
        #Get input.
        print("Enter 1 to view the books in your wish list.")
        print("Enter 2 to add a book to your wish list.")
        print("Enter -1 to log out and return to the main menu.")
        print("> ", end = "")
        response = input()

        #Determine if input is an integer.
        number = None
        if is_integer(response):
            number = int(response)
        else:
            print("That is not an integer.")
            continue
        
        #Determine if user wants to exit wish list menu.
        if number == -1:
            print("Returning to the main menu.")
            print("Goodbye, {} {}.".format(user.first_name, user.last_name))
            break
        
        #Make decision based on input.
        if number == 1:
            #Display books that have been placed in the user's wish list.
            print("\nHere are the books in your wish list:")
            show_books(get_books_in_wish_list(cursor, user.user_id))
            print()
        elif number == 2:
            #Display add-to-wish list menu.
            show_add_to_wish_list_menu(cursor, user)
        else:
            #Display invalid response.
            print("That is not a valid response.")

#Displays add-to-wish list menu.
def show_add_to_wish_list_menu(cursor, user):
    #Display books that are not in wish list.
    print("\nHere are the books not in your wish list:")
    books = get_books_not_in_wish_list(cursor, user.user_id)
    show_books_all_information(books)
    print()

    while True:
        #Get input.
        print("Enter the book id of the book that you would like to add to your wish list.")
        print("Enter -1 to cancel and return to the wish list menu.")
        print("> ", end = "")
        response = input()

        #Determine if input is an integer.
        number = None
        if is_integer(response):
            number = int(response)
        else:
            print("That is not an integer.")
            continue
        
        #Determine if user wants to exit add-to-wish list menu.
        if number == -1:
            print("Returning to the wish list menu.")
            break

        #Make decision based on input.
        if does_book_exist(books, number):
            #Add book to user's wish list.
            add_book_to_wish_list(cursor, user.user_id, number)
            print("Book added to the wish list.")
            break
        else:
            #Display if input does not correspond to any book id.
            print("That is not one of the listed books.")

#Gets list of books.
def get_books(cursor):
    cursor.execute("SELECT book_id, book_name, details, author FROM whatabook.book")
    result = cursor.fetchall()

    books = []
    for item in result:
        books.append(book.Book(item[0], item[1], item[2], item[3]))

    return books

#Gets list of books in a user's wish list.
def get_books_in_wish_list(cursor, user_id):
    cursor.execute("SELECT book.book_id, book_name, details, author \
                    FROM whatabook.book \
                    INNER JOIN whatabook.wishlist \
                    ON whatabook.book.book_id = whatabook.wishlist.book_id \
                    WHERE wishlist.user_id = {}".format(user_id))
    result = cursor.fetchall()

    books = []
    for item in result:
        books.append(book.Book(item[0], item[1], item[2], item[3]))

    return books

#Gets list of books not in a user's wish list.
def get_books_not_in_wish_list(cursor, user_id):
    #Query solution based on guidance from WhatABook requirements.
    cursor.execute("SELECT book_id, book_name, details, author \
                    FROM whatabook.book \
                    WHERE book_id NOT IN \
                        (SELECT book_id \
                        FROM whatabook.wishlist \
                        WHERE user_id = {})".format(user_id))
    result = cursor.fetchall()

    books = []
    for item in result:
        books.append(book.Book(item[0], item[1], item[2], item[3]))

    return books

#Displays list of books.
def show_books(books):
    for book in books:
        print("{} by {}".format(book.book_name, book.author))

#Display list of books with all information.
def show_books_all_information(books):
    for book in books:
        print("{} by {}".format(book.book_name, book.author))
        print("\tBook ID: {}".format(book.book_id))
        print("\tDetails: {}".format(book.details))

#Determines if book exists in a list of books based on book id.
def does_book_exist(books, book_id):
    for book in books:
        if book_id == book.book_id:
            return True
    return False

#Adds book to a user's wish list.
def add_book_to_wish_list(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) \
                    VALUES({}, {})".format(user_id, book_id))
    db.commit()

#Gets list of stores.
def get_stores(cursor):
    cursor.execute("SELECT store_id, locale FROM whatabook.store")
    result = cursor.fetchall()

    stores = []
    for item in result:
        stores.append(store.Store(item[0], item[1]))

    return stores

#Displays list of stores.
def show_stores(stores):
    for store in stores:
        print("{}".format(store.locale))

#Gets user based on id.
def get_user(cursor, user_id):
    cursor.execute("SELECT user_id, first_name, last_name \
                    FROM whatabook.user WHERE user_id = {}".format(user_id))
    result = cursor.fetchone()

    u = None

    if result == None:
        pass
    else:
        u = user.User(result[0], result[1], result[2])

    return u

#Determines if string is an integer.
def is_integer(string):
    try:
        int(string)
        return True
    except:
        return False

#Execute the function main().
if __name__ == "__main__":
    main()