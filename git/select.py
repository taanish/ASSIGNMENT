#this is my  ASSIGNMENT using python.
import sqlite3
import sqlalchemy
from sqlalchemy import inspect
conn = sqlite3.connect(test)
 
c = conn.cursor()
c.execute('''
          CREATE TABLE Books
          (Bookid varchar PRIMARY KEY ASC, bookname varchar(250) NOT NULL, ISBN varchar(250) NOT NULL,)
          ''')
c.execute('''
          CREATE TABLE Authors
          (bookid varchar PRIMARY KEY ASC,Author_name varchar(250) NOT NULL''')
 
c.execute('''
          INSERT INTO Books VALUES('1234', 'Nine tales','400001')
          ''')
c.execute('''
          INSERT INTO Books VALUES('1235', 'Risvat','400002')
          ''')
c.execute('''
          INSERT INTO Books VALUES('1236', 'Ghuskhori','400003')
          ''')
c.execute('''
          INSERT INTO Books VALUES('1237', 'Mehnat','400004')
          ''')
c.execute('''
          INSERT INTO Books VALUES('1238', 'Inam','400005')
          ''')
c.execute('''
          INSERT INTO Authors VALUES('1234','Abhishek,Shivani')
          ''')
c.execute('''
          INSERT INTO Authors VALUES('1235','Shiva,Rajni')
          ''')
c.execute('''
          INSERT INTO Authors VALUES('1236','Ramesh,Shiv,Rakesh')
          ''')
c.execute('''
          INSERT INTO Authors VALUES('1237','Abdul,Mia,Jay')
          ''')
c.execute('''
          INSERT INTO Authors VALUES('1238','Jaya,Shipra,Richa')
          ''')
result=c.execute('''SELECT bookname from Books,Authors
             where Books.bookid=Authors.bookid ''')
 
conn.commit()
conn.close()
