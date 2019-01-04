from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing my files for this project
from data import *
from graph import *

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

#This route will get the number of suicides based on country and year
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

#This route will get the number of suicides based on country and sex
@app.route('/suicides_by_country_sex', methods=['GET', 'POST'])
def route_three():
    data = Data()
    if request.method == 'POST':
        post_data = request.get_json()
        country = post_data.get('country')
        sex = post_data.get('sex')
        Total = data.suicides_by_country_sex(country, sex)
        return jsonify(Total)
    Total = 'TEST'
    return jsonify(Total)

#This route will get the number of suicides based on country and sex
@app.route('/suicides_by_country_sex_year', methods=['GET', 'POST'])
def route_four():
    data = Data()
    if request.method == 'POST':
        print("POST")
        post_data = request.get_json()
        country = post_data.get('country')
        sex = post_data.get('sex')
        year = int(post_data.get('year'))
        Total = data.suicides_by_country_sex_year(country, sex, year)
        return jsonify(Total)
    Total = 'TEST'
    return jsonify(Total)

#This route will get the number of suicides for the U.S. and by age group Combined
@app.route('/suicides_by_age_combined', methods=['GET'])
def route_five():
    data = Data()
    combined = data.suicides_by_age_group()
    return jsonify(combined)

#This route will get the number of suicides for the U.S. and by age group Combined
@app.route('/suicides_by_age_group_male', methods=['GET'])
def route_six():
    data = Data()
    combined = data.suicides_by_age_group_male()
    return jsonify(combined)

#This route will get the number of suicides for the U.S. and by age group Combined
@app.route('/suicides_by_age_group_female', methods=['GET'])
def route_seven():
    data = Data()
    combined = data.suicides_by_age_group_female()
    return jsonify(combined)

if __name__ == '__main__':
    app.run()
