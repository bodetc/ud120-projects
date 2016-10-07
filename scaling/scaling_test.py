""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    minVal=min(arr)
    maxVal=max(arr)
    return [(x-minVal)/float(maxVal-minVal) for x in arr]


def sklearnScaling(arr):
    from sklearn.preprocessing import MinMaxScaler
    import numpy
    scaler = MinMaxScaler()
    rescaled_weigth=scaler.fit_transform(numpy.asarray(arr).astype(float).reshape(-1, 1))
    return rescaled_weigth

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
print sklearnScaling(data)