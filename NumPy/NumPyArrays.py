import numpy
class NumPyArrays:
    numpyArr = numpy.array([1, 2, 3])

    print(numpyArr)

    numpyRange = numpy.arange(0, 10, 2)

    print(numpyRange)

    numpyZeros = numpy.zeros((2,3))

    print(numpyZeros)

    """Evenly spaced points"""

    numpySpace = numpy.linspace(0, 5, 10)

    print(numpySpace)

    """identity matrix"""

    idMatrix = numpy.eye(4)

    print(idMatrix)

    """random"""

    numpyRandom = numpy.random.randn(4,4)

    print(numpyRandom)

    numpyRandomInt = numpy.random.randint(1,50,10)

    print(numpyRandomInt)

    print(numpyRandomInt.max())
    print(numpyRandomInt.min())
    print(numpyRandomInt.argmax())
    print(numpyRandomInt.argmin())
    print(numpyRandomInt.dtype)