from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from datetime import datetime
import os

app = Flask(__name__, static_folder="static")
# csrf = CSRFProtect(app)

# WEBSITE_HOSTNAME exists only in production environment
if not 'WEBSITE_HOSTNAME' in os.environ:
   # local development, where we'll use environment variables
   print("Loading config.development and environment variables from .env file.")
   app.config.from_object('azureproject.development')
else:
   # production
   print("Loading config.production.")
   app.config.from_object('azureproject.production')

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

# Create databases, if databases exists doesn't issue create
# For schema changes, run "flask db migrate"
from models import User
db.create_all()
db.session.commit()

@app.route("/")
def index():
    return render_template('index.html')

@app.get("/api/pledges")
def pledge_read():
    from models import User
    people = User.query.count()
    print(f"people: {people}")
    return {"people": people}

@app.post("/api/pledges")
def pledge_update():
    from models import User
    try:
        name = request.get_json()["name"]
    except(KeyError):
        return {"error_message": "Name must not be blank."}
    else:
        user = User()
        user.name = name
        db.session.add(user)
        db.session.commit()

        people = User.query.count()
        return {"people": people}
    return {"message": "Name must not be blank."}

if __name__ == "__main__":
    app.run(debug=False)