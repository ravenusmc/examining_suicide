#This file will handle a lot of the data process for the fact page.
#Bringing in the outside libraries for use in this pageimport csv
from csv import writer
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/who_suicide_statistics.csv')

    def test(self):
        print(self.data.head())

test = Data()
test.test()
