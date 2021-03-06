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

#This route will build the world map
@app.route('/build_world_map', methods=['GET', 'POST'])
def route_eight():
    graph = Graph()
    post_data = request.get_json()
    year = 1979
    suicide_data = graph.build_world_map(year)
    if request.method == 'POST':
        year = int(post_data.get('year'))
        suicide_data = graph.build_world_map(year)
        return jsonify(suicide_data)
    return jsonify(suicide_data)

#This route will build total graph data
@app.route('/build_total_suicides_graph', methods=['GET'])
def route_nine():
    graph = Graph()
    suicide_data = graph.build_total_suicides()
    return jsonify(suicide_data)

#This route will build the graph for the U.S.
@app.route('/build_total_suicides_graph_us', methods=['GET'])
def route_ten():
    graph = Graph()
    suicide_data = graph.build_total_suicides_us()
    return jsonify(suicide_data)

#This route will build the graph for the U.S showing male suicides.
@app.route('/build_total_suicides_graph_us_males', methods=['GET'])
def route_eleven():
    graph = Graph()
    suicide_data = graph.build_total_suicides_graph_us_males()
    return jsonify(suicide_data)

#This route will build the graph for the U.S showing female suicides.
@app.route('/build_total_suicides_graph_us_females', methods=['GET'])
def route_twelve():
    graph = Graph()
    suicide_data = graph.build_total_suicides_graph_us_females()
    return jsonify(suicide_data)

### The below routes will get all the data to build the age graphs
@app.route('/build_first_age_graph', methods=['GET'])
def route_thirteen():
    graph = Graph()
    suicide_data = graph.build_first_age_graph()
    return jsonify(suicide_data)

@app.route('/build_second_age_graph', methods=['GET'])
def route_fourteen():
    graph = Graph()
    suicide_data = graph.build_second_age_graph()
    return jsonify(suicide_data)

@app.route('/build_third_age_graph', methods=['GET'])
def route_fifteen():
    graph = Graph()
    suicide_data = graph.build_third_age_graph()
    return jsonify(suicide_data)

@app.route('/build_fourth_age_graph', methods=['GET'])
def route_sixteen():
    graph = Graph()
    suicide_data = graph.build_fourth_age_graph()
    return jsonify(suicide_data)

@app.route('/build_fifth_age_graph', methods=['GET'])
def route_seventeen():
    graph = Graph()
    suicide_data = graph.build_fifth_age_graph()
    return jsonify(suicide_data)

@app.route('/build_sixth_age_graph', methods=['GET'])
def route_eightteen():
    graph = Graph()
    suicide_data = graph.build_sixth_age_graph()
    return jsonify(suicide_data)


if __name__ == '__main__':
    app.run()
