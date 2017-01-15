import numpy
class Indexing:
    arr = numpy.arange(0,11)

    print(arr)

    slice_of_arr = arr[3:]

    print(slice_of_arr)

    slice_of_arr[:] = 12

    print(slice_of_arr)
    print(arr)

    arr_copy = arr.copy()

    arr_copy[:] = 100

    print(arr_copy)
    print(arr)

    numpyArray = numpy.array([[1,2,3],[4,5,6],[7,8,9]])

    print(numpyArray)

    print(numpyArray[:2,1:])

    greaterThanFive = numpyArray > 5

    print(numpyArray[greaterThanFive])

