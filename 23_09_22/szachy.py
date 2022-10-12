def zad1():   
    with open("23_09_22/Dane/szachy.txt") as file:
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
    with open("23_09_22/Dane/szachy.txt") as file:
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
                    if x.isupper() and figury[x] != figury[x.lower()] and figury[x] != 0:
                        w = False
                        break
                    elif figury[x] != figury[x.upper()] and figury[x] != 0:
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
    with open("23_09_22/Dane/szachy.txt") as file:
        plansze = []
        for e in file:
            plansze.append([*e[0:8]])
        plansze.append(["\n"])
        czarny = []
        bialy = []
        odp = [0,0] # biały, czarny
        for y in range(len(plansze)):
            if plansze[y] == ["\n"]:
                X = []
                Y = []
                Szach = False
                for i in range(8): #y
                    if plansze[y-8+i][bialy[1]] != ".":
                        Y.append(plansze[y-8+i][bialy[1]])
                for i in range(8): #x
                    if plansze[bialy[0]][i] != ".":
                        X.append(plansze[bialy[0]][i])
                for i in range(len(X)):
                    if X[i] == "K":
                        if i != len(X)-1 :
                            if X[i+1] == "w" :
                                Szach = True
                        if i != 0:
                            if X[i-1] == "w":
                                Szach = True
                
                for i in range(len(Y)):
                    if Y[i] == "K":
                        if i != len(Y)-1 :
                            if Y[i+1] == "w" :
                                Szach = True
                        if i != 0:
                            if Y[i-1] == "w":
                                Szach = True
                if Szach:
                    odp[1]+=1
                Szach = False
                X = []
                Y = []
                for i in range(8): #y
                    if plansze[y-8+i][czarny[1]] != ".":
                        Y.append(plansze[y-8+i][czarny[1]])
                for i in range(8): #x
                    if plansze[czarny[0]][i] != ".":
                        X.append(plansze[czarny[0]][i])
                for i in range(len(X)):
                    if X[i] == "k":
                        if i != len(X)-1 :
                            if X[i+1] == "W" :
                                Szach = True
                        if i != 0:
                            if X[i-1] == "W":
                                Szach = True
                
                for i in range(len(Y)):
                    if Y[i] == "k":
                        if i != len(Y)-1 :
                            if Y[i+1] == "W" :
                                Szach = True
                        if i != 0:
                            if Y[i-1] == "W":
                                Szach = True
                if Szach:
                    odp[0]+=1
                continue
            for x in range(8):
                if plansze[y][x] == "K": #biały
                    bialy = [y,x]
                elif plansze[y][x] == "k": #czarny
                    czarny = [y,x]
                
        print(*odp)

print("zad 1")
zad1()
print("zad 2")
zad2()
print("zad 3")
zad3()