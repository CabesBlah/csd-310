
-- Title: Module 10.3 whatabook.init.sql 
-- Author: Keegan Jones
-- Date: 2/16/2021
-- Description: WhatABook database and table creation

-- ALTERATION by Caleb Lewandowski
USE whatabook;
-- END OF ALTERATION

-- Drop test user if exists. 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- Create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- Drop constraints on foreign keys if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they are present
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;

--    CREATE TABLES --

CREATE TABLE user(
    user_id     INT         NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75) NOT NULL,
    last_name   VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE book(
    book_id     INT         NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)NOT NULL,
    PRIMARY KEY (book_id)
);

CREATE TABLE store(
    store_id    INT         NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE wishlist(
    wishlist_id INT         NOT NULL    AUTO_INCREMENT,
    user_id     INT         NOT NULL,
    book_id     INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

--   INSERT RECORDS --

-- Insert store record
INSERT INTO store(locale)
    Values('22443 Novel Rd., Bookworm City, MO. 65846');

-- Insert book records
INSERT INTO book(book_name, author, details)
    VALUES('The Borrowers', 'Mary Norton', 'The first book in The Borrowers series');

INSERT INTO book(book_name, author, details)
    VALUES('The Borrowers Afloat', 'Mary Norton', 'The third book in The Borrowers series.');

INSERT INTO book(book_name, author, details)
    VALUES('The Borrowers Aloft', 'Mary Norton', 'The forth book in The Borrowers series.');

INSERT INTO book(book_name, author, details)
    VALUES('The Borrowers Avenged', 'Mary Norton', 'The fifth book in The Borrowers series.');

INSERT INTO book(book_name, author, details)
    VALUES('Dream Animals: A Bedtime Journey', 'Emily Winfield Martin', 'A childrens bedtime story.');

INSERT INTO book(book_name, author, details)
    VALUES('Its Time to Sleep My Love', 'Eric Metaxas', 'A New York Times bestselling childrens book');

INSERT INTO book(book_name, author, details)
    VALUES('Black Beauty', 'Anna Sewell', 'A classic novel about a horse.');

INSERT INTO book(book_name, author, details)
    VALUES('The Adventures of Huckleberry Finn', 'Mark Twain', 'A Great Illustrated Classics edition.');
    
INSERT INTO book(book_name, author, details)
    VALUES('The Call of the Wild', 'Jack London', 'A Great Illustrated Classics edition.');

-- Insert users
INSERT INTO user(first_name, last_name)
    VALUES('Nellie', 'Jones');

INSERT INTO user(first_name, last_name)
    VALUES('Olivia', 'Jones');

INSERT INTO user(first_name, last_name)
    VALUES('Afton', 'Jones');

-- Insert wishlist records

Insert Into wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Nellie'),
        (SELECT book_id FROM book WHERE book_name = 'Dream Animals: A Bedtime Journey')
    );

Insert Into wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Olivia'),
        (SELECT book_id FROM book WHERE book_name = 'Its Time to Sleep My Love')
    );

Insert Into wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Afton'),
        (SELECT book_id FROM book WHERE book_name = 'The Call of the Wild')
    );    

