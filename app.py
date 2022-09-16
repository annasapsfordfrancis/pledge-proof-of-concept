from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.get("/api/pledges")
def pledge_read():
    cur = sqlite3.connect("data.db").cursor()
    people = cur.execute("SELECT COUNT(name) FROM pledges").fetchone()[0]
    cur.close()
    print(f"people: {people}")
    return {"people": people}

@app.post("/api/pledges")
def pledge_update():
    name = request.get_json()["name"]
    if name:
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute(f"INSERT INTO pledges VALUES ('{name}')")
        con.commit()
        people = cur.execute("SELECT COUNT(name) FROM pledges").fetchone()[0]
        cur.close()
        return {"people": people}
    return {"message": "Name must not be blank."}