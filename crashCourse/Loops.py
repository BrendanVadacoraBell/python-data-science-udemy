class Loops:

    lst = [1,3,4,5,6]

    for elem in lst:
        print('Hello #{num}'.format(num=elem))

    for num in range(0,5):
        print(num)

    rangeList = list(range(10))

    print(rangeList)

    listComprehension = [num**2 for num in rangeList]

    print(listComprehension)