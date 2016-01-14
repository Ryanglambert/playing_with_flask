#all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash

#configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME  = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

# us if we're defining the global "FLASKR_SETTINGS"
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# from sqlite3 module we use the 'connect' function to connect to our Flask instance "app"
# passing the argument app.config['DATABASE'] which is a value from a dictionary in the Flask instance named "app"
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()

