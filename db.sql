CREATE DATABASE librarymanagement;

CREATE TABLE bookMarc (
    book_id INT PRIMARY KEY,
    title VARCHAR(50),
    author VARCHAR(50),
    publisher VARCHAR(50),
    year INT,
    isbn VARCHAR(13)
);

CREATE TABLE book (
    inventory_number INT PRIMARY KEY,
    book_id INT,
    status VARCHAR(20),
    FOREIGN KEY (book_id) REFERENCES bookMarc(book_id)
);

select * from bookmarc
INSERT INTO bookMarc (book_id, title, author, publisher, year, isbn) VALUES
(2,'Harry Porter','John Max','Harper & Brothers',1990,9790061945467),
(3, 'To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott & Co.', 1960, 9780060935467),
(4, '1984', 'George Orwell', 'Secker & Warburg', 1949, 9780451524935),
(5, 'Pride and Prejudice', 'Jane Austen', 'T. Egerton', 1813, 9780141439518),
(6, 'The Catcher in the Rye', 'J.D. Salinger', 'Little, Brown and Company', 1951, 9780316769488),
(7, 'Moby-Dick', 'Herman Melville', 'Harper & Brothers', 1851, 9781503280786),
(8, 'War and Peace', 'Leo Tolstoy', 'The Russian Messenger', 1869, 9781400079988),
(9, 'The Odyssey', 'Homer', 'Various', -800, 9780140268867),
(10, 'Ulysses', 'James Joyce', 'Sylvia Beach', 1922, 9780199535675),
(11, 'The Divine Comedy', 'Dante Alighieri', 'Various', 1320, 9780142437223);

select * from bookmarc
where book_id = 9
