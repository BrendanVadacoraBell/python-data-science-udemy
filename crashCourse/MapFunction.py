class MapFunction:
    numList = [1,2,3,4,5]

    print(list(map(lambda num: num*2, numList)))

    print(list(filter(lambda num: num%2==0, numList)))

    """Methods

    Just built in functions
    """

    s = "Yolo Swaggins"

    print(s.lower())

    print(s.split(" "))

    print(4 in numList)

    tupleList = [(1,2),(3,4),(5,6)]


    """
    Tuple unpacking
    """
    for (a,b) in tupleList:
        print(a,b)