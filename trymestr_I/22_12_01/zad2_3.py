def mutateBack(t):
    gens = {"BD":"A", "CA": "B", "CD":"B", "DD":"C", "BC": "D"}
    gen = t
    while len(gen) != 1:
        nG = []
        for i in range(0,len(gen),2):
            gT = gen[i:i+2]
            if gT not in gens:
                return False
            else:
                nG.append(gens[gT])
        if len(nG) == 1:
            break
        else:
            gen = "".join(nG).strip()
    return True
with open("22_12_01/genetyka.txt") as file :
    list = []
    for y in file:
        list.append(y.strip())
        print(list[-1])
    # list = [e.strip() for e in file]
    counter = 0
    for x in list:
        if not mutateBack(str(x)):
            counter += 1
    print(counter)