# Source: https://machinelearningmastery.com/load-machine-learning-data-python/
import csv
import numpy

filename = '../../data/raw/greenhouse_gas_inventory_data_data.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x)

"""
Should I convert:
    Convert first column (countries) to one-hot? 
    Convert second (year) and third (value in kilotons equivalent CO2) column to float 
    Convert fourth column (category) to one-hot or maybe remove it ?
If I want to predict: 
    Global Average temperature I need:
        (1)Predict the output of each country by year X
        Encorporate growth somehow? - India is going to industrialize and will produce more
        wheras the US and other developed countries should be decreasing their emissions
        Find relationship between GHG emissions and temperature and use predicted amount of emissions to estimate
In order to decide what type of model I should try to build, I need to visualize this data
    Perhaps [country, year (x axis), GHG (y axis)] 
"""



# Skip header?
# Is this the right orientation?
# print(data[1:][1]) Why isn't this the first to last row and first column ?