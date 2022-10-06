def roz(number):
    n = int(number)
    div = 2
    divs = []
    while n != 1:
        if n%div == 0:
            divs.append(div)
            n = n/div
        else:
            div += 1
    return divs

with open("liczby.txt") as file:
    maxN = 0 # 1
    maxD = 0 # 1
    for e in file:
        tester = roz(e)
        if len(tester) > maxD :
            maxD = len(tester)
            maxN = e
    print(maxN, maxD)

with open("liczby.txt") as file2: 
    maxN = 0 # 2
    maxD = 0 # 2
    for x in file2:
        tester = roz(x)
        testList = []
        for el in tester:
            if el not in testList:
                testList.append(el)
        if len(testList) > maxD :
                maxD = len(tester)
                maxN = x
    print(maxN, maxD)