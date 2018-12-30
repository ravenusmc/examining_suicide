from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing my files for this project
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

#Getting the number of suicides by country
@app.route('/suicides_by_country', methods=['GET', 'POST'])
def route_one():
    data = Data()
    if request.method == 'POST':
        post_data = request.get_json()
        country = post_data.get('country')
        Total = data.suicides_by_country(country)
        return jsonify(Total)
    Total = 'TEST'
    return jsonify(Total)

@app.route('/suicides_by_country_year', methods=['GET', 'POST'])
def route_two():
    data = Data()
    if request.method == 'POST':
        post_data = request.get_json()
        country = post_data.get('country')
        year = int(post_data.get('year'))
        Total = data.suicides_by_country_year(country, year)
        return jsonify(Total)
    Total = 'TEST'
    return jsonify(Total)

if __name__ == '__main__':
    app.run()
