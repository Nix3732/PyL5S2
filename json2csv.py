import csv
import pandas as pd
from pandas import json_normalize
import json

with open('1.json') as json_file:
    data = json.load(json_file)
flat_data = json_normalize(data, 'Employees')

flat_data.to_csv('1.csv', index=False)

