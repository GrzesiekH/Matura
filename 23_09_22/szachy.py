from curses.ascii import isupper


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
        for e in plansze:
            if e == ['\n'] :
                max = 0
                c = [0,0]
                w = True
                for x in figury:
                    if figury[x].isupper() and figury[x] != figury[x].lower():
                        w = False
                        break
                    elif figury[x] != figury[x].upper():
                        w =False
                        break
                if w :
                    c[0] += 1
                    
            for i in range(len(e)):
                if e[i] != ".":
                    figury[e[i]] += 1
        print(len(odp), min(odp))

zad2()