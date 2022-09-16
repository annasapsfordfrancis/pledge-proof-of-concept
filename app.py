from flask import Flask, render_template, request
import sqlite3
import os

# class Config(object):
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    secret_key = app.config.get("SECRET_KEY")
    print(f"The key is {secret_key}")
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

if __name__ == "__main__":
    app.run(debug=False)