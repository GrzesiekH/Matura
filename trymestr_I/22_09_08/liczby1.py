with open("liczby.txt") as file:
    n = 0
    counter = 0
    for e in file:
        if e[0] == e[-2]:
            if n == 0:
                n = e
            counter += 1
    print(n)
    print(counter)