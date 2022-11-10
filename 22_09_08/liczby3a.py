with open("zadania maturalne/08.09.22/liczby.txt") as numbers :
    file = []
    for e in numbers:
        file.append(int(e))
    file.sort(reverse=True)
    counter = 0
    listOf3 = []
    for a in file:
        for b in file:
            if a > b and a%b == 0:
                for c in file:
                    if b > c and b%c == 0:
                        counter += 1
                        listOf3.append([a,b,c])
    print(counter)
    print()
    for e in listOf3:
        print(e[0],e[1],e[2])