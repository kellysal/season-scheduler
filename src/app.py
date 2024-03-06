#!/usr/bin/env python3

import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask.templating import render_template

#database config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

#define the database model that is used to store datetime, temperature, forecast details
db = SQLAlchemy(app)
class Weather(db.Model):
	datetime = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow())
	temperature = db.Column(db.Integer, nullable=False)
	detail = db.Column(db.String, nullable=False)

#render the index page with weather data
@app.route("/")
def index():
    weather = Weather.query.all()
    return render_template('index.html', weather=weather)

#average temperature
class Calculator:
    def multiply(self, a, b):
        return a * b
    
    #mock object
    def get_temperature(self):
        response = requests.get("https://api.weather.gov/gridpoints/OKX/47,69/forecast")
        return response.json()["properties"]["periods"][0]["temperature"]

#helper function to get temperature using API (api.weather.gov)
def get_temperature():
    response = requests.get("https://api.weather.gov/gridpoints/OKX/47,69/forecast")
    return response.json()["properties"]["periods"][0]["temperature"]

def get_detail():
    response = requests.get("https://api.weather.gov/gridpoints/OKX/47,69/forecast")
    return response.json()["properties"]["periods"][0]["detailedForecast"]

#add to the database
app.app_context().push()
db.create_all()
current_temperature = get_temperature()
current_detail = get_detail()
new_entry = Weather(temperature=current_temperature,detail=current_detail)
db.session.add(new_entry)
db.session.commit()

if __name__ == '__main__':
    app.run()