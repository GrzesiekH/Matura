def zad3():
    with open("trymestr_II/23_03_01/dane2_3.txt") as file:
        T = [e.strip() for e in file]
    for e in T:
        W = 0
        S = 0
        for i in range(len(e)):
            match e[i]:
                case "[":
                    S += 1
                case "]":
                    S -= 1
            if S>W:
                W = S
        print(W)

def zad4():
    with open("trymestr_II/23_03_01/dane2_4.txt") as file:
        T = [e.strip() for e in file]
    for e in T:
        S = 0
        for i in range(len(e)):
            match e[i]:
                case "[":
                    S += 1
                case "]":
                    S -= 1
            if S<0:
                break
        print("tak" if S == 0 else "nie")

zad3()
zad4()