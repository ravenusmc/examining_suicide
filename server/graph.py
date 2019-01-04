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
        print('hhh')
        #I have to create a master array
        #I have to loop through the data by country.
        #I have to get the total number of suicides by year for each country.
        #I have to put both the country name and suicides for year into smaller array
        #I don't have to loop through year-since the user will be controlling that on
        #the UI side.
        #I need to do a search for each country and year WHERE YEAR will STAY
        #CONSTANT
