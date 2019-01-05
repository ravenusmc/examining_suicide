#This file will hold the class and methods that will build the data for the data
#visualizations in this project.

#importing libraries that will be used.
import numpy as np
import pandas as pd

class Graph():

    #Getting the graph data.
    def __init__(self):
        self.data = pd.read_csv('./data/who_suicide_statistics.csv')

    def build_world_map(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = []
        #getting a list of unique countries
        countries = self.data.country.unique()
        for country in countries:
            #resetting the data for each loop
            data = self.data
            #This list will hold the data for a single country
            single_country = []
            data = data[(data.country == country) & (data.year == 1979)]
            #Getting the total suicides for each country
            suicides = data['suicides_no'].sum()
            single_country.append(country)
            single_country.append(suicides)
            suicide_data.append(single_country)
            print(suicide_data)
            input()
        #I need to do a search for each country and year WHERE YEAR will STAY
        #CONSTANT

data = Graph()
data.build_world_map()
