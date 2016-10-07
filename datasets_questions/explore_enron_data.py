#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("./final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

len(enron_data['METTS MARK'])

i = 0
for val in enron_data.itervalues():
    if val['poi'] == 1:
        i += 1

print i

print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

for key in enron_data:
    if key.startswith('SKILLING') | key.startswith('LAY') | key.startswith('FASTOW'):
        print key, ": ", enron_data[key]

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print enron_data['SKILLING JEFFREY K']

salary = 0
email = 0
total_payments = 0
for key in enron_data:
    if not enron_data[key]['salary'] == 'NaN':
        salary += 1
    if not enron_data[key]['email_address'] == 'NaN':
        email += 1
    if not enron_data[key]['total_payments'] == 'NaN':
        total_payments += 1

print "Salary: ", salary
print "Email: ", email
print "Total Payments: ", total_payments
print "Total Payments (percent): ", 1-total_payments/float(len(enron_data))

len(dict((k, v) for k, v in enron_data.items() if v['total_payments'] == 'NaN'))
len(filter(lambda x: x['total_payments']=='NaN' and x['poi'] == 1, enron_data.itervalues()))
len(filter(lambda x: x['poi'] == 1, enron_data.itervalues()))
