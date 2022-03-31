import sqlalchemy

#print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:@localhost/Exercise18", echo=True, future=True)

with engine.connect() as conn:
    #print("Hello")
    conn.execute(text("CREATE TABLE some_table3 (x int, y int)"))
    conn.execute(text("INSERT INTO some_table3 (x, y) VALUES (:x, :y)")
        [{"x": 1, "y": 1}, {"x": 2, "y":4}]
    )
    conn.commit()

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table3"))
    for row in result:
        print(f"x: {row.x} y: {row.y}")
