from flask import Flask, render_template, request
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    con = psycopg2.connect(
    host = "localhost",
    database = "pledges",
    user = os.environ["DB_USERNAME"],
    password = os.environ["DB_PASSWORD"]
    )
    return con

@app.route("/")
def index():
    return render_template('index.html')

@app.get("/api/pledges")
def pledge_read():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT COUNT(name) FROM people;")
    people = cur.fetchone()[0]
    if not people:
        people = 0
    cur.close()
    con.close()
    print(f"people: {people}")
    return {"people": people}

@app.post("/api/pledges")
def pledge_update():
    name = request.get_json()["name"]
    if name:
        con = get_db_connection()
        cur = con.cursor()
        cur.execute(f"INSERT INTO people (name) VALUES ('{name}')")
        con.commit()
        cur.execute("SELECT COUNT(name) FROM people")
        people = cur.fetchone()[0]
        cur.close()
        con.close()
        return {"people": people}
    return {"message": "Name must not be blank."}

if __name__ == "__main__":
    app.run(debug=False)