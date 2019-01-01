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

    #This method will get the suicides for country, sex and year
    def suicides_by_country_sex_year(self, country, sex, year):
        self.data = self.data[(self.data.country == country) & (self.data.sex == sex) & (self.data.year == year)]
        Total = self.data['suicides_no'].sum()
        return Total

    #This method will get number of suicides by age groups.
    def suicides_by_age_group(self):
        age_groups = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
        Total_suicides = []
        for age in age_groups:
            #I have to set the data frame equal to another data frame or else it will hold only the first
            #age group in the data set.
            df = self.data
            df = df[(df.age == age) & (df.country == 'United States of America')]
            Total = df['suicides_no'].sum()
            Total_suicides.append(Total)
        return Total_suicides

    #This method will get number of suicides by age groups and male sex.
    def suicides_by_age_group_male(self):
        age_groups = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
        Total_suicides = []
        for age in age_groups:
            #I have to set the data frame equal to another data frame or else it will hold only the first
            #age group in the data set.
            df = self.data
            df = df[(df.age == age) & (df.country == 'United States of America') & (df.sex == 'male')]
            Total = df['suicides_no'].sum()
            Total_suicides.append(Total)
        return Total_suicides

    #This method will get number of suicides by age groups and female sex.
    def suicides_by_age_group_female(self):
        age_groups = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
        Total_suicides = []
        for age in age_groups:
            #I have to set the data frame equal to another data frame or else it will hold only the first
            #age group in the data set.
            df = self.data
            df = df[(df.age == age) & (df.country == 'United States of America') & (df.sex == 'female')]
            Total = df['suicides_no'].sum()
            Total_suicides.append(Total)
        return Total_suicides

# play = Data()
# play.suicides_by_age_group_male()
