def zad1():
    with open("22_12_08/przyklad_neon.txt") as file:
        list = [e.strip() for e in file]
        len = 0
        for x in list:
            X = x.split()
            if X[0] == "USUN":
                len -= 1
            elif X[0] == "DOPISZ":
                len+= 1
        print(len)

def zad2():
    with open("22_12_08/przyklad_neon.txt") as file:
        list = [e.strip() for e in file]
        komendy = [e.split()[0] for e in list]
        maks = [0,""]
        streak = [0,""]
        for x in komendy:
            if streak[0] == 0:
                streak[0] = 1
                streak[1] = x
            else:
                if x == streak[1]:
                    streak[0]+=1
                else:
                    if streak[0] > maks[0]:
                        maks[0] = streak[0]
                        maks[1] = streak[1]
                    streak[0] = 0
                    streak[1] = ""
        
        print(*maks)

def zad3():
    with open("22_12_08/przyklad_neon.txt") as file:
        list = [e.strip() for e in file]
        dop = []
        for e in list:
            if e.split()[0] == "DOPISZ":
                dop.append(e.split()[1])
        maks = [0,""]
        

zad3()