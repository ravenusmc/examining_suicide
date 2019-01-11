#This file will hold the class and methods that will build the data for the data
#visualizations in this project.

#importing libraries that will be used.
import numpy as np
import pandas as pd

class Graph():

    #Getting the graph data.
    def __init__(self):
        self.data = pd.read_csv('./data/who_suicide_statistics.csv')

    def build_world_map(self, year):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = []
        #getting a list of unique countries
        countries = self.data.country.unique()
        for country in countries:
            #resetting the data for each loop
            data = self.data
            #This list will hold the data for a single country
            single_country = []
            data = data[(data.country == country) & (data.year == year)]
            #Getting the total suicides for each country
            suicides = data['suicides_no'].sum()
            #Changing country names to be used on the map.
            if country == 'United States of America':
                country = 'United States'
            elif country == 'Russian Federation':
                country = 'Russia'
            elif country == 'Iran (Islamic Rep of)':
                country = "Iran"
            elif country == 'Venezuela (Bolivarian Republic of)':
                country = 'Venezuela'
            single_country.append(country)
            single_country.append(suicides)
            suicide_data.append(single_country)
        return suicide_data

    def build_total_suicides(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            #year = str(year)
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            data = data[data.year == year]
            suicides = data['suicides_no'].sum()
            year = str(year)
            single_country.append(year)
            single_country.append(suicides)
            suicide_data.append(single_country)
        return suicide_data

    def build_total_suicides_us(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            #year = str(year)
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            data = data[(data.year == year) & (data.country == 'United States of America')]
            suicides = data['suicides_no'].sum()
            year = str(year)
            single_country.append(year)
            single_country.append(suicides)
            suicide_data.append(single_country)
        return suicide_data

    def build_total_suicides_graph_us_males(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            #year = str(year)
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            data = data[(data.year == year) & (data.country == 'United States of America') & (data.sex == 'male')]
            suicides = data['suicides_no'].sum()
            year = str(year)
            single_country.append(year)
            single_country.append(suicides)
            suicide_data.append(single_country)
        return suicide_data

    def build_total_suicides_graph_us_females(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            #year = str(year)
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            data = data[(data.year == year) & (data.country == 'United States of America') & (data.sex == 'female')]
            suicides = data['suicides_no'].sum()
            year = str(year)
            single_country.append(year)
            single_country.append(suicides)
            suicide_data.append(single_country)
        return suicide_data


data = Graph()
data.build_total_suicides()
