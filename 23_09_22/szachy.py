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
        figury = []
        odp = []
        for e in plansze:
            if e == ['\n'] :
                c = [0,0]
                for x in figury:
                    if x.isupper():
                        c[0]+=1
                    else:
                        c[1]+=1
                if c[0] != c[1]:
                    continue
                w = True
                for x in figury:
                    if x.isupper() and x.lower() not in figury:
                        w = False
                        break
                    elif x.upper() not in figury:
                        w = False
                        break
                if w:
                    odp.append(len(figury))

            for i in range(len(e)):
                if e[i] != ".":
                    figury.append(e[i])
        print(len(odp), min(odp))

zad2()