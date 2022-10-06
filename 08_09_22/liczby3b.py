with open("zadania maturalne/08.09.22/liczby.txt") as numbers :
    file = []
    for e in numbers:
        file.append(int(e))
    file.sort(reverse=True)
    counter = 0
    for a in file:
        for b in file:
            if a > b and a%b == 0:
                for c in file:
                    if b > c and b%c == 0:
                        for d in file:
                            if c > d and c%d == 0:
                                for e in file :
                                    if d > e and d%e == 0:
                                        counter +=1                    
    print(counter)
