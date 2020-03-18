import pandas as pd
import numpy as np



def read_data(filename):
    """ Read data from CSV.
  
    Keyword arguments:
    filename -- path to the csv
    
    Return a numpy array of size (number_of_countries, number of entries per country, 3)
    """
    names = ['country_or_area', 'year', 'value', 'category']
    data = pd.read_csv(filename, names=names, skiprows=1)# , index_col='country_or_area')

    # source: https://stackoverflow.com/questions/52621497/pandas-group-by-column-and-transform-the-data-to-numpy-array
    group_by_country = data.groupby('country_or_area').cumcount()  
    multi_indexed = pd.MultiIndex.from_product([data['country_or_area'].unique(), group_by_country.unique()])
    to_list = (data.set_index(['country_or_area',group_by_country])
       .reindex(mux, fill_value=0)
       .groupby(level=0)['year','value', 'category']
       .apply(lambda x: x.values.tolist())
       .tolist()
    )

    return np.array(to_list)
