import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

con = psycopg2.connect(
    host = "localhost",
    database = "pledges",
    user = os.environ["DBUSER"],
    password = os.environ["DBPASS"]
)

cur = con.cursor()

cur.execute("CREATE TABLE people (id serial PRIMARY KEY, name varchar(100) NOT NULL);")
con.commit()
cur.close()
con.close()