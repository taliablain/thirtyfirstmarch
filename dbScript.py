import sqlalchemy

#print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:@localhost/Exercise18", echo=False, future=True)

#user_input = input("Which genre of books would you like?")

#with engine.connect() as conn:
    #result = conn.execute(
        #text("select BOOK_ID, AUTHUR, TITLE, GENRE from BOOK_INFO where BOOK_INFO.GENRE like :GENRE"),
        #{"GENRE": user_input }
    #)
    #for row in result:
        #print(f"{row.TITLE} by {row.AUTHUR}")

#displaying which books are available
print("available books: ")
with engine.connect() as conn:
    result = conn.execute(text("SELECT TITLE FROM BOOK_INFO"))
    for row in result:
        print(f"{row.TITLE}")

#displaying which books a user has on loan and their due date
user_name = (input("please enter your user id: "))
with engine.connect() as conn:
    result = conn.execute(text("SELECT TITLE, DUE_DATE FROM BOOK_INFO, LOAN_LOG WHERE LOAN_LOG.CUST_ID LIKE :PARAM"),
    {"PARAM": user_name}
    )
    print("books you have on loan")
    for row in result:
        print(f"{row.TITLE}")
        print("due date: ")
        print(f"{row.DUE_DATE}")


#inserting some non fiction books into the library
with engine.connect() as conn:
    conn.execute(text("INSERT INTO BOOK_INFO(BOOK_ID, TITLE, AUTHOR, GENRE) VALUES (5,"MERPEOPLE: A COMPREHENSIVE GUIDE TO THEIR LANGUAGE AND CUSTOMS", "D.MARWOOD", "NON-FICTION")",
    conn.commit()

