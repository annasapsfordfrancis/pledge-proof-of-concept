# Pledge Proof of Concept

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

In terminal with virttual environment (venv) running:
```
pip install -r requirements.txt
```

## Run the server
```
flask run
```

## Access the website
You can view the website on http://127.0.0.1:5000