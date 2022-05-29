from flask import Flask

#define the flask instance
app = Flask(__name__);

#create flask route
@app.route('/')
#create function
def hellow_world():
    return 'I have a million dollars';

#export app
#export FLASK_APP=app.py;

#flask run;