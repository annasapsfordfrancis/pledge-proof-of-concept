# Pledge Proof of Concept

## Python version
I've only tested with Python 3.10.6, but everything from 3.7 and up should be fine.

## Activate virtual environment
Make sure virtualenv is installed:
```
pip install virtualenv
```

Create a virtual environment (if you don't have a `venv` folder):
```
python -m venv ./venv
```

Run virtual environment:

Mac/Linux
```
source venv/bin/activate
```

Windows
```
.\venv\Scripts\activate
```

Note: (venv) should be at the start of each line in the terminal.

## Install dependencies

In terminal with virtual environment (venv) running:
```
pip install -r requirements.txt
```

## Set up Postgresql
I've tested this with Postgresql 14, but other versions might work too.

I followed this guide to get things set up on Mac: https://daily-dev-tips.com/posts/installing-postgresql-on-a-mac-with-homebrew/

### Create the database
```
psql postgres
create database pledges;
```

You can quit the shell with `\q`

### Set up environment variables
Create a `.env` file in the project root directory with the contents:
```
FLASK_DEBUG=True
DBNAME="pledges"
DBHOST="localhost"
DBUSER = "your_username"
DBPASS = "your_password"
```

### Create database migrations
```
flask db init
flask db migrate -m "initial migration"
```

If you want to check if the tables have been set up correctly:
```
psql postgres
\c pledges
\dt
\d user
```

## Run the server
```
flask run
```

## Access the website
You can view the website on http://127.0.0.1:5000

# Folder structure

- [templates](https://github.com/annasapsfordfrancis/pledge-proof-of-concept/tree/main/templates)
    - [index.html](https://github.com/annasapsfordfrancis/pledge-proof-of-concept/blob/main/templates/index.html) -> html template in [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/templates/) format
- venv -> virtualenv virtual environment folder
- [.gitignore](https://github.com/annasapsfordfrancis/pledge-proof-of-concept/blob/main/.gitignore)
- [app.py](https://github.com/annasapsfordfrancis/pledge-proof-of-concept/blob/main/app.py) -> the [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) server logic lives here
- data.db -> [Sqlite](https://docs.python.org/3/library/sqlite3.html) database: one table `pledges` with one column `name`
- README.md
- [requirements.txt](https://github.com/annasapsfordfrancis/pledge-proof-of-concept/blob/main/requirements.txt) -> pip requirements

## API
The internal API. This connects to the database and allows GET and POST requests at http://127.0.0.1:5000/api/pledges

### GET
Returns JSON
```json
{ "people": 5 }
```

### POST
Accepts JSON
```json
{ "name": "Jane Smith" }
```

Then returns JSON
```json
{ "people": 6 }
```

## Frontend
The frontend is hosted at http://127.0.0.1:5000
This is currently a [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/templates/) html template with embedded JavaScript and no CSS.
