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

## Run the server
```
flask run
```

## Access the website
You can view the website on http://127.0.0.1:5000

# Folder structure

- templates
    - index.html -> html template in [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/templates/) format
- venv -> virtualenv virtual environment folder
- .gitignore
- app.py -> the [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) server logic lives here
- data.db -> [Sqlite](https://docs.python.org/3/library/sqlite3.html) database: one table `pledges` with one column `name`
- README.md
- requirements.txt -> pip requirements

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
