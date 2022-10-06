def zad_1():
    with open("zadania maturalne/22.09.22/liczby.txt") as file:
        numbers = []
        for e in file:
            numbers.append(str(int(e)))
        reflections =[]
        for e in numbers:
            lengh = len(e)
            reflection = ""
            for i in range(1,lengh+1):
                reflection += e[-i]
            reflections.append(reflection)
        for e in reflections :
            if int(e)%17 == 0:
                print(int(e))


def Mod(number):
    return number if number>0 else -number

def zad_2():
    with open("zadania maturalne/22.09.22/liczby.txt") as file:
        numbers = []
        for e in file:
            numbers.append(str(int(e)))
        reflections =[]
        for e in numbers:
            lengh = len(e)
            reflection = ""
            for i in range(1,lengh+1):
                reflection += e[-i]
            reflections.append((int(e),int(reflection)))

    modMax = 0
    numberMax = 0
    for tuple in reflections:
        mod = Mod(tuple[0]-tuple[1])
        if mod>modMax:
            modMax = mod
            numberMax = tuple[0]
    print(numberMax,modMax)


def Div(number):
    n = number
    div = 2
    divs = []
    while n != 1:
        if n%div == 0:
            divs.append(div)
            n = n/div
        else:
            div += 1
    return "Prime" if len(divs) == 1 and divs[0] == number else False
def zad_3():
    with open("zadania maturalne/22.09.22/liczby.txt") as file: 
        numbers = []
        for e in file:
            numbers.append(str(int(e)))
        reflections =[]
        for e in numbers:
            lengh = len(e)
            reflection = ""
            for i in range(1,lengh+1):
                reflection += e[-i]
            reflections.append((int(e),int(reflection)))
        for tuple in reflections:
            if Div(tuple[0]) == "Prime" and Div(tuple[1]) == "Prime":
                print(tuple[0])

def zad_4():
    with open("zadania maturalne/22.09.22/liczby.txt") as file: 
        numbers = []
        for e in file:
            numbers.append(int(e))
        dic = {}
        soloCounter = 0
        doubleCounter = 0
        tripleCounter = 0
        for e in numbers:
            if e in dic:
                if dic[e] == 1:
                    dic[e] = 2
                elif dic[e] == 2:
                    dic[e] = 3
            else:
                dic[e] = 1
        done =[]
        for e in numbers:
            if e not in done:
                if dic[e] == 1:
                    soloCounter += 1
                    done.append(e)
                elif dic[e] == 2:
                    doubleCounter += 1
                    done.append(e)
                elif dic[e] == 3:
                    tripleCounter += 1
                    done.append(e)

        print(soloCounter,doubleCounter,tripleCounter)
zad_1()
print()
zad_2()
print()
zad_3()
print()
zad_4()