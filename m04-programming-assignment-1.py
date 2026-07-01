# 11.1 Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 daily'. 
# Then, use the interactive interpreter to import the zoo module and call its hours() function.
import zoo
zoo.hours()

# 11.2 In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
import zoo as menagerie
menagerie.hours()

# 16.4 Use the sqlite3 module to create a SQLite database called books.db and a table called books with these fields: 
# title (text), author (text), and year (integer).
import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
    (
    title VARCHAR(500) PRIMARY KEY,
    author VARCHAR(500),
    publication_year INT)''')

# 16.5 Read books2.csv and insert its data into the book table.

# import csv module
import csv

# open the csv file and read through the lines
with open("books2.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    # skip header row
    next(reader)

    # execute many to insert all rows in the csv into the table
    curs.executemany("INSERT INTO books VALUES (?, ?, ?)", reader)

# commit the transaction and close the connection
conn.commit()
conn.close()

# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. 
# As in 16.6, select and print the title column from the book table in alphabetical order.

# import sqlalchemy
import sqlalchemy as sa

# connect to the db
engine = sa.create_engine('sqlite:///books.db')
with engine.connect() as connection:

    # query the books table for all rows, sorrted A-Z
    query = sa.text("SELECT title FROM books ORDER BY title ASC;")
    result = connection.execute(query)
    
    # loop through results and print the title
    for row in result:
        print(row)