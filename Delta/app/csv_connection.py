import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pandas as pd 
from app import app
from flask import jsonify, request
import json
import csv


@app.route('/deltaairline')
def firstpage():
	# to get variable value from HTML
	origin = request.args.get('origin')
	destination = request.args.get('dest')

	# to accept lower case and upper case from front end
	origin_lower=origin.lower()
	destination_lower=destination.lower()

	df = pd.read_csv('flights_data.csv', names=['id','created_at','updated_at','flight_identifier','flt_num',
	'scheduled_origin_gate','scheduled_destination_gate','out_gmt','in_gmt','off_gmt','on_gmt','destination','origin',
	'destination_full_name','origin_full_name'])
	# to accept lower case and upper case from front end
	df1=df[((df['origin'].str.lower()==origin_lower) | (df['origin_full_name'].str.lower()==origin_lower)) & ((df['destination'].str.lower()==destination_lower) | (df['destination_full_name'].str.lower()==destination_lower))]
	
	jsonData = df1.to_json(orient="records")
	return jsonData 
	# return {'error':False}