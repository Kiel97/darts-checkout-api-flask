# Darts Checkout API Flask
A very simple REST API built with Python 3, Flask, SQLite3 and Tkinter modules.

## Installation
There is `requirements.txt` file containing all required Python modules to work. It's best to create virtual environment inside project folder by typing `$ virtualenv venv`. You can activate env by typing `$ . venv/bin/activate`. Once inside type in terminal `pip install -r requirements.txt`.
After that open 2 terminal window, for Flask application, and second for Tkinter GUI (no multithreading, sorry). Inside Flask terminal type `$ python app.py` while in the other `$ python gui.py`. The application should work now.

## Usage
### Tkinter GUI
When running app simply insert score you are looking for (like 2, 10, 41, 122, 132, 140 and so on) and then press Search button. Tkinter makes GET request to Flask application API with score parameter passed. GUI inserts all combos returned from GET request to the Listbox. Select one combo from list to display it bigger in Label widget. In case of no checkouts available from specified score, the "No checkout" appears in list.
### Flask API
API contains few routes: 
1. **'/'** - nothing but greetings in string form
2. **'/checkout'** POST - insert new record to database in JSON format
3. **'/checkout'** GET - gets all records from database in JSON format
4. **'/checkout/id/<id>'** GET - gets record with matching id in JSON format, id is primary key in database
5. **'/checkout/score/<score>'** GET - the most interesting route, gets all records with matching score value in JSON format
6. **'/checkout/id/<id>'** PUT - updates record with matching id in JSON format
7. **'/checkout/id/<id>'** DELETE - deletes record with matching id in JSON format
8. **'/checkout'** DELETE - removes all records from database
  
Since the database contains only one or two combos for each viable score, you can easily add more of them with Postman or any other useful API testing utility.
Like that.
`{
  "score": 170,
  "combo": "T20 T20 BULL"
}`

Score is an integer and combo is string with max 14 characters. Since id is a primary key in database, it is set to AutoIncrement so you don't have to worry about it when adding new records.
