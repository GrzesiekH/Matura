def zad1():
    with open("trymestr_II/23_03_01/przyklad.txt") as file:
        T = [int(e.strip()) for e in file]
    c= 0
    for e in T:
        while e >1:
            if e%3 == 0:
                e /= 3
            else:
                break
        c+= 1 if e == 1 else 0
    print(c)

def silnia(n):
    if n == 0:
        return 1
    s = n
    n -= 1
    while n > 0:
        s *= n
        n -= 1
    return s

def zad2():
    with open("trymestr_II/23_03_01/przyklad.txt") as file:
        T = [e.strip() for e in file]
    ansT = []
    for e in T:
        s = 0
        for i in range(len(e)):
            s += silnia(int(e[i]))
        if s == int(e):
            ansT.append(s)
    print(*ansT)

def NWD(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def podciag(T):
    max = [0,0,0] #  i, len, NWD
    act = 0
    actNWD = 0 
    for i in range(len(T)-1):
        iNWD = NWD(T[i],T[i+1])
        if actNWD == 0 and iNWD >1:
            actNWD = iNWD
            continue
        for j in range(act,i+1):
            if NWD(T[i+1],T[j]) != actNWD or iNWD <= 1:
                lenght = i-act+1
                if lenght>max[1]:
                    max[0] = act
                    max[1] = lenght
                    max[2] = actNWD
                act = i+1
                actNWD = 0
    lenght = i-act+2
    if lenght>max[1]:
        max[0] = act
        max[1] = lenght
        max[2] = actNWD
    return max if max[1] > 1 else [0,0,0]
        

def zad3():
    with open("trymestr_II/23_03_01/przyklad.txt") as file:
        T = [int(e.strip()) for e in file]
    max = [0,0,0]
    for i in range(len(T)-2):
        actMax = podciag(T[i:len(T)+1])
        if actMax[1] > max[1]:
            max[0] = actMax[0]
            max[1] = actMax[1]
            max[2] = actMax[2]
    print(T[max[0]],max[1],max[2])





zad3()