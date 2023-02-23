with open("trymestr_II/23_02_23/szyfrogram.txt") as f:
    T = [e.strip() for e in f]

def zad1():
    global T
    A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for e in T:
        l = list(e)
        for x in l:
            A[ord(x)-65] += 1  
    for i in range(len(A)):
        print(chr(i+65), A[i])

def zad2():
    print("ALGORYTM")

def zad3():
    global T
    A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for e in T:
        l = list(e)
        for x in l:
            A[ord(x)-65] += 1
    B = []
    with open("trymestr_II/23_02_23/czestosc.txt") as f:
        for e in f:
            a = e.strip().split()
            B.append(int(a[1]))
    C = []
    for x in T:
        l = list(x)
        for y in l:
            b = A[ord(y)-65]
            for i in range(26):
                if b == B[i]:
                    C.append(chr(i+65))
    print("".join(C))


