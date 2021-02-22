-- Caleb Lewandowski
-- February 22, 2021
-- Module 10.3 Assignment
-- Purpose: To initialize the whatabook database.

-- Create a user. If user already exists, drop it.
DROP USER IF EXISTS 'whatabook_user'@'localhost';
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- Drop tables store, wishlist, book, and user if they exist.
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;

-- Create the table user.
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

-- Create the table book.
CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY(book_id)
);

-- Create the table wishlist.
CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id)
        REFERENCES user(user_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);

-- Create the table store.
CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);


-- Insert users into the table user.
INSERT INTO user(first_name, last_name)
    VALUE('Axel', 'Air');
INSERT INTO user(first_name, last_name)
    VALUE('Bob', 'Bank');
INSERT INTO user(first_name, last_name)
    VALUE('Caleb', 'Coal');

-- Insert books into the table book.
INSERT INTO book(book_name, details, author)
    VALUE('The Story of a Swordsman', 'A swordsmans partakes in a dangerous journey.', "Ian I");
INSERT INTO book(book_name, details, author)
    VALUE('Video Games are Fun', "A writer's enjoyment of video games.", "Jack Joe");
INSERT INTO book(book_name, details, author)
    VALUE('How Chocolate is Made', 'An in depth analysis into the creation of chocolate.', "Kristy Keen");
INSERT INTO book(book_name, details, author)
    VALUE('Words are Weird', 'Though and tough are spelled similarly but are pronounced differently.', "Lee Look");
INSERT INTO book(book_name, details, author)
    VALUE('Nothing', '...', "Mike Moon");
INSERT INTO book(book_name, details, author)
    VALUE('Something', 'Something is here.', "Not No");
INSERT INTO book(book_name, details, author)
    VALUE('Everything', 'Everything', "Or Oop");
INSERT INTO book(book_name, details, author)
    VALUE('Light', 'Light can be very bright.', "Pear Put");
INSERT INTO book(book_name, details, author)
    VALUE('Darkness', 'You cannot see when it is too dark.', "Quack Quack");

-- Insert wishlists into the table wishlist.
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Axel'),
        (SELECT book_id FROM book WHERE book_name = 'The Story of a Swordsman')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Bob'),
        (SELECT book_id FROM book WHERE book_name = 'Light')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Caleb'),
        (SELECT book_id FROM book WHERE book_name = 'Video Games are Fun')
    );

-- Insert store into the table store.
INSERT INTO store(locale)
    VALUES("12345 Something Street    Everything, Nothing 99999");