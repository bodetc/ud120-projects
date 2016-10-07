#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np

    cleaned_data=zip(ages, net_worths,np.square(predictions - net_worths))
    cleaned_data.sort(key=lambda tup: tup[2])
    print "cleaned_data:", cleaned_data
    print "cleaned_data:", cleaned_data[0:80]

    return cleaned_data[0:80]
