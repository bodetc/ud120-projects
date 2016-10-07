#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

for key in data_dict:
    if not data_dict[key]['salary'] == 'NaN' and data_dict[key]['salary'] > 10000000:
        print key, data_dict[key]

data_dict.pop('TOTAL')


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

for key in data_dict:
    if (not data_dict[key]['salary'] == 'NaN' and data_dict[key]['salary'] > 1000000) and (not data_dict[key]['bonus'] == 'NaN' and data_dict[key]['bonus'] > 5000000):
        print key, data_dict[key]