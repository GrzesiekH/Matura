def zad1():   
    with open("23_09_22/Dane/szachy_przyklad.txt") as file:
        plansze = []
        for e in file:
            plansze.append([*e[0:8]])
        plansze.append(["\n"])
        counterList = [0,0,0,0,0,0,0,0]
        counter = []
        for e in plansze:
            if e == ['\n'] :
                c = 0
                for x in counterList:
                    if x == 8:
                        c += 1
                if c != 0:
                    counter.append(c)
                counterList = [0,0,0,0,0,0,0,0]
                continue
            for i in range(len(e)):
                if e[i] == ".":
                    counterList[i] += 1
        print(len(counter), max(counter))
        
def zad2():
    with open("23_09_22/Dane/szachy_przyklad.txt") as file:
        plansze = []
        for e in file:
            plansze.append([*e[0:8]])
        plansze.append(["\n"])
        figury = {"K":0,"k":0, "W":0, "w":0, "S":0, "s":0,"H":0, "h":0, "G":0, "g":0, "P":0, "p":0 }
        odp = []
        max = 0
        for e in plansze:
            if e == ['\n'] :   
                c = 0
                w = True
                for x in figury:
                    if x.isupper() and figury[x] != figury[x.lower()]:
                        w = False
                        break
                    elif figury[x] != figury[x.upper()]:
                        w = False
                        break 
                if w :
                    for x in figury:
                        if figury[x] != 0:
                            c += figury[x]
                    odp.append(c)
                figury = {"K":0,"k":0, "W":0, "w":0, "S":0, "s":0,"H":0, "h":0, "G":0, "g":0, "P":0, "p":0 }
                continue
            for i in range(len(e)):
                if e[i] != ".":
                    figury[e[i]] += 1
        
        print(len(odp), min(odp))

def zad3():
    with open("23_09_22/Dane/szachy_przyklad.txt") as file:
        plansze = []
        for e in file:
            plansze.append([*e[0:8]])
        plansze.append(["\n"])
        czarny = []
        bialy = []
        szach = [] # biały, czarny
        for y in range(len(plansze)):
            if plansze[y] == "\n":
                wieza = False
                krol = False
                Szach = True
                for i in range(8): #x
                    if plansze[bialy[0]][i] != ".":
                        if plansze[bialy[0]][i] == "K":
                            krol = True
                        elif plansze[bialy[0]][i] == "W":
                            wieza = True
                        if not wieza and krol:
                            Szach = False
                            break
                        elif wieza and not krol:
                            Szach = False
                            break
                        elif wieza and krol:
                            break
                if Szach:
                    szach[0]+=1
                wieza = False
                krol = False
                Szach = True
                for i in range(8): #y 
                    if plansze[i][bialy[1]] != ".":
                        if plansze[i][bialy[1]] == "k":
                            krol = True
                        elif plansze[i][bialy[1]] == "w":
                            wieza = True
                        if not wieza and krol:
                            Szach = False
                            break
                        elif wieza and not krol:
                            Szach = False
                            break
                        elif wieza and krol:
                            break
                if Szach:
                    szach[0]+=1
                continue
            for x in range(8):
                if plansze[y][x] == "K": #biały
                    bialy = [y][x]
                elif plansze[y][x] == "k": #czarny
                    czarny = [y][x]
        print(szach)

zad3()