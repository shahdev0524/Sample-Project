from flask import Flask, render_template

app = Flask(__name__)

from app import csv_connection

@app.route("/")
def hello():
    return render_template('delta.html')