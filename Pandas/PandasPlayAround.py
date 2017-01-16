import numpy
import pandas

class PandasPlayAround:
    labels = ['a','b','c']
    my_data = [10,20,30]
    arr = numpy.array(my_data)
    d =  {'a':10, 'b':20, 'c':30}

    pSeries = pandas.Series(data = my_data, index = labels)
    print(pSeries)

    pSeries2 = pandas.Series(arr, labels)

    print(pSeries2)

    pSeries3 = pandas.Series(d)

    print(pSeries3)