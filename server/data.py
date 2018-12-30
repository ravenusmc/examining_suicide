#This file will handle a lot of the data process for the fact page.
#Bringing in the outside libraries for use in this pageimport csv
from csv import writer
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/who_suicide_statistics.csv')

    #This method will get the suicides by year for each country
    def suicides_by_country(self):
        #Getting the data set to match a specific country.
        self.data = self.data[self.data.country == 'United States of America']
        #Getting the total number of suicides
        Total = self.data['suicides_no'].sum()
        #returning the total
        return Total

test = Data()
test.suicides_by_country()
