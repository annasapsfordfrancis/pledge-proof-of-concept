import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

con = psycopg2.connect(
    host = "localhost",
    database = "pledges",
    user = os.environ["DB_USERNAME"],
    password = os.environ["DB_PASSWORD"]
)

cur = con.cursor()

cur.execute("CREATE TABLE people (id serial PRIMARY KEY, name varchar(100) NOT NULL);")
con.commit()
cur.close()
con.close()