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
        # print(self.data.dtypes)
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
            if year != 2016:
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
            if year != 2016:
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
            if year != 2016:
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
            if year != 2016:
                data = data[(data.year == year) & (data.country == 'United States of America') & (data.sex == 'female')]
                suicides = data['suicides_no'].sum()
                year = str(year)
                single_country.append(year)
                single_country.append(suicides)
                suicide_data.append(single_country)
        return suicide_data

    #This method will get the data to build the tree map. It will not be called
    #by axios in the program.
    def build_tree_graph(self):
        countries = self.data.country.unique()
        #This list will hold all of the data to build a data frame
        d = []
        #building a new dataframe to get the sum of all the countries suicides.
        for country in countries:
            #resetting the data for each loop
            data = self.data
            data = data[(data.country == country)]
            suicides = data['suicides_no'].sum()
            d.append({'Country': country, 'Suicides': suicides})
        #creating the dataframe
        df = pd.DataFrame(d)
        #sorting the dataframe
        df = df.nlargest(5, 'Suicides')
        #print(df)

    #This method will build the first age graph
    def build_first_age_graph(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            if year != 2016:
                data = data[(data.year == year) & (data.country == 'United States of America')
                & (data.age == '5-14 years')]
                suicides = data['suicides_no'].sum()
                year = str(year)
                single_country.append(year)
                single_country.append(suicides)
                suicide_data.append(single_country)
        return suicide_data

    #This method will build the first age graph
    def build_second_age_graph(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            if year != 2016:
                data = data[(data.year == year) & (data.country == 'United States of America')
                & (data.age == '15-24 years')]
                suicides = data['suicides_no'].sum()
                year = str(year)
                single_country.append(year)
                single_country.append(suicides)
                suicide_data.append(single_country)
        return suicide_data

    def build_third_age_graph(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            if year != 2016:
                data = data[(data.year == year) & (data.country == 'United States of America')
                & (data.age == '25-34 years')]
                suicides = data['suicides_no'].sum()
                year = str(year)
                single_country.append(year)
                single_country.append(suicides)
                suicide_data.append(single_country)
        return suicide_data

    def build_fourth_age_graph(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            if year != 2016:
                data = data[(data.year == year) & (data.country == 'United States of America')
                & (data.age == '35-54 years')]
                suicides = data['suicides_no'].sum()
                year = str(year)
                single_country.append(year)
                single_country.append(suicides)
                suicide_data.append(single_country)
        return suicide_data

    def build_fifth_age_graph(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            if year != 2016:
                data = data[(data.year == year) & (data.country == 'United States of America')
                & (data.age == '55-74 years')]
                suicides = data['suicides_no'].sum()
                year = str(year)
                single_country.append(year)
                single_country.append(suicides)
                suicide_data.append(single_country)
        return suicide_data

    def build_sixth_age_graph(self):
        #This list will hold all of the country and suicide deaths for each year
        suicide_data = [['Year', 'Suicides']]
        year_list = []
        #getting a list of unique years
        years = self.data.year.unique()
        #Append each year to a list which I'll then have to sort.
        for year in years:
            year_list.append(year)
        year_list.sort()
        for year in year_list:
            #This list will hold the data for a single country
            single_country = []
            #resetting the data for each loop
            data = self.data
            if year != 2016:
                data = data[(data.year == year) & (data.country == 'United States of America')
                & (data.age == '75+ years')]
                suicides = data['suicides_no'].sum()
                year = str(year)
                single_country.append(year)
                single_country.append(suicides)
                suicide_data.append(single_country)
        return suicide_data



# data = Graph()
# data.build_world_map(1980)































##
