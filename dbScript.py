import sqlalchemy

#print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:@localhost/Exercise18", echo=True, future=True)

genre = input("Which book would you like?")

with engine.connect() as conn:
    result = conn.execute(
        text("select BOOK_ID, AUTHUR, TITLE, GENRE from BOOK_INFO"),
        {"ID": genre}
    )
    for row in result:
        print(f"AUTHOR: {row.AUTHUR}")

