#This file will handle a lot of the data process for the fact page.
#Bringing in the outside libraries for use in this pageimport csv
from csv import writer
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/who_suicide_statistics.csv')

    #This method will get the suicides by year for each country
    def suicides_by_country(self, country):
        #Getting the data set to match a specific country.
        self.data = self.data[self.data.country == country]
        #Getting the total number of suicides
        Total = self.data['suicides_no'].sum()
        #returning the total
        return Total

    #This method will get the suicides by country and by year
    def suicides_by_country_year(self, country, year):
        self.data = self.data[(self.data.country == country) & (self.data.year == year)]
        Total = self.data['suicides_no'].sum()
        return Total

    #This method will get the suicides for country and by sex
    def suicides_by_country_sex(self, country, sex):
        self.data = self.data[(self.data.country == country) & (self.data.sex == sex)]
        Total = self.data['suicides_no'].sum()
        return Total

# play = Data()
# play.suicides_by_country_year()
